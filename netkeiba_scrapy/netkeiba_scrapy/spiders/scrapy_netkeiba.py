# -*- coding: utf-8 -*-
import scrapy
from netkeiba_scrapy.items import RaceUrl

class ScrapyNetkeibaSpider(scrapy.Spider):
    name = 'scrapy_netkeiba'
    allowed_domains = ['db.sp.netkeiba.com']
    base_url = 'https://db.sp.netkeiba.com'
    page_num = 1
    start_year = 2019
    end_year = 2020
    start_urls = [
        base_url + '/?pid=race_list&start_year=' +
        str(start_year) + '&end_year=' + str(end_year) + '&page=' + str(page_num)
    ]

    def parse(self, response):

        urls = response.xpath('//div[@class="LinkBox_01 fc"]/a/@href').extract()
        for url in urls:
            yield RaceUrl(url=url)

    def exist_next_page(self, response):
        """
        次のページがあるか判定
        「次へ」にhrefがあるかで判定する
        """
        exist = False

        return exist
