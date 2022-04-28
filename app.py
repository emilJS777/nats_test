import asyncio
import json
import ast

from nats.aio.client import Client as NATS
from nats.aio.errors import ErrTimeout
import time



class Broker:
    def __init__(self):
        asyncio.run(Broker.subscriber())


    @staticmethod
    async def subscriber():
        nc = NATS()

        while True:
            await nc.connect(servers=["nats://144.91.119.81:4222"])

            async def message_handler(msg):
                data = json.loads(msg.data.decode())
                print(data[0])

            # await nc.subscribe("payment", cb=message_handler)
            await nc.flush()

            await nc.publish("counters", json.dumps([{"id": "KK890", "coin": {'d': 20, 't': 15}, "bill": {'d': 0, 't': 15}, "bonus": {'d': 0, 't': 15}, "cashless": {'d': 0, 't': 15}, "service": {'d': 0, 't': 15}}]).encode())

            # await nc.publish("payment", json.dumps({"id": "KK890", "type": "coin", "price": 900, "currency": "amd"}).encode())


            # await nc.publish("content", json.dumps({"id": "yim7", "lather": 0, "water": 1}).encode())
            await asyncio.sleep(3)
            await nc.close()




Broker()
