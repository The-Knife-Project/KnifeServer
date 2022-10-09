from settings import *

import socket
from socket import socket as sc
import json

class Connection(object):

    def __init__(self, address, connected=False):

        self.address = address
        self.connected = connected


class Server(object):

    VALID = 0
    INVALID = 1
    EMPTY = 2

    INCORRECT_MESSAGE_FORMAT = 100

    def __init__(self) -> None:

        self.UDPServerSocket = sc(
            family=socket.AF_INET,
            type=socket.SOCK_DGRAM
        )

        self.connections: list[Connection] = {}

    def bind(self) -> None:

        self.UDPServerSocket.bind(ADDRESS)
        # self.UDPServerSocket.setblocking(False)
    
    def add_conn(self, data: tuple) -> None: ...
    def del_conn(self, data: tuple) -> None: ...

    async def listen(self) -> None:

        bytes_address_pair = self.UDPServerSocket.recvfrom(BUFFERSIZE)

        if not bytes_address_pair:
            return Server.EMPTY

        message = bytes_address_pair[0]
        address = bytes_address_pair[1]

        try:
            message = json.loads(message)
        except TypeError:
            return (Server.INVALID, address, Server.INCORRECT_MESSAGE_FORMAT)

        return (Server.VALID, address, message)
