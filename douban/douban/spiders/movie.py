# -*- coding: utf-8 -*-
import scrapy
from items import DoubanItem
from scrapy_redis.spiders import RedisSpider


class MovieSpider(RedisSpider):
    name = 'movie'
    redis_key = 'movie:start_urls'
    allowed_domains = ['movie.douban.com']

    def parse(self, response):
        detail_urls = response.xpath('//div[@class="hd"]/a/@href').extract()
        print(detail_urls)
        for detail_url in detail_urls:
            yield scrapy.Request(detail_url, callback=self.detail_info)
        page = response.xpath('//span[@class="next"]/link/@href').extract_first()
        if page is not None:
            url = f'https://movie.douban.com/top250{page}'
            yield scrapy.Request(url, callback=self.parse)

    def detail_info(self, response):
        item = DoubanItem()
        name = response.xpath('//h1/span[1]/text()').extract()
        director = response.xpath('//*[contains(text(), "导演")]/following-sibling::span[1]//text()').extract()
        item['name'] = name
        item['director'] = director
        yield item

