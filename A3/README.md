# CS58A
CS158A - Summer 2025 - Assignment
A3 - LEADER ELECTION PROBLEM

This application is to create a chat server and a chat client program that allow users to join a chat room and leave the chat room whenever they like. 

To set up this program and have it running. Please follow these steps below:

Step 1: Download all of the files from directory A3 on Github link: https://github.com/Tinypawo8/CS158A.git
config1.txt
config2.txt
config3.txt
log1.txt
log2.txt
log3.txt
myleprocess.py

Step 2: Create a folders name NodeA, NodeB, NodeC and copy these 2 in each folder
1. myleprocess.py
2. config.txt (renamed from config1.txt)

Step3: Open 3 terminal window and cd into the folders above. Run the command "python3 myleprocess.py" on each terminal

Step 3: After you run them the result should be like this in the 3 terminals:

tinypaw@Tinypaws-Laptop NodeA % python3 myleprocess.py
Node started with UUID: 6f513abd-9cb2-4b7c-905f-30f025422f3d
Client connected
Sent: uuid=6f513abd-9cb2-4b7c-905f-30f025422f3d, flag=0
Server connected
Received: uuid=7876d553-70a5-4760-82da-2593560d7a44, flag=0, greater, 0
Sent: uuid=7876d553-70a5-4760-82da-2593560d7a44, flag=0
Received: uuid=7876d553-70a5-4760-82da-2593560d7a44, flag=1, greater, 0
Sent: uuid=7876d553-70a5-4760-82da-2593560d7a44, flag=1

tinypaw@Tinypaws-Laptop NodeB % python3 myleprocess.py
Node started with UUID: 181643d1-9911-4b08-8434-bce837d0bc24
Server connected
Received: uuid=6f513abd-9cb2-4b7c-905f-30f025422f3d, flag=0, greater, 0
Send failed: 'NoneType' object has no attribute 'sendall'
Client connected
Sent: uuid=181643d1-9911-4b08-8434-bce837d0bc24, flag=0
Received: uuid=7876d553-70a5-4760-82da-2593560d7a44, flag=0, greater, 0
Sent: uuid=7876d553-70a5-4760-82da-2593560d7a44, flag=0
Received: uuid=7876d553-70a5-4760-82da-2593560d7a44, flag=1, greater, 0
Sent: uuid=7876d553-70a5-4760-82da-2593560d7a44, flag=1

tinypaw@Tinypaws-Laptop NodeC % python3 myleprocess.py
Node started with UUID: 7876d553-70a5-4760-82da-2593560d7a44
Server connected
Client connected
Received: uuid=181643d1-9911-4b08-8434-bce837d0bc24, flag=0, less, 0
Message ignored.
Sent: uuid=7876d553-70a5-4760-82da-2593560d7a44, flag=0
Received: uuid=7876d553-70a5-4760-82da-2593560d7a44, flag=0, same, 0
Leader is decided to 7876d553-70a5-4760-82da-2593560d7a44
Sent: uuid=7876d553-70a5-4760-82da-2593560d7a44, flag=1
Received: uuid=7876d553-70a5-4760-82da-2593560d7a44, flag=1, same, 1, leader=7876d553-70a5-4760-82da-2593560d7a44
Leader message completed a full ring. Stopping forwarding.


Step 5: Hit control + C to end the programs on each terminal.