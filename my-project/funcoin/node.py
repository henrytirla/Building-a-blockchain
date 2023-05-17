import asyncio
from funcoin.blockchain import  Blockchain
from funcoin.connections import ConnectionPool
from funcoin.peers import P2PProtocol
from funcoin.server import Server

blockchain = Blockchain()
connection_pool = ConnectionPool

server= Server(blockchain,connection_pool,P2PProtocol)

async def main():
      await server.listen()


asyncio.run(main())