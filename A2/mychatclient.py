import socket
import threading
import sys

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("Connected to chat server. Type 'exit' to leave.")

#create a function to receive message from server
def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            client.close()
            break
#create function to send message to sever so that server can broadcast it
def write():
    while True:
        message = input()
        if message.lower() == 'exit':
            print("Disconnected from server")
            client.close()
            break
        try:
            message += "<END>"
            client.sendall(message.encode())
        except:
            break

# Start threads
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
