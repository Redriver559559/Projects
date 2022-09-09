import datetime
import asyncio
import aioconsole
import json
from rich import print

#This is currently still a work in progress, more will be added soon.

class Client():
    """Client class for handling information about the host, port, username, and if it is connected"""
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.username = None
        self.writer = None
        self.reader = None
        self.connected = False

    #trys to connect to server until succesful
    async def connect(self):
        while self.connected == False:
            print('Connecting...')
            try:
                self.reader, self.writer = await asyncio.open_connection('localhost', 9090)
                self.connected = True
            except ConnectionRefusedError:
                pass
        print(f"Connected to {self.writer.get_extra_info('peername')}\n")
        await self.login()
        
    async def login(self):
        """Takes in the users login and saves the username, the password is just input and is not stored anywhere"""
        self.username = input('Username: ')
        password = input('Password: ')
        data = json.dumps({'username':self.username, 'password':password}).encode()
        self.writer.write(data)
        await self.writer.drain()
    
    @staticmethod
    async def get_time():
        """Gets the users current time and returns a time object"""
        time = datetime.datetime.now()
        return (time.strftime("%m/%d/%Y %#I:%M %p"))
    
    async def send_message(self, message):
        data = json.dumps({'message':message}).encode()
        self.writer.write(data)
        await self.writer.drain()

    async def format_message(self, message_data):
        sender = message_data['sender']
        message = message_data['message']
        if sender == self.username: #Blue for your username
            return(f"[blue]{self.username} : [white]{message}[/white] [grey37]{await self.get_time()}")
        elif sender == 'Server':
            return(f"[yellow]{sender} : [white]{message}[/white] [grey37]{await self.get_time()}")
        else:
            return(f"[red]{sender} : [white]{message} [grey37]{await self.get_time()}")

    async def recv_message(self):
        """Recieves messages from the server and checks the message data for usernames. Basic coloring for other names and the server messages"""
        while True:
            try:
                data = (await self.reader.readuntil(b'}'))
                message_data = json.loads(data)
            except ConnectionResetError:
                print("Connection Disconnected...")
                self.connected = False
                await self.connect()

            message = await self.format_message(message_data)
            print(message)

    async def receive_input(self):
        """Sends the message to the server / host machine."""
        while True:
            message = (await aioconsole.ainput())
            if len(message) > 20000:
                print('Too Long!')
            else:
                await self.send_message(message)
    
    async def run_client(self):
        await self.connect()
        recieve_message = asyncio.create_task(client.recv_message())
        send_message = asyncio.create_task(client.receive_input())

        await asyncio.gather(recieve_message, send_message)

client = Client('127.0.0.1', 8888)
asyncio.run(client.run_client())
