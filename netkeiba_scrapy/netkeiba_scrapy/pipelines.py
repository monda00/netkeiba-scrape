from scrapy.exporters import CsvItemExporter
from netkeiba_scrapy.items import RaceUrlItem, HorseItem

class NetkeibaScrapyPipeline:
    def open_spider(self, spider):
        if spider.name == 'scrapy_horse':
            self.csvfile = open('./output/horse.csv', 'wb')
        elif spider.name == 'scrapy_race':
            self.csvfile = open('./output/race.csv', 'wb')

        self.exporter = CsvItemExporter(self.csvfile)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.csvfile.close()
