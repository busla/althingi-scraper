# -*- coding: utf-8 -*-        
import scrapy

from scrapy.spiders import XMLFeedSpider
from althingi_scraper.items import SignatureItem


class SignatureSpider(XMLFeedSpider):
    def __init__(self, petition_id=None, *args, **kwargs):
        super(SignatureSpider, self).__init__(*args, **kwargs)
        #self.url = kw.get('url')
        
        self.start_urls = [
            'http://www.althingi.is/altext/xml/atkvaedagreidslur/atkvaedagreidsla/?numer=%s' % petition_id
        ]        

    name = 'signature'
    allowed_domains = ['althingi.is']
    
    
    itertag = u'þingmaður'
    iterator = 'iternodes'
    
        
    def parse_node(self, response, node):

        item = SignatureItem()
        item['member_id'] = node.xpath(u'@id').extract_first()
        item['signature'] = node.xpath(u'atkvæði/text()').extract_first()
        
        
        return item
