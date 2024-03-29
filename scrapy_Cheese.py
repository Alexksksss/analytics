from urllib import response
import scrapy
import time


#scrapy runspider "datadiving_proj/datadiving_proj/spiders/testSpider.py" -o "cheese.csv"


class testSpider(scrapy.Spider):
    name = "testSpider"
    start_urls = ["https://pro-syr.ru/zakvaski-dlya-syra/mezofilnye/"]

    def parse(self, response):
        links = response.css("div.nameproduct a::attr(href)")
        for link in links:
            time.sleep(1)
            yield response.follow(link, self.parse_cheese)

        link = response.css("ul.pagination a::attr(href)").get()
        yield response.follow(link, self.parse)

    def parse_cheese(self, response):
        price = response.css("span.autocalc-product-price::text").get().split(' ')
        if len(price) > 2:
            price_f = int(price[0])*1000 + int(price[1])
        else:
            price_f = price[0]
        yield {
            "name": response.css("div.col-md-9 h1::text").get(),
            "price": price_f,
            "availability": response.css("div.product-description b::text").get()
        }

        #response.css("div.col-md-9 h1::text").get() --name
        #response.css("span.autocalc-product-price::text").get() --price
        #response.css("div.product-description b::text").get() --наличие