import os
import asyncio
from gino import Gino

db = Gino()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    nickname = db.Column(db.Unicode(), default='noname')


async def main():
    await db.set_bind(os.environ["AWS_POSTGRES_CONNECTION"])

    # Create tables
    await db.gino.create_all()
    u1 = await User.create(nickname='test_user')
    print(u1.id, u1.nickname) 
    user = await User.query.where(User.nickname == 'test_user').gino.first()
    print(user)

asyncio.get_event_loop().run_until_complete(main())