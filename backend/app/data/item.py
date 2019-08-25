import os
import asyncio
import datetime
from gino import Gino
from database import Database

db = Database.get()

class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer(), primary_key=True)
    fetcher_name = db.Column(db.Unicode())
    external_id = db.Column(db.Unicode())
    url = db.Column(db.Unicode())
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
