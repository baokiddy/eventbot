import scrapy
from scrapy.spiders import Spider
# from scrapy_splash import SplashRequest

from ..items import EventbotItem

class MySpider(Spider):
    name = 'eventbot'
    start_urls = ['https://www.eventbrite.com/d/netherlands--amsterdam/conferences/?end_date=2020-02-29&page=1&start_date=2020-01-01',] 

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield SplashRequest(url=url, callback=self.parse, args={'wait': 3})


    def parse(self, response):
        item = EventbotItem()
        
        for event in response.css("div.eds-media-card-content__content__principal"):
            item['event_link'] = event.css("div.eds-media-card-content__primary-content > a.eds-media-card-content__action-link::attr(href)").extract_first()
            item['event_name'] = event.css("div.eds-is-hidden-accessible::text").extract_first()
            item['event_date'] = event.css("div.eds-media-card-content__sub-content > div.eds-text-bs--fixed::text").extract_first()
            item['event_location'] = event.css("div.eds-text-bs--fixed > div.card-text--truncated__one::text").extract_first()
            if ("div.eds-media-card-content__sub-content-cropped > div.eds-text-bs--fixed::text") != 'Free':
                item['event_price'] = event.css("div.eds-media-card-content__sub-content-cropped > div.eds-text-bs--fixed::text").extract_first()
            yield item
        
        next_page_url = response.css("div.eds-l-pad-left-4 > a.eds-btn--link::attr(href)").extract_first()
        if next_page_url is not None:
            next_page = 'https://www.eventbrite.com' + next_page_url
            yield scrapy.Request(url=next_page)