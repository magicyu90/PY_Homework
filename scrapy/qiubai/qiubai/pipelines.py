# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QiubaiPipeline(object):
    def process_item(self, item, spider):
        # return item
        with open('/Users/hugo/dev/qiubai.txt', 'a+') as f:
            f.write('作者：{} \n{}\n点赞：{}\t评论数：{}\n\n'.format(
                item['author'], item["body"], item['funNum'], item["comNum"]))
