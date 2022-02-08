import scrapy

class NewSpider(scrapy.Spider)
    name = "new spider"
    start_urls = ["https://brickset.com/sets/year-2020"]

    def parse(self, response):
        xpath_selector = "//img"
        for x in response.xpath(xpath_selector):
            newsel