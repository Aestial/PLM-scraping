import scrapy


class IngredientsSpider(scrapy.Spider):
    name = 'ingredients'
    start_urls = ['https://www.medicamentosplm.com/Home/Sustancia/']

    def parse(self, response):
        ingredient_page_links = response.xpath('//div[@id="editable"]').css('a')
        yield from response.follow_all(ingredient_page_links, self.parse_ingredient)
        
        pagination_links = response.css('ul.pagination-pages li.page-item a')
        yield from response.follow_all(pagination_links, self.parse)      
        
        letter_links = response.css('ul.pagination li.page-item a')
        yield from response.follow_all(letter_links, self.parse)

    def parse_ingredient(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()
        yield {
            'ingredient': extract_with_css('ol.breadcrumb li.active::text'),
        }