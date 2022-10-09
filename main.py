from src.connection import Server
from settings import RESTING_TIME, ADDRESS

import asyncio


server: Server = Server()
server.bind()

async def main() -> None:

    print('server is up and running on: %s : %s' % ADDRESS)

    while True:

        data = await server.listen()
        print(data)

        asyncio.sleep(RESTING_TIME)

asyncio.run(main())

