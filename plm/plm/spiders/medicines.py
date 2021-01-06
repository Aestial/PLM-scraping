import scrapy


class MedicinesSpider(scrapy.Spider):
    name = 'medicines'
    allowed_domains = ['www.medicamentosplm.com/']
    start_urls = ['https://www.medicamentosplm.com/Home/Medicamento//']

    def parse(self, response):
        meds = response.xpath('//div[@id="editable"]').css('a.product-info::attr(href)')
        # yield response.follow(med, callback=self.parse_med)
        for med in meds:
            yield {
                "med": med.get()
            }
        
    def parse_med(self, response):
        yield {
            'marca': response.css('div.info-ipp-pricipal').xpath('./p[1]/text()').get()
        }