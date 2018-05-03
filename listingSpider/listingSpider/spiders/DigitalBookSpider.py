# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class DigitalbookspiderSpider(CrawlSpider):
    name = "DigitalBookSpider"
    allowed_domains = ["kompass.com"]

    start_urls = [
        'https://fr.kompass.com/searchCompanies?acClassif=&localizationCode=FR_72_33_33063&localizationLabel=Bordeaux&localizationType=town&text=restaurant&searchType=SUPPLIER'
    ]

    def start_requests(self):
        headers= {'User-Agent': 'Mozilla/5.0 (Linux; <Android Version>;) AppleWebKit/<WebKit Rev> (KHTML, like Gecko) Chrome/<Chrome Rev> Mobile Safari/<WebKit Rev>'}
        for url in self.start_urls:
            yield Request(url, headers=headers)

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pn')),
             callback="parse_item",
             follow=True),)
 
    def parse_item(self, response):
        print('Processing..' + response.url)
        # print(response.text)

    def parse(self, response):
        pass