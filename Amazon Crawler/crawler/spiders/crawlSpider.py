import scrapy

class crawlSpider(scrapy.Spider):
    name='crawlSpider'
    start_urls=['https://www.amazon.in/s?k=iphone+case&rh=n%3A976419031%2Cp_36%3A1318503031&dc&qid=1630913192&rnid=1318502031&ref=sr_nr_p_36_1']
    
    def parse(self, response):
        product_Name = response.css('span.a-size-base-plus.a-color-base.a-text-normal::text').extract()
        product_Rating = response.css('div.a-section.a-spacing-none.a-spacing-top-micro > div.a-row.a-size-small > span::attr(aria-label)').extract()
        product_Price = response.css('span.a-text-price > span.a-offscreen::text').get().replace('₹','')
        product_DiscPrice = response.css('span.a-price-whole::text').extract()
        product_Link = 'amazon.in'+response.css('a.a-link-normal.a-text-normal').attrib['href']
        data = zip(product_Name,product_Rating,product_Price,product_DiscPrice,product_Link)
        for data in response.css('div.a-section.a-spacing-none'):
            try:
                yield{
                    'Product_Name' : data.css('span.a-size-base-plus.a-color-base.a-text-normal::text').get(),
                    'Product_Rating' : data.css('div.a-section.a-spacing-none.a-spacing-top-micro > div.a-row.a-size-small > span::attr(aria-label)').get(),
                    'Product_Original_Price' : data.css('span.a-text-price > span.a-offscreen::text').get(),
                    'Product_Discounted_Price' : data.css('span.a-price-whole::text').get(),
                    'Product_Link' : 'amazon.in'+data.css('a.a-link-normal.a-text-normal').attrib['href'],
                }
            except:
            	yield{
                    'Product_Name' : product_Name,
                    'Product_Rating' : product_Rating,
                    'Product_Original_Price' : product_Price,
                    'Product_Discounted_Price' : product_DiscPrice,
                    'Product_Link' : product_Link,
                }