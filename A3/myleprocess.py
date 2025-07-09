import socket
import threading
import uuid
import time
import json

LOG_FILE = "log.txt"
STATE_FINDING = 0
STATE_KNOWS_LEADER = 1

#Create a message class
class Message:
    def __init__(self, uuid_val, flag):
        self.uuid = str(uuid_val)
        self.flag = flag

    def to_json(self):
        return json.dumps(self.__dict__) + "\n"

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str.strip())
        return Message(data['uuid'], data['flag'])

#Create a node class
class Node:
    def __init__(self):
        self.uuid = uuid.uuid4()
        self.state = STATE_FINDING
        self.leader_id = None
        self.server_conn = None
        self.client_conn = None
        self.lock = threading.Lock()
        self.read_config()

    #Create a function to read input from the config.txt file
    def read_config(self):
        with open("config.txt") as f:
            lines = f.read().splitlines()
        self.server_ip, self.server_port = lines[0].split(',')
        self.client_ip, self.client_port = lines[1].split(',')
        #Convert string into number for port variables
        self.server_port = int(self.server_port)
        self.client_port = int(self.client_port)

    #Create a log function to write message to a log.txt file
    def log(self, msg):
        with self.lock:
            with open(LOG_FILE, "a") as f:
                f.write(msg + "\n")
            print(msg)

    #create a function to hadle connections
    def handle_connection(self, conn):
        buffer = ""
        while True:
            try:
                data = conn.recv(1024).decode()
                if not data:
                    break
                buffer += data
                while "\n" in buffer:
                    line, buffer = buffer.split("\n", 1)
                    msg = Message.from_json(line)
                    self.process_message(msg)
            except Exception as e:
                self.log(f"Error in receiving: {e}")
                break
    
    # Start the server and listen to connection from another port.
    def start_server(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.server_ip, self.server_port))
        s.listen(1)
        conn, _ = s.accept()
        self.server_conn = conn
        self.log("Server connected")
        self.handle_connection(conn)

    #Connect with client
    def connect_to_client(self):
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((self.client_ip, self.client_port))
                self.client_conn = s
                self.log("Client connected")
                break
            except ConnectionRefusedError:
                time.sleep(1)
    #Send message and log the messge sent
    def send_message(self, message):
        try:
            msg_json = message.to_json()
            self.client_conn.sendall(msg_json.encode())
            self.log(f"Sent: uuid={message.uuid}, flag={message.flag}")
        except Exception as e:
            self.log(f"Send failed: {e}")

    def process_message(self, message):
        msg_uuid = uuid.UUID(message.uuid)
        comparison = "same" if msg_uuid == self.uuid else "greater" if msg_uuid > self.uuid else "less"

        log_msg = f"Received: uuid={message.uuid}, flag={message.flag}, {comparison}, {self.state}"
        if self.state == STATE_KNOWS_LEADER:
            log_msg += f", leader={self.leader_id}"
        self.log(log_msg)

        if message.flag == 1:
            if self.state == STATE_KNOWS_LEADER and message.uuid == self.leader_id:
                self.log("Leader message completed a full ring. Stopping forwarding.")
                return
            self.state = STATE_KNOWS_LEADER
            self.leader_id = message.uuid
            self.send_message(message)
            return

        if msg_uuid == self.uuid:
            self.state = STATE_KNOWS_LEADER
            self.leader_id = str(self.uuid)
            self.log(f"Leader is decided to {self.leader_id}")
            self.send_message(Message(self.uuid, 1))
            return

        if msg_uuid > self.uuid:
            self.send_message(message)
        else:
            self.log("Message ignored.")

    def start(self):
        print(f"Node started with UUID: {self.uuid}")
        threading.Thread(target=self.start_server, daemon=True).start()
        time.sleep(2)
        self.connect_to_client()
        time.sleep(2)
        initial_msg = Message(self.uuid, 0)
        self.send_message(initial_msg)

        while True:
            time.sleep(1)

if __name__ == "__main__":
    node = Node()
    node.start()
