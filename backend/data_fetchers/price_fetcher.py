from pifetcher.core import FetchWorker, Config
from data import DB
from datetime import datetime


class PriceFetcher(FetchWorker):
    def on_save_result(self, price, batch_id, work):
        now = datetime.now()
        price['date'] = now.strftime('%m/%d/%Y')
        price['time'] = now.strftime('%H:%M:%S')
        DB.save_price(price)

    def on_empty_result_error(self):
        self.stop()

    def on_batch_start(self, batch_id):
        works = [ {"fetcherName":item["fetcherName"], "url": "https://"+item["host"]+"/dp/"+item["itemId"]} for item in DB.get_items()]
        print(works)
        self.add_works(works)

    def on_batch_finish(self, batch_id):
        print("batch finished " + batch_id)


if __name__ == '__main__':
    fetcher = PriceFetcher()
    fetcher.init('pifetcherConfig.json')
    fetcher.send_start_signal()
    fetcher.do_works()
