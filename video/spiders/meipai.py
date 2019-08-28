# -*- coding: utf-8 -*-
import scrapy
# from video.items import VideoItem
from utils.meipai_decode import *
import base64
import time

class MeipaiSpider(scrapy.Spider):
    name = 'meipai'
    allowed_domains = ['meipai.com']
    start_urls = ['https://www.meipai.com/search/mv?q=卢舍那大佛&page=1']

    def parse(self, response):
        lis = response.xpath("//ul[contains(@class,'content-l-ul')]/li")
        for li in lis :
            # item = VideoItem()
            item ={}
            datavideo = li.xpath("./div[1]/@data-video").get()
            # print(datavideo)
            item['files'] = li.xpath(".//a[contains(@class,'content-l-p')]/@title").get()
            try:
                str1, hex = getHex(datavideo)
                pre, tail = getDec(hex)
                d = substr(str1, pre)
                zz = substr(d, getPos(d, tail))
            except:
                pass
            # if len(zz) % 3 == 1:
            #     zz += '=='
            # if len(zz) % 3 == 2:
            #     zz += '='
            #
            try:
                item['file_urls'] = base64.urlsafe_b64decode(zz)
                item['file_urls'] = item['file_urls'].decode()
                item['files'] = li.xpath(".//a[contains(@class,'content-l-p')]/@title").get()
                yield item
            except :
                pass


        for i in range(2,5):
            time.sleep(1)
            next_url = "https://www.meipai.com/search/mv?q=卢舍那大佛&page={}".format(i)

            yield scrapy.Request(url=next_url,callback=self.parse)



