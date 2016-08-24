# -*- coding: utf-8 -*-        
import scrapy


from scrapy.shell import inspect_response
from scrapy.spiders import XMLFeedSpider
from althingi_scraper.items import PartyItem
from althingi_scraper.utils import fix_thorn


class PartySpider(XMLFeedSpider):

    def __init__(self, session_id=None, *args, **kwargs):
        super(PartySpider, self).__init__(*args, **kwargs)
        self.start_urls = [
            'http://www.althingi.is/altext/xml/thingflokkar/?lthing=%s' % session_id,        
        ]     
    name = 'party'

    allowed_domains = ['althingi.is']
    session = 145  
    """
    start_urls = [
        'http://www.althingi.is/altext/xml/thingflokkar/?lthing=%d' % session,        
        #'http://www.althingi.is/altext/xml/thingflokkar/'
    ]  
    """ 
    
    
    itertag = u'þingflokkur'
    iterator = 'iternodes'
    

    def parse_node(self, response, node):

        item = PartyItem()
        item['party_id'] = node.xpath(u'@id').extract_first()
        item['name'] = node.xpath(u'heiti/text()').extract_first().replace("\n", "")
        #self.logger.info('Hi, this is a <%s> node!: %s', self.itertag, ''.join(node.extract()))
        item['long_abbr'] = node.xpath(u'skammstafanir/löngskammstöfun/text()').extract()
        item['short_abbr'] = node.xpath(u'skammstafanir/stuttskammstöfun/text()').extract_first()
        
        
        return item