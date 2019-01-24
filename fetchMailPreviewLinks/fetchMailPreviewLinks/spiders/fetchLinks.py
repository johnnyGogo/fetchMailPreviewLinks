# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from urllib.parse import urlparse
from ..items import FetchmailpreviewlinksItem

class FetchlinksSpider(scrapy.Spider):
    name = 'fetchLinks'

    start_urls = ['http://127.0.0.1:3000/rails/mailers/notification']

    def parse(self, response):
        self.logger.info('start response')


        links = LinkExtractor(canonicalize=True,
                              unique=True,
                              deny='https://www.facebook.com/|https://twitter.com/Termly_io|https://plus.google.com/u/|https://www.linkedin.com/company/termly/|https://www.google.com.tw/maps/place|.+rails/mailers/.+/termly.io|\?part=text%2Fhtml|rails/mailers/notification/%rawUnsubscribe%'
                              ).extract_links(response)

        # depth 1 is mail's content
        if response.meta['depth'] == 1:
            for link in links:
                yield FetchmailpreviewlinksItem(
                    mail_name=urlparse(response.url).path.split('/')[-1],
                    link_text=link.text,
                    link=link.url
                )

        for link in links:
            yield scrapy.Request(link.url + '?part=text%2Fhtml', callback=self.parse)

