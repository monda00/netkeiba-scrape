# -*- coding: utf-8 -*-
import csv
import scrapy
from netkeiba_scrapy.items import RaceUrl
from netkeiba_scrapy.items import Horse

class RaceUrlSpider(scrapy.Spider):
    name = 'scrapy_race_url'
    allowed_domains = ['db.sp.netkeiba.com']
    base_url = 'https://db.sp.netkeiba.com'
    start_year = 2019
    end_year = 2020
    start_urls = [
        base_url + '/?pid=race_list&start_year=' +
        str(start_year) + '&end_year=' + str(end_year) + '&page=1'
    ]

    def parse(self, response):
        """
        検索ページのレース一覧からレースのURLを取得する
        """
        urls = response.xpath('//div[@class="LinkBox_01 fc"]/a/@href').extract()
        for url in urls:
            yield RaceUrl(url=url)

        if self.exist_next_page(response):
            next_page_url = self.base_url + response.xpath(
                '//div[@class="Common_Pager"]//a[@title="次へ"]/@href').extract_first()
            yield scrapy.Request(next_page_url, callback=self.parse)
        else:
            return

    def exist_next_page(self, response):
        """
        次のページがあるか判定
        「次へ」にhrefがあるかで判定する
        """
        if response.xpath('//div[@class="Common_Pager"]//a[@title="次へ"]/@href').extract_first() is None:
            return False
        else:
            return True

class Horse(scrapy.Spider):
    name = 'scrapy_horse'
    allowed_domains = ['db.sp.netkeiba.com']

    def start_requests(self):
        """
        csvファイルからurlのリストを取得
        """
        urls = []
        with open('../../url.csv') as f:
            reader = csv.reader(f)
            for row in reader:
                if not row[0] == 'url':
                    urls.append(row)

        for url in urls:
            yield scrapy.Request(url[0], self.parse)

    def parse(self, response):
        """
        レースページから各馬の情報を取得
        """

    def exist_next_rank():
        """
        レースの結果一覧の次の順位があるか
        """
        return False
