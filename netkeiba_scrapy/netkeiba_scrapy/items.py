# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RaceUrlItem(scrapy.Item):
    url = scrapy.Field()

class HorseItem(scrapy.Item):
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

class RaceItem(scrapy.Item):
    name = scrapy.Field()
    date = scrapy.Field()
    start_time = scrapy.Field()
    place = scrapy.Field()
    race_round = scrapy.Field()
    distance = scrapy.Field()
    clockwise = scrapy.Field()
    field_type = scrapy.Field()
    field_condition = scrapy.Field()
    weather = scrapy.Field()
