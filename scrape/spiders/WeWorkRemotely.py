import scrapy
import datetime

from scrape.items import JobListing
from scrape.helpers.determine_date import determine_date

class WeWorkRemotelySpider(scrapy.Spider):
    name = "WeWorkRemotely"
    type = "job"
    version = 1
    allowed_domains = ["weworkremotely.com"]
    start_urls = ["https://weworkremotely.com/categories/2-programming/jobs"]

    def parse(self, response):
        for href in response.css(".jobs a:not(.view-all)::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        item = JobListing()
        item['title'] = response.css('.listing-header-container > h1::text').extract_first()
        if item['title'] is None:
            return
        item['url'] = response.url
        item['source'] = self.name
        item['spider_version'] = self.version
        item['updated_at'] = datetime.datetime.now()
        item['published_on'] = determine_date(response.css('.listing-header-container > h3::text').extract_first())
        item['content'] = response.css('.listing-container').extract_first()
        item['company'] = response.css('.company::text').extract_first()
        item['company_website'] = response.css('.listing-header-container > h2 > a::attr("href")').extract_first()
        item['image_url'] = response.css('.listing-logo > img::attr("src")').extract_first()
        item['location'] = response.css('.location::text').extract_first()
        yield item