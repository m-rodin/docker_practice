import asyncio
import asyncio_redis
import asyncpg
import time

async def process():
    pg = await asyncpg.connect(user='docker', password='docker', database='docker', host='db')
    redis = await asyncio_redis.Connection.create(host='redis', port=6379)
    
    while True:
        item = await redis.blpop(["queue:raw"])
        print("Got message: ", item.value)
        await pg.execute('''INSERT INTO messages(message) VALUES($1)''', item.value)
        print("The message was saved in the db")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(process())
