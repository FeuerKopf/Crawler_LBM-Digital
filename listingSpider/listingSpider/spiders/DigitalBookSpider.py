import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class DigitalBookSpider(CrawlSpider):
    name = "DigitalBookSpider"
    allowed_domains = ['www.pagesjaunes.fr', 'https://www.pagesjaunes.fr', 'http://www.pagesjaunes.fr']
    start_urls = [
        'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=coiffeur&ou=33000&proximite=0',
        'http://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=coiffeur&ou=33000&proximite=0'
    ]
    rules = (
    Rule(LinkExtractor(), callback='parse_page', follow=True),
)

    def parse(self, response):
        for h3 in response.xpath('//h3').extract():
            yield {"title": h3}

        for url in response.xpath('//a/@href').extract():
            yield scrapy.Request(url, callback=self.parse)