from settings import *
from src.logging_helper import function_logs

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

        self.connections: dict[Connection] = {}

    @function_logs
    def bind(self) -> None:

        self.UDPServerSocket.bind(ADDRESS)

    @function_logs
    def add_conn(self, data: tuple) -> None:
        ...

    @function_logs
    def del_conn(self, data: tuple) -> None:
        ...

    @function_logs
    async def listen(self) -> int | tuple[any, any, any]:

        bytes_address_pair = self.UDPServerSocket.recvfrom(BUFFERSIZE)

        if not bytes_address_pair:
            return Server.EMPTY

        message = bytes_address_pair[0]
        address = bytes_address_pair[1]

        try:
            message = json.loads(message)
        except TypeError:
            return Server.INVALID, address, Server.INCORRECT_MESSAGE_FORMAT

        return Server.VALID, address, message
