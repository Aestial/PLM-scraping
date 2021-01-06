import scrapy

class MedicinesSpider(scrapy.Spider):
    name = 'medicines'
    allowed_domains = ['www.medicamentosplm.com']
    start_urls = ['https://www.medicamentosplm.com/Home/Medicamento/']

    def parse(self, response):
        med_page_links = response.xpath('//div[@id="editable"]').css('a.product-info')
        yield from response.follow_all(med_page_links, self.parse_med)

        pagination_links = response.css('ul.pagination-pages li.page-item a')
        yield from response.follow_all(pagination_links, self.parse)      
        
        letter_links = response.css('ul.pagination li.page-item a')
        yield from response.follow_all(letter_links, self.parse) 
        
    def parse_med(self, response):        
        def extract_with_xpath(elem, query):
            return elem.xpath(query).get(default='').strip() 
        
        def clean_list(l):
            return list(filter(None, map(str.strip, l)))

        info = response.css('div.info-ipp-pricipal')
        indic = response.css('div#rubro-1')
        contra = response.css('div#rubro-3')

        yield {
            'marca': extract_with_xpath(info, './p[1]/text()'),
            'sustancias': [x.strip() for x in extract_with_xpath(info, './p[2]/text()').split(',')],
            'forma': extract_with_xpath(info, './p[3]/text()'),
            'indicaciones': clean_list(indic.xpath('./p/text()').getall()),
            'contraindicaciones': clean_list(contra.xpath('./p/text()').getall())
        }