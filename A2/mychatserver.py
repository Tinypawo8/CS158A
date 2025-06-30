import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

#create a list to store clients that connect to server
clients = []

#create lock for threading to ensure one thread can access to a share resource at a time
lock = threading.Lock()

#create a broadcase function to send message to all other clients
def broadcast(message, _client=None):
    with lock:
        for client in clients:
            if client != _client:
                client.send(message)
                
#create a function to handle a new client connect to server
def handle(client):
    port = client.getpeername()[1]
    address = client.getpeername()[0]
    print(f"New connection from {client.getpeername()}") 

    #Listen out to message and broadcast it to server and all other client
    while True:
        try:
            message = receive_full_message(client)
            if message:
                broadcast(f"[{port}]: {message.decode()}".encode(), client)
                print(f"{port}: {message.decode()}")
        except:
            break

    #remove disconncted client
    with lock:
        if client in clients:
            clients.remove(client)
        
    client.close()
    broadcast(f"[{port}] Disconnected from server.\n".encode())
    print((f"[{port}] Disconnected from server.".encode().decode()))


#create a function to handle long message in chunks
def receive_full_message(client):
    buffer = b""
    while True:
        chunk = client.recv(1024)
        if not chunk:
            break  # client disconnected
        buffer += chunk
        if b"<END>" in buffer:
            break
    return buffer.replace(b"<END>", b"")

#create a function to receive connection from clients
def receive():
    print(f"Server listening on {HOST}:{PORT}")
    while True:
        client, address = server.accept()
        with lock:
            clients.append(client)
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
