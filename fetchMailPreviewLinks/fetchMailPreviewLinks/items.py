# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FetchmailpreviewlinksItem(scrapy.Item):
    mail_name = scrapy.Field()
    link_text = scrapy.Field()
    link = scrapy.Field()
