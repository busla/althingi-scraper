# -*- coding: utf-8 -*-        
import scrapy

from scrapy.spiders import XMLFeedSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request

from althingi_scraper.items import CommitteeMeetingItem


class CommitteeMeetingSpider(XMLFeedSpider):
    
    def __init__(self, session_id=None, *args, **kwargs):
        super(CommitteeMeetingSpider, self).__init__(*args, **kwargs)
        self.start_urls = [
            'http://www.althingi.is/altext/xml/nefndarfundir/?lthing=%s' % session_id
        ]     

    name = 'committee_meeting'
    allowed_domains = ['althingi.is']   
    
    
    itertag = u'nefndarfundur'
    iterator = 'iternodes'
       

    def parse_node(self, response, node):

        item = CommitteeMeetingItem()
        item['meeting_id'] = node.xpath(u'@númer').extract_first()
        item['session'] = node.xpath(u'@þingnúmer').extract_first()
        item['committee'] = node.xpath(u'nefnd/@id').extract_first()
        item['start_time'] = node.xpath(u'fundursettur/text()').extract_first()
        item['end_time'] = node.xpath(u'fuslit/text()').extract_first()
        item['report_url'] = node.xpath(u'nánar/fundargerð/xml/text()').extract_first()
        
        # Bíð með að sækja fundargerðina þar til síðar.
        """
        if item['report_url']:
            request = Request(url=item['report_url'], callback=self.parse_report)
            request.meta['item'] = item
            yield request
        """

        # Fjarlægja ef kallað er í parse_report()
        return item
       

            
    """
    Sækir fundargerðina sem inniheldur einnig mætingarlista
    """
    def parse_report(self, response):
        item = response.meta['item']                
        item['attended'] = response.xpath(u'//nefndarfundur/fundargerð/texti/text()').extract_first()
        yield item
        
        #print "####################### "+str(response.xpath(u'//þingmaður').extract())+" ############################"
        

    