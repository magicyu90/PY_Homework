# -*- coding: utf-8 -*-
import scrapy
from HugoBlog.items import HugoblogItem


class BlogspiderSpider(scrapy.Spider):
    name = 'BlogSpider'
    allowed_domains = ['blog.magicyu.com']
    baseUrl = 'http://blog.magicyu.com/'
    start_urls = [baseUrl]

    def parse(self, response):
        articiles = response.xpath('//div[@class="post-block"]')
        for article in articiles:
            item = HugoblogItem()
            headerInfo = article.xpath('./header[@class="post-header"]')
            item['title'] = headerInfo.xpath(
                './h1[1]/a[@class="post-title-link"]/text()').extract()[0]
            item['createDate'] = headerInfo.xpath(
                './div[@class="post-meta"]/span[@class="post-time"]/time[1]/text()').extract()[0].strip()

            detailBtn = article.xpath(
                './/div[@class="post-body"]/div[1]/a[1]/@href').extract()[0]
            detailUrl = self.baseUrl + detailBtn
            yield scrapy.Request(detailUrl, callback=self.get_content, meta={'blog_item': item})

        next_page = response.xpath('//a[@class="extend next"]')
        if next_page:
            next_url = self.baseUrl + next_page.xpath('./@href').extract()[0]
            yield scrapy.Request(next_url, callback=self.parse)

    def get_content(self, response):
        """获取内容"""
        item = response.meta.get('blog_item')
        item['content'] = response.xpath(
            '//div[@class="post-body"]/p[1]/text()').extract()[0]
        yield item
