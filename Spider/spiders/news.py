# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['tech.huanqiu.com']
    start_urls = ['http://tech.huanqiu.com/internet/?agt=267']

    def parse(self, response):
        link = LinkExtractor(restrict_xpaths='//*[@id="pages"]/a')
        links = link.extract_links(response)
        if links:
            for link_one in links:
                print (link_one.url)
