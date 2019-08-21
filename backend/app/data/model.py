import os
import asyncio
from gino import Gino
from price import Price
from database import Database
db = Database.get()


async def main():
    await db.set_bind(os.environ["AWS_POSTGRES_CONNECTION"])

    # Create tables
    await db.gino.create_all()
    #p = await Price.create(external_id = "test", url= "url", price = 100)
    #print(p) 
    price = await Price.query.gino.all()
    print(price)

asyncio.get_event_loop().run_until_complete(main())