# -*- coding: utf-8 -*-
import scrapy


class Quotes1Spider(scrapy.Spider):
    name = 'quotes1'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/tag/humor/']

    def parse(self, response):
        # print(response)
        for quote in response.css('div.quote'):
            print(quote)
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.xpath('span/small/text()').get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

# 输出结果到json文件
# scrapy runspider quotes1 -o quotes1.json
