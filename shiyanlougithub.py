#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import scrapy

class ShiyanlouGithubSpider(scrapy.Spider):
    name = 'shiyanlougithub'
    start_urls = [
        'http://github.com/shiyanlou?tab=repositores',
        'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK0MjAxNy0wNi0wNlQyMjoyMToxNlrOBZKV2w%3D%3D&tab=repositories',
        'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK0MjAxNS0wMS0yNlQwODoxNzo1M1rOAcd_9A%3D%3D&tab=repositories',
        'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK0MjAxNC0xMS0yNFQwNzowMDoxN1rOAZz3Yw%3D%3D&tab=repositories'
    ]

    def parse(self,response):
        for i in response.css('li.col-12'):
            yield {
                'name': i.xpath('.//a/text()').extract_first().strip(),
                'update_time': i.xpath('.//relative-time/@datetime').extract_first()
            }


