import os
import asyncio
import datetime
from gino import Gino
from database import Database

db = Database.get()

class Price(db.Model):
    __tablename__ = 'price'

    id = db.Column(db.Integer(), primary_key=True)
    external_id = db.Column(db.Unicode())
    url = db.Column(db.Unicode())
    price = db.Column(db.Integer())
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
