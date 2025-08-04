import ssl
import socket
import threading
import sys

lock = threading.Lock()

def connect_to_google():
        HOST = 'www.google.com'
        PORT = 443

        # Create a socket and wrap it in an SSL context
        context = ssl.create_default_context()

        with socket.create_connection((HOST, PORT)) as sock:
                with context.wrap_socket(sock, server_hostname=HOST) as ssock:
                    print(f"Connected to {HOST} with {ssock.version()}")

                    # Send a simple HTTP GET request to host - Google
                    request = f"GET / HTTP/1.1\r\nHost: {HOST}\r\nConnection: close\r\n\r\n"
                    ssock.sendall(request.encode("utf-8"))

                    # Receive and append response in a string - response
                    response = b""
                    while True:
                        data = ssock.recv(4096)
                        if not data:
                            break
                        response += data
                    
        # Split headers and body
        header_data, _, body = response.partition(b"\r\n\r\n")

        #Decode the body data
        decoded_body = body.decode("utf-8", errors="ignore")

        # Save body into an html file
        with open("response.html", "w", encoding="utf-8") as f:
                f.write(decoded_body)

        print("Saved Google homepage to response.html")

if __name__ == "__main__":
    connect_to_google()
