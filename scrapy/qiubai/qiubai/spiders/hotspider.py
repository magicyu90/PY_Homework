# -*- coding: utf-8 -*-
import scrapy
from qiubai.items import QiubaiItem


class HotspiderSpider(scrapy.Spider):
    name = 'hotspider'
    allowed_domains = ['qiushibaike.com']
    start_urls = []

    for i in range(1, 3):
        start_urls.append('http://www.qiushibaike.com/8hr/page/'+str(i)+'/')

    def parse(self, response):
        item = QiubaiItem()
        articles = response.xpath('//div[@id="content-left"]/div')

        for article in articles:
            item['author'] = article.xpath(
                './div[@class="author"]//h2/text()').extract()[0]
            item['body'] = article.xpath(
                '//a[@class="contentHerf"]/div/span[1]/text()').extract()[0]
            item['funNum'] = article.xpath(
                '//span[@class="stats-vote"]/i/text()').extract()[0]
            item['comNum'] = article.xpath(
                '//span[@class="stats-comments"]/a/i/text()').extract()[0]
            yield item
