from pifetcher.core import FetchWorker, Config
from data import DB

class PriceFetcher(FetchWorker):
    def on_save_result(self, result):
        DB.save_price(result)
        
    def on_empty_result_error(self):
        self.stop()
    def on_start_process_signal(self):
        works = [ {"fetcher_name":item["fetcher_name"], "url":item["url"]} for item in DB.get_items()]
        self.add_works(works)

if __name__ == '__main__':
    Config.use('pifetcherConfig.json')
    fetcher = PriceFetcher()
    fetcher.do_works()