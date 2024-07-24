# to run scrapy runspider spider.py -o ranveer_brar_urls.json

import scrapy

from scrapy.spiders import CrawlSpider
from scrapy import Request
from w3lib.http import basic_auth_header
from scrapy.crawler import CrawlerProcess
from links import Links
from config import *
from helper_func import *

class MySpider(CrawlSpider):
    #name of crawler
    name = SPIDER_NAME

    #only scrape on pages within the example.co.uk domain
    allowed_domains = domains

    #start scraping on the site homepage once credentials have been authenticated
    start_urls=base_url

    #rules for recursively scraping the URLS found
    rules=rules
    
    seen_links=set()

    #method to identify hyperlinks by xpath and extract hyperlinks as scrapy items
    
    def parse_link(self, response):
        for element in response.xpath('//a'):
            oglink = element.xpath('@href').get()
            #need to add on prefix as some hrefs are not full https URLs and thus cannot be followed for scraping
            print(oglink)
            if "http" not in str(oglink):
                full_url = complete_url + oglink
            else:
                full_url = oglink
            
            
            if any(substring in full_url for substring in urls_to_be_removed):
                continue

            if full_url not in self.seen_links and complete_url in full_url:
                self.seen_links.add(full_url)
                item = Links()
                item['link'] = full_url
                yield item



    