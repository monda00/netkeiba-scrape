# -*- coding: utf-8 -*-
import scrapy


class ScrapyNetkeibaSpider(scrapy.Spider):
    name = 'scrapy_netkeiba'
    allowed_domains = ['db.sp.netkeiba.com']
    start_urls = ['http://db.sp.netkeiba.com/']

    def parse(self, response):
        pass
