from socket import *

serverPort = 12000
buffSize = 64

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    #accept
    cnSocket, addr = serverSocket.accept()
    print(f"Connected from {addr}")

    #receive
    data = cnSocket.recv(buffSize).decode()
    msg_len = int(data[:2])
    message_body = data[2:]

    print(f"msg_len: {msg_len}")
    print(f"processed: {message_body}")

    #proccess
    response = message_body.upper()
    response_packet = f"{len(response):02}" + response
    msg_len_sent = len(response)
    print(f"msg_len_sent: {msg_len_sent}")

    #send
    cnSocket.send(response_packet.encode())

    #close
    cnSocket.close()
    print("Connection closed\n")
    
serverSocket.close()
