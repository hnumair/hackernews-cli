from scrapy import Spider

class HNSpider(Spider):
    name = "hackernews"
    start_urls = ['https://news.ycombinator.com',]


    def parse(self, response):

       posts = response.css("a.storylink")

       for post in posts:
            yield{
                'title': post.css("::text").get(),
                'link': post.css("a::attr(href)").get(),
            }
