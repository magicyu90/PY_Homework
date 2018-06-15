# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SfItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()


class TencentItem(scrapy.Item):
     # 职位名
    positionName = scrapy.Field()
    # 职位链接
    positionLink = scrapy.Field()
    # 职位类型
    positionType = scrapy.Field()
    # 职位人数
    positionNumber = scrapy.Field()
    # 工作地点
    workLocation = scrapy.Field()
    # 发布时点
    publishTime = scrapy.Field()
