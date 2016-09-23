import scrapy
import datetime
from scrape.helpers.determine_employment_type import determine_employment_type
from scrape.helpers.determine_date import determine_date

from scrape.items import JobListing

class CWJobs(scrapy.Spider):
    name = "CWJobs"
    type = "job"
    version = 2
    allowed_domains = ["cwjobs.co.uk"]
    start_urls = ["http://www.cwjobs.co.uk/jobs"]

    def parse(self, response):
        for href in response.css(".job-title > a::attr('href')"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)

        next_page_url = response.css("a.next::attr('href')")
        if next_page_url:
            url = response.urljoin(next_page_url[0].extract())
            if url != response.url:
                yield scrapy.Request(url, self.parse)

    def parse_dir_contents(self, response):
        item = JobListing()
        item['title'] = response.css('[property="title"]::text').extract_first()
        if item['title'] is None:
            return
        item['url'] = response.url.split('?')[0]
        item['source'] = self.name
        item['spider_version'] = self.version
        item['updated_at'] = datetime.datetime.now()
        item['location'] = response.css('[property="address"]').extract_first()
        item['renumeration'] = response.css('[property="baseSalary"]::text').extract_first()
        item['company'] = response.css('.company > div > a::text').extract_first()
        item['company_website'] = response.css('.company > div > a::attr("href")').extract_first()
        item['employment_type'] = determine_employment_type(response.css('.job-type > div::text').extract_first())
        item['published_on'] = determine_date(response.css('.date-posted > div > span::text').extract_first())
        item['content'] = response.css('.job-description').extract_first()
        yield item