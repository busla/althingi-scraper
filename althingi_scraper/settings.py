# -*- coding: utf-8 -*-

# Scrapy settings for althingi_scraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'althingi_scraper'

SPIDER_MODULES = ['althingi_scraper.spiders']
NEWSPIDER_MODULE = 'althingi_scraper.spiders'


ITEM_PIPELINES = {
    'althingi_scraper.pipelines.DropIfEmptyFieldPipeline': 100,
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'althingi_scraper (+http://www.yourdomain.com)'
