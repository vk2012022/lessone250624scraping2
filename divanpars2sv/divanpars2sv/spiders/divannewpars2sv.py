import scrapy


class Divannewpars2svSpider(scrapy.Spider):
    name = "divannewpars2sv"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        svetds = response.css('div.LlPhw')
        for svetd in svetds:
            yield {
                'name' :  svetd.css('div.lsooF span::text').get(),
                'price' :  svetd.css('div.pY3d2 span::text').get(),
                'url' :  svetd.css('a').attrib['href']
            }
