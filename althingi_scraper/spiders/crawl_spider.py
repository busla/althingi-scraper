# -*- coding: utf-8 -*-        
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from althingi_scraper.items import IssueItem

class TestSpider(CrawlSpider):
    def __init__(self, session_id=None, *args, **kwargs):
        super(TestSpider, self).__init__(*args, **kwargs)
        #self.url = kw.get('url')
        
        self.start_urls = [
            'http://www.althingi.is/altext/xml/thingmalalisti/?lthing=%s' % session_id
        ]    

    name = 'test'
    allowed_domains = ['http://www.althingi.is']



    def parse_item(self, node):
        
        #print node.xpath(u'xml').extract()
        item = IssueItem()
        
        item['issue_id'] = node.xpath('//malsheiti/text()').extract_first()
        #item['name'] = node.xpath(u'//mál/málsheiti/text()').extract_first()
        #item['session'] = node.xpath(u'//mál/@þingnúmer').extract_first()
        #item['url'] = node.xpath(u'//mál/xml/text()').extract_first()

        print(item)
        return item
