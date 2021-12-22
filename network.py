import socket

class Network:
    def __init__(self, server, port) -> None:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = server
        self.port = port
        self.addr = (self.ip, self.port)
        self.pos = self.connect() # Network class function

    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr) # socket library method
            return self.client.recv(2048).decode()
        except:
            pass

    # send data to server
    # return value = data received from server
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)