# -*- coding: utf-8 -*-        
import scrapy

from scrapy.spiders import XMLFeedSpider
from althingi_scraper.items import SessionItem

class SessionSpider(XMLFeedSpider):
    name = 'session'

    allowed_domains = ['http://www.althingi.is']
    start_urls = [
        'http://www.althingi.is/altext/xml/loggjafarthing/'
    ]        

    itertag = u'þing'
    iterator = 'iternodes'
    
        
    def parse_node(self, response, node):

        
        item = SessionItem()
        item['session_id'] = node.xpath(u'@númer').extract_first()
        item['date_from'] = node.xpath(u'þingsetning/text()').extract_first()
        date_to = node.xpath(u'þinglok/text()')
        
        # If empty add 'null'
        if not date_to:
            item['date_to'] = ''
        else:
            item['date_to'] = date_to.extract_first()
        
        return item
