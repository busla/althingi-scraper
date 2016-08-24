# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exceptions import DropItem

class DropIfEmptyFieldPipeline(object):

    def process_item(self, item, spider):
        if spider.name == 'member':
        # to test if only "job_id" is empty,
        # change to:
        # if not(item["job_id"]):
            if not(all(item.values())):
                raise DropItem()
            else:
                return item
        return item