# -*- coding: utf-8 -*-
import scrapy
from SF.items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    baseURL = 'http://hr.tencent.com/position.php?&start='
    offset = 0
    start_urls = [baseURL+str(offset)]

    def parse(self, response):
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for node in node_list:
            item = TencentItem()
            item['positionName'] = node.xpath('./td[1]/a/text()').extract()[0]
            item['positionLink'] = node.xpath('./td[1]/a/@href').extract()[0]
            item['positionType'] = node.xpath('./td[2]/text()').extract()[0]
            item['positionNumber'] = node.xpath('./td[3]/text()').extract()[0]
            item['workLocation'] = node.xpath('./td[4]/text()').extract()[0]
            item['publishTime'] = node.xpath('./td[5]/text()').extract()[0]
            yield item

        if self.offset < 200:
            self.offset += 10
            url = self.baseURL + str(self.offset)
            yield scrapy.Request(url, callback=self.parse)
