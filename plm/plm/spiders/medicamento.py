import scrapy

class MedicamentoSpider(scrapy.Spider):
    name = 'medicamento'
    allowed_domains = ['www.medicamentosplm.com']
    start_urls = ['https://www.medicamentosplm.com/Home/Medicamento/']

    def parse(self, response):
        def extract_with_css(elem, query):
            return elem.css(query).get(default='').strip()

        for med in response.xpath('//div[@id="editable"]'):
            yield {
                'medicamento': extract_with_css(med, 'a.product-info::text'),
                'sustancia': extract_with_css(med, 'div#prescription-substance-1 a::text'),
            }