# -*- coding: utf-8 -*-        
import scrapy


from scrapy.spiders import XMLFeedSpider

from althingi_scraper.items import CommitteeItem

class CommitteeSpider(XMLFeedSpider):
    def __init__(self, *args, **kwargs):
        super(CommitteeSpider, self).__init__(*args, **kwargs)
        self.start_urls = [
            'http://www.althingi.is/altext/xml/nefndir/'
        ] 


    name = 'committee'
    allowed_domains = ['althingi.is']
    
    itertag = u'nefnd'
    iterator = 'iternodes'
    
    def parse_node(self, response, node):
    
        #self.logger.info('Parse function called on %s', response.url)

        item = CommitteeItem()
        item['committee_id'] = int(node.xpath(u'@id').extract_first())
        item['name'] = node.xpath(u'heiti/text()').extract_first()
        item['short_abbr'] = node.xpath(u'skammstafanir/stuttskammstöfun/text()').extract_first()
        item['long_abbr'] = node.xpath(u'skammstafanir/löngskammstöfun/text()').extract_first()
        return item
