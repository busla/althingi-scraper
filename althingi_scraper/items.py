# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PartyItem(scrapy.Item):
    party_id = scrapy.Field()
    name = scrapy.Field()
    short_abbr = scrapy.Field()
    long_abbr = scrapy.Field()

class IssueItem(scrapy.Item):
    issue_id = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    session = scrapy.Field()

class PetitionItem(scrapy.Item):    
    petition_id = scrapy.Field()
    petition_url = scrapy.Field()    
    signature_xml_url = scrapy.Field()    
    session_id = scrapy.Field()
    issue_id = scrapy.Field()
    issue_name = scrapy.Field()
    issue_url = scrapy.Field()
    date_created = scrapy.Field()
    signatures = scrapy.Field()
    #member_id = scrapy.Field()
    #signature = scrapy.Field()
    

class MemberItem(scrapy.Item):    
    member_id = scrapy.Field()
    name = scrapy.Field()    
    dob = scrapy.Field()
    abbr = scrapy.Field()
    seats = scrapy.Field()
    seat_xml_url = scrapy.Field()

class SeatItem(scrapy.Item):
    member_id = scrapy.Field()    
    session_id = scrapy.Field()
    role = scrapy.Field()    
    party_id = scrapy.Field()
    region_id = scrapy.Field()
    region_name = scrapy.Field()
    seat_number = scrapy.Field()
    date_from = scrapy.Field()
    date_to = scrapy.Field()

class SignatureItem(scrapy.Item):    
    session_id = scrapy.Field()
    issue_id = scrapy.Field()    
    member_id = scrapy.Field()
    signature_id = scrapy.Field()
    signature = scrapy.Field()
    date_created = scrapy.Field()

class SessionItem(scrapy.Item):    
    session_id = scrapy.Field()
    date_from = scrapy.Field()    
    date_to = scrapy.Field() 

class CommitteeItem(scrapy.Item):
    committee_id = scrapy.Field()
    name = scrapy.Field()
    short_abbr = scrapy.Field()
    long_abbr = scrapy.Field()

class CommitteeMeetingItem(scrapy.Item):
    meeting_id = scrapy.Field()
    session = scrapy.Field()
    committee = scrapy.Field()
    start_time = scrapy.Field()    
    end_time = scrapy.Field()
    report_url = scrapy.Field()
    attended = scrapy.Field()    