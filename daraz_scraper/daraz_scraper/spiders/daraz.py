import scrapy

from scrapy_playwright.page import PageMethod



scrolling_script = """
// Scroll down the page 8 times
const scrolls = 8;
let scrollCount = 0;

// Scroll down and then wait for 0.5s
const scrollInterval = setInterval(() => {
  window.scrollTo(0, document.body.scrollHeight);
  scrollCount++;

  if (scrollCount === scrolls) {
    clearInterval(scrollInterval);
  }
}, 500);

    """ # instruct a browser to perform infinite scrolling in JavaScript by automatically scrolling down the page eight times at an interval of 0.5 seconds in the browser



class DarazSpider(scrapy.Spider):
    name = "daraz"
    allowed_domains = ["www.daraz.com.np"]
    # start_urls = ["https://www.daraz.com.np/ankle-boots/"]



    def start_requests(self):
        url = "https://www.daraz.com.np/ankle-boots/" 
        yield scrapy.Request(url,
                             meta={"playwright":True, #it tells Scrapy to route the request through scrapy-playwright
                                   "playwright-page-method":[
                                       PageMethod("evaluate",scrolling_script),
                                       PageMethod("wait_for_timeout", 7000),
                                       PageMethod("wait_for_selector", ".gridItem--Yd0sa")

                                   ],
                                   }) 

    def parse(self, response):
        for product in response.css(".gridItem--Yd0sa"):
            url = product.css("a::attr(href)").get().split("?")[0]
            image = product.css(".image-wrapper--ydch1 img::attr(src)").get()
            name = product.css(".title-wrapper--IaQ0m::text").get()
            rating = product.css(".rating--pwPrV::text").get()
            price = product.css(".currency--GVKjl::text").get()
            sold = product.css("div.split--cTjJp + div::text").get()
            
        
         # add the data to the list of scraped items
            yield {
                'url': url,
                'image': image,
                'name': name,
                'rating': rating,
                'price': price,
                'sold': sold
            }







        
