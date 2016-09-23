import scrapy
import datetime

from scrape.items import JobListing
from scrape.helpers.determine_employment_type import determine_employment_type
from scrape.helpers.determine_date import determine_date
from scrape.helpers.determine_integer import determine_integer

class WorkInStartups(scrapy.Spider):
    name = "WorkInStartups"
    type = "job"
    version = 2
    allowed_domains = ["workinstartups.com"]
    start_urls = ["http://workinstartups.com/job-board/jobs"]

    def parse(self, response):
        for href in response.css("a.job-row-link::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)

        next_page_url = response.css("#job-listings > a:last-child::attr('href')")
        if next_page_url:
            url = response.urljoin(next_page_url[0].extract())
            if url != response.url:
                yield scrapy.Request(url, self.parse)

    def parse_dir_contents(self, response):
        item = JobListing()
        item['title'] = response.css('#job-title::text').extract_first()
        if item['title'] is None:
            return
        item['url'] = response.url
        item['source'] = self.name
        item['spider_version'] = self.version
        item['updated_at'] = datetime.datetime.now()
        item['published_on'] = determine_date(response.css('#number-views > strong:nth-of-type(1)::text').extract_first())
        item['expires_on'] = determine_date(response.css('#number-views > strong:nth-of-type(2)::text').extract_first())
        item['view_count'] = determine_integer(response.css('#number-views > strong:nth-of-type(3)::text').extract_first())
        item['content'] = response.css('#job-description').extract_first()
        item['company'] = response.css('#job-subtitle > a > strong::text').extract_first()
        item['company_website'] = response.css('#job-subtitle > a::attr("href")').extract_first()
        item['location'] = response.css('#job-subtitle > strong:last-child::text').extract_first()
        item['renumeration'] = response.css('.job-subtitle-salary::text').extract_first()
        item['employment_type'] = determine_employment_type(response.css('#job-title::attr("class")').extract_first())
        yield item