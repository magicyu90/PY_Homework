# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem


class SztianqiSpider(scrapy.Spider):
    name = 'SZtianqi'
    allowed_domains = ['tianqi.com']
    start_urls = ['http://www.tianqi.com/suzhou/']

    def parse(self, response):
        items = []

        sevenday = response.xpath('//ul[@class="week"]/li')  # 日期
        sevenweathers = response.xpath('//ul[@class="txt txt2"]/li')  # 天气

        for day in sevenday:
            item = WeatherItem()
            date = day.xpath('./b/text()').extract()
            week = day.xpath('./span/text()').extract()
            item['date'] = date
            item['week'] = week
            items.append(item)

        for i in range(len(sevenweathers)):
            weather = sevenweathers[i].xpath('./text()').extract()
            items[i]['weather'] = weather

        return items
