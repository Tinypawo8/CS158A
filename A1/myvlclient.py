from socket import *

serverName = 'localhost'
serverPort = 12000
buffSize = 64

# TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print("Connected")

# Input
sentence = input('Input lowercase sentence: ')

# Send
clientSocket.send(sentence.encode())

# Receive
received_data = clientSocket.recv(buffSize)
response_length = int(received_data[:2].decode())
response_message = received_data[2:2 + response_length].decode()

print('From Server:', response_message)

clientSocket.close()
