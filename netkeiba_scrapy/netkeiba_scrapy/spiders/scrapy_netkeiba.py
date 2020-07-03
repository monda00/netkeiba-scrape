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
        with open('./url_test.csv') as f:
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
        rank = 1

        while self.exist_next_rank(response, rank):
            name = response.xpath(
                '//table[@class="table_slide_body ResultsByRaceDetail"]//tr[{}]/td[4]/a/text()'.format(rank)).extract_first()
            race_name = response.xpath(
                '//span[@class="RaceName_main"]/text()').extract_first()
            race_date = response.xpath(
                '//span[@class="Race_Date"]/text()').extract_first().replace('\n', '')
            frame_number = response.xpath(
                '//table[@class="table_slide_body ResultsByRaceDetail"]//tr[{}]/td[2]/text()'.format(rank)).extract_first()
            horse_number = response.xpath(
                '//table[@class="table_slide_body ResultsByRaceDetail"]//tr[{}]/td[3]/text()'.format(rank)).extract_first()
            age = response.xpath(
                '//table[@class="table_slide_body ResultsByRaceDetail"]//tr[{}]/td[5]/text()'.format(rank)).extract_first()
            weight = response.xpath(
                '//table[@class="table_slide_body ResultsByRaceDetail"]//tr[{}]/td[6]/text()'.format(rank)).extract_first()
            jockey = response.xpath(
                '//table[@class="table_slide_body ResultsByRaceDetail"]//tr[{}]/td[7]/a/text()'.format(rank)).extract_first()
            time = response.xpath(
                '//table[@class="table_slide_body ResultsByRaceDetail"]//tr[{}]/td[8]/text()'.format(rank)).extract_first()
            agari = response.xpath(
                '//table[@class="table_slide_body ResultsByRaceDetail"]//tr[{}]/td[12]/text()'.format(rank)).extract_first()
            win = response.xpath(
                '//table[@class="table_slide_body ResultsByRaceDetail"]//tr[{}]/td[13]/text()'.format(rank)).extract_first()
            popular = response.xpath(
                '//table[@class="table_slide_body ResultsByRaceDetail"]//tr[{}]/td[14]/text()'.format(rank)).extract_first()
            horse_weight = response.xpath(
                '//table[@class="table_slide_body ResultsByRaceDetail"]//tr[{}]/td[15]/text()'.format(rank)).extract_first()

            horse = Horse(
                name=name,
                race_name=race_name,
                race_date=race_date,
                frame_number=frame_number,
                horse_number=horse_number,
                age=age,
                weight=weight,
                jockey=jockey,
                time=time,
                agari=agari,
                win=win,
                popular=popular,
                horse_weight=horse_weight,
                rane=rank
            )
            yield {'horse': horse}
            rank += 1
        return

    def exist_next_rank(self, response, rank):
        """
        レースの結果一覧の次の順位があるか
        """
        if response.xpath('//table[@class="table_slide_body ResultsByRaceDetail"]//tr[{}]'.format(rank)).extract_first() is None:
            return False
        else:
            return True
