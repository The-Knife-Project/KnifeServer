from src.connection import Server
from settings import RESTING_TIME, ADDRESS
from src.logging_helper import *

import asyncio

server: Server = Server()
server.bind()


@function_logs
async def main() -> None:
    info('server is up and running on: %s : %s' % ADDRESS)

    while True:
        data = await server.listen()

        if data[0] == Server.INVALID or data[0] == Server.EMPTY:
            continue

        debug('message received: %s, from %s' % (str(data[2]).replace('\n', '\\n'), data[1]))

        await asyncio.sleep(RESTING_TIME)


asyncio.run(main())
