
#CS158A - Summer 2025 - Assignment
A4 - LEADER ELECTION PROBLEM - Debugged - Rerun

This application is to create a chat server and a chat client program that allow users to join a chat room and leave the chat room whenever they like. 

To set up this program and have it running. Please follow these steps below:

Step 1: Download all of the files from directory A3 on Github link: https://github.com/Tinypawo8/CS158A.git
Node1: 
log.txt
config.txt
Myleprocess.py

Node2:
log.txt
config.txt
myleprocess.py

Node3:
log.txt
config.txt
myleprocess.py

Step2: Open 3 terminal window and cd into the folders above. Run the command "python3 myleprocess.py" on each terminal in the order of Node3, Node1, Node 2 quickly right after each another.

Step 3: After you run them the result should be something similar with this in the 3 terminals:

Node1 terminal: 
tinypaw@Tinypaws-Laptop Node1 % python3 myleprocess.py
Node started with UUID: 44e7ab1f-a19a-4df1-bfb5-e795e756447b
Server listening...
Client connected
Received: uuid=c8eb0692-dfda-4e35-8a60-90e9494911ad, flag=0, greater, 0
Sent: uuid=c8eb0692-dfda-4e35-8a60-90e9494911ad, flag=0
Sent: uuid=44e7ab1f-a19a-4df1-bfb5-e795e756447b, flag=0
Received: uuid=e337f44e-b53b-4fd2-8c26-23edb0c7641f, flag=0, greater, 0
Received: uuid=e337f44e-b53b-4fd2-8c26-23edb0c7641f, flag=1, greater, 0
Sent: uuid=e337f44e-b53b-4fd2-8c26-23edb0c7641f, flag=0
Sent: uuid=e337f44e-b53b-4fd2-8c26-23edb0c7641f, flag=1

Node2 terminal:
tinypaw@Tinypaws-Laptop Node2 % python3 myleprocess.py 
Node started with UUID: e337f44e-b53b-4fd2-8c26-23edb0c7641f
Server listening...
Received: uuid=c8eb0692-dfda-4e35-8a60-90e9494911ad, flag=0, less, 0
Message ignored.
Client connected
Received: uuid=44e7ab1f-a19a-4df1-bfb5-e795e756447b, flag=0, less, 0
Message ignored.
Received: uuid=e337f44e-b53b-4fd2-8c26-23edb0c7641f, flag=0, same, 0
Leader is decided to e337f44e-b53b-4fd2-8c26-23edb0c7641f
Received: uuid=e337f44e-b53b-4fd2-8c26-23edb0c7641f, flag=1, same, 1, leader=e337f44e-b53b-4fd2-8c26-23edb0c7641f
Leader message completed a full ring. Stopping forwarding.
Sent: uuid=e337f44e-b53b-4fd2-8c26-23edb0c7641f, flag=0
Sent: uuid=e337f44e-b53b-4fd2-8c26-23edb0c7641f, flag=1

Node3 terminal:
tinypaw@Tinypaws-Laptop Node3 % python3 myleprocess.py
Node started with UUID: c8eb0692-dfda-4e35-8a60-90e9494911ad
Server listening...
Client connected
Sent: uuid=c8eb0692-dfda-4e35-8a60-90e9494911ad, flag=0
Received: uuid=e337f44e-b53b-4fd2-8c26-23edb0c7641f, flag=0, greater, 0
Received: uuid=e337f44e-b53b-4fd2-8c26-23edb0c7641f, flag=1, greater, 0
Sent: uuid=e337f44e-b53b-4fd2-8c26-23edb0c7641f, flag=0
Sent: uuid=e337f44e-b53b-4fd2-8c26-23edb0c7641f, flag=1

Step 4: Hit control + C to end the programs on each terminal.