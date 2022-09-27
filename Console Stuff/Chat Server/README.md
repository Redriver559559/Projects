<h1>Updates</h1>
<li>Added a new 'history' feature. It is only serverside running at the moment, meaning no messages are save when the server shuts down, only during the connection with other clients.</li>
<li>Re did the message system for better parsing and faster speeds, you no longer need to translate any messages.</li>
<li>Buffer size increased from 1024 to 64000</li>
<li>Command re work</li>
<li>Reconnect and username login with multiple (infinte) trys</li>

<h1>Issues</h1>
<li>When sending messages bigger than the buffer limit, the buffer will stop and just break for that client</li>
<li>When sending anything with a single slash, or putting brackets around something like '[white]' the color parser will freak out and color for you. Kind of a cool bug</li>

<h1>to-do</h1>
<li>Fix the message formmating for proper data control</li>
<li>proper error handling and ,again, better data format for this and many other issues</li>
<li>make clustered servers</li>
<li>make channels</li>
<li>save messages in some sort of database</li>
<li>add TLS, or SSL (probably SSL)</li>
