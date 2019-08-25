import os
import asyncio
from gino import Gino
from price import Price
from item import Item
from database import Database
db = Database.get()


async def main():
    await db.set_bind(os.environ["AWS_POSTGRES_CONNECTION"])

    # Create tables
    await db.gino.create_all()
    await Item.create(fetcher_name='amazon', url='https://www.amazon.com/dp/B01FOHJAY0?aaxitk=Zjo6TKFu.6I7aMNex51ZoQ&pd_rd_i=B01FOHJAY0&pf_rd_p=9420597b-7dad-4cbd-a28d-7d676ac67378&hsa_cr_id=3555886890201&sb-ci-n=asinImage&sb-ci-v=https%3A%2F%2Fimages-na.ssl-images-amazon.com%2Fimages%2FI%2F61QgIdENkhL.jpg&sb-ci-a=B01FOHJAY0')
    #p = await Price.create(external_id = "test", url= "url", price = 100)
    #print(p) 
    all_items = await Item.query.gino.all()
    print(all_items)

asyncio.get_event_loop().run_until_complete(main())