# -*- coding: utf-8 -*-
import scrapy
from SF.items import SfItem


class SfSpider(scrapy.Spider):
    name = 'sf'
    allowed_domains = ['https://segmentfault.com']
    start_urls = ['https://segmentfault.com/']

    def parse(self, response):
        # 标题列表
        node_list = response.xpath('//h4[@class="news__item-title mt0"]')

        for node in node_list:
            item = SfItem()
            item['title'] = node.xpath('./a/text()').extract()[0]
            yield item
