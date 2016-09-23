import scrapy
import datetime

class Article(scrapy.Item):
    url = scrapy.Field()
    source = scrapy.Field()
    author = scrapy.Field()
    updated_at = scrapy.Field()
    published_on = scrapy.Field()
    expires_on = scrapy.Field()
    title = scrapy.Field()
    image_url = scrapy.Field()
    content = scrapy.Field()
    tags = scrapy.Field()
    view_count = scrapy.Field()
    spider_version = scrapy.Field()

class JobListing(Article):
    company = scrapy.Field()
    company_website = scrapy.Field()
    location = scrapy.Field()
    renumeration_min = scrapy.Field()
    renumeration_max = scrapy.Field()
    renumeration = scrapy.Field()
    employment_type = scrapy.Field()
