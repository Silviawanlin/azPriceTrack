from gino import Gino
db = Gino()
class Database:
    @staticmethod
    def get():
        return db