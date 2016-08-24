# -*- coding: utf-8 -*-        
import scrapy

from scrapy.shell import inspect_response
from scrapy.spiders import XMLFeedSpider
from scrapy.linkextractors import LinkExtractor
from althingi_scraper.items import MemberItem, SeatItem
from althingi_scraper.utils import fix_thorn
from scrapy.http import Request

class MemberSpider(XMLFeedSpider):
    def __init__(self, session_id=None, *args, **kwargs):
        super(MemberSpider, self).__init__(*args, **kwargs)
        self.start_urls = [
            'http://www.althingi.is/altext/xml/thingmenn/?lthing=%s' % session_id
        ] 

    name = 'member'
    allowed_domains = ['althingi.is']


    """
    session = 145
    start_urls = [
        'http://www.althingi.is/altext/xml/thingmenn/?lthing=%d' % session
    ]   
    """
    
    itertag = u'þingmaður'
    iterator = 'iternodes'
    
    def parse_node(self, response, node):
    
        #self.logger.info('Parse function called on %s', response.url)

        item = MemberItem()
        item['member_id'] = node.xpath(u'@id').extract_first()
        item['name'] = node.xpath(u'nafn/text()').extract_first()
        item['dob'] = node.xpath(u'fæðingardagur/text()').extract_first()
        item['abbr'] = node.xpath(u'skammstöfun/text()').extract_first()    
        item['seat_xml_url'] = node.xpath(u'xml/þingseta/text()').extract_first()
        request = Request(url=item['seat_xml_url'], callback=self.parse_seat)
        request.meta['item'] = item
        yield request
        

    def parse_seat(self, response):
        item = response.meta['item']        
        result = []
        
        #self.logger.info('Member seat url: %s', response.url)
        
        for seat in response.xpath(u'//þingseta'):
            seats = {}
            #self.logger.info('Seat: %s', seat)
            seats['session_id'] = seat.xpath(u'þing/text()').extract_first()
            seats['role'] = seat.xpath(u'tegund/text()').extract_first()        
            seats['party_id'] = seat.xpath(u'þingflokkur/@id').extract_first()        
            seats['region_name'] = seat.xpath(u'kjördæmi/text()').extract_first()        
            seats['date_from'] = seat.xpath(u'tímabil/inn/text()').extract_first()        
            seats['date_to'] = seat.xpath(u'tímabil/út/text()').extract_first()                                
            
            if seats['party_id']:
                result.append(seats)
        item['seats'] = result
        return item
