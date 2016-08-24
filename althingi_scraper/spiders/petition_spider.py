# -*- coding: utf-8 -*-        
import scrapy

from scrapy.spiders import XMLFeedSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request

from althingi_scraper.items import PetitionItem, SignatureItem


class PetitionSpider(XMLFeedSpider):
    
    def __init__(self, session_id=None, *args, **kwargs):
        super(PetitionSpider, self).__init__(*args, **kwargs)
        self.start_urls = [
            'http://www.althingi.is/altext/xml/atkvaedagreidslur/?lthing=%s' % session_id
        ]     

    name = 'petition'
    allowed_domains = ['althingi.is']   
    
    
    itertag = u'atkvæðagreiðsla'
    iterator = 'iternodes'
       

    def parse_node(self, response, node):
        if node.xpath(u'nánar/xml'):
            item = PetitionItem()
            item['issue_id'] = node.xpath(u'@málsnúmer').extract_first()
            item['issue_name'] = node.xpath(u'mál/málsheiti/text()').extract_first()
            item['issue_url'] = node.xpath(u'mál/xml/text()').extract_first()
            item['petition_url'] = node.xpath(u'nánar/html/text()').extract_first()
            item['signature_xml_url'] = node.xpath(u'nánar/xml/text()').extract_first()
            item['petition_id'] = node.xpath(u'@atkvæðagreiðslunúmer').extract_first()
            item['session_id'] = node.xpath(u'@þingnúmer').extract_first()
            item['date_created'] = node.xpath(u'tími/text()').extract_first()
            request = Request(url=item['signature_xml_url'], callback=self.parse_signature)
            request.meta['item'] = item
            yield request


            
    
    def parse_signature(self, response):
        item = response.meta['item']        
        signatures = []
        #print response.xpath(u'//þingmaður').extract():
        for signature in response.xpath(u'//þingmaður'):
        #print "####################### %s ######################" % signature
            member_id = signature.xpath(u'@id').extract_first()
            signature = signature.xpath(u'atkvæði/text()').extract_first()
            #print "####################### %s ######################" % item
            signatures.append({'member_id': member_id, 'signature': signature})
        item['signatures'] = signatures  
        return item
        
        #print "####################### "+str(response.xpath(u'//þingmaður').extract())+" ############################"
        

    