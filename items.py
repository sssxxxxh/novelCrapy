# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelcrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    novel_topic = scrapy.Field()
    novel_name = scrapy.Field()
    novel_chapter = scrapy.Field()
    novel_content = scrapy.Field()