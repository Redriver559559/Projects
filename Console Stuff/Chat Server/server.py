import asyncio
import json
import inspect

#adress information
host, port = ('127.0.0.1', 9090)
clients = dict()
banned_users = set()

class Client:
    """Client class for storing client information such as task, username and more"""
    def __init__(self, reader, writer, task):
        self.reader = reader
        self.writer = writer
        self.task = task
        self.username = None

class Commands:
    prefix = '//'
    commands = {}
    def command(name):
        def wrapper(command):
            Commands.commands[name] = command
            return command
        return wrapper

@Commands.command('users')
async def users_online():
    user_list = [x for x in clients.keys()]
    await server_broadcast('Server', f'Users online: {user_list}')

async def broadcast(client, data):
    format = {'sender':client.username, 'message':data, 'message_type':'public'}
    data = json.dumps(format).encode()
    for client in clients.values():
        await send_data(client, data)

@Commands.command('broadcast')
async def server_broadcast(client, data):
    data = ''.join(data)
    format = {'sender':'Server', 'message':data, 'message_type':'public'}
    data = json.dumps(format).encode()
    for client in clients.values():
        await send_data(client, data)

@Commands.command('message')
async def message(client, data):
    target_username = data[0]
    if target_username in clients:
        target_client = clients[target_username]
        data = ' '.join(data)
    format = {'sender':client.username, 'message':data, 'message_type':'private'}
    data = json.dumps(format).encode()
    await send_data(client, data)
    await send_data(target_client, data)

async def server_message(client, data):
    format = {'sender':'Server', 'message':data, 'message_type':'public'}
    data = json.dumps(format).encode()
    await send_data(client, data)

async def user_leave(client):
        client.task.cancel()
        if client.username != None:
            del clients[client.username]
        if not client.writer.is_closing():
            client.writer.close()
            await client.writer.wait_closed()

async def send_data(client, data):
    client.writer.write(data)
    await client.writer.drain()

#recieives data from the client, loads the data as a json.
async def receive_data(client): 
    try:
        data = await client.reader.readuntil(b'}')
        return json.loads(data)
    except ConnectionResetError:
        await client.user_leave()

async def check_command(client, data):
    command_name, *arguments = data.split()
    command_name = command_name[len(Commands.prefix):]
    if command_name in Commands.commands:
        command = Commands.commands[command_name]
        if len(arguments) == 0:
            try:
                await command()
            except TypeError:
                await server_message(client, f'The command "{command_name}" requires 1 or more parameters.')
                args = inspect.signature(command)
                print(args.parameters)
        elif len(arguments) > 0:
            try:
                await command(client, arguments)

            except TypeError:
                await server_message(client, f'The command "{command_name}" requires no parameters')
    else:
        await broadcast(client, data)
        
async def check_message(client, message):
    if message.startswith(Commands.prefix):
        await check_command(client, message)
    else:
        await broadcast(client, message)
        
#main client handler that cheks messages and broadcasts them
async def handle_client(client):
    while True:
        data = await receive_data(client)
        message = data['message']
        if message == None:
            return
        await check_message(client, message)

#checks user identity and validates them
async def login(client):
    login_data = await receive_data(client)
    username = login_data['username']
    if username in banned_users:
        await user_leave(client)
    client.username = username
    clients[client.username] = client

#creates a client when a user connects and starts login and the client proccesses 
async def client_connected(reader, writer):
    task = asyncio.current_task(loop=None)
    client = Client(reader, writer, task)
    await login(client)
    await server_message(client, 'Logged in!')
    await handle_client(client)

#just listens for connections and makes courotines when they connect
async def run_server():
    server = await asyncio.start_server(client_connected, host, port)
    print('Server started!')
    async with server:
        await server.serve_forever()

asyncio.run(run_server())
