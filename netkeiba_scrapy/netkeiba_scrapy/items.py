# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RaceUrl(scrapy.Item):
    url = scrapy.Field()

class Horse(scrapy.Item):
    name = scrapy.Field()
    race_name = scrapy.Field()
    race_date = scrapy.Field()
    frame_number = scrapy.Field()
    horse_number = scrapy.Field()
    age = scrapy.Field()
    weight = scrapy.Field()
    jockey = scrapy.Field()
    time = scrapy.Field()
    agari = scrapy.Field()
    win = scrapy.Field()
    popular = scrapy.Field()
    horse_weight = scrapy.Field()
    rank = scrapy.Field()
