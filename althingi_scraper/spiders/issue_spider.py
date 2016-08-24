# -*- coding: utf-8 -*-        
import scrapy
import re


from scrapy.spiders import XMLFeedSpider
from althingi_scraper.items import IssueItem

class IssueSpider(XMLFeedSpider):
    def __init__(self, session_id=None, *args, **kwargs):
        super(IssueSpider, self).__init__(*args, **kwargs)
        #self.url = kw.get('url')
        
        self.start_urls = [
            'http://www.althingi.is/altext/xml/thingmalalisti/?lthing=%s' % session_id
        ]    

    name = 'issue'
    allowed_domains = ['http://www.althingi.is']
    
    itertag = u'mál'
    iterator = 'xml'
    
    """
    def adapt_response(self, response): 
        
        body = response.body \
            .replace('málsnúmer', 'malsnumer') \
            .replace('málsheiti', 'malsheiti') \
            .replace('málstegund', 'malstegund') \
            .replace('málaskrá', 'malaskra') \
            .replace('þingnúmer', 'thingnumer') \
            .replace('mál', 'mal')
        
        #print 'MY ENCODING: %s' % response.body_as_unicode().encode(response.encoding) == response.body

        #body = re.sub('<malsheiti>.*?</malsheiti>', '<malsheiti>THIS IS A NAME</malsheiti>', body)
        
        #body = response.body.decode('latin-1').encode('utf-8')
        #print body
        return response.replace(body=body)
        #return response.body_as_unicode()
    """
    def parse_node(self, response, node):
        
        #print node.xpath(u'xml').extract()
        item = IssueItem()
        item['url'] = node.xpath(u'xml/text()').extract_first()
        item['name'] = node.xpath(u'málsheiti/text()').extract_first()
        item['issue_id'] = node.xpath(u'@málsnúmer').extract_first()
        item['session'] = node.xpath(u'@þingnúmer').extract_first()
        
        
        
        return item
