# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.files import FilesPipeline
# from scrapy.pipelines.media import
import os
from urllib.request import urlretrieve
import time
import random
import re

class VideoDownloadPipeline(object):
    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '卢舍那大佛')
        if not os.path.exists(self.path):
            # print('该路径不存在')
            os.mkdir(self.path)
        # else:
        #     print('该路径存在')

    def process_item(self, item, spider):
        title = item['files']
        urls = item['file_urls']
        # title_path = os.path.join(self.path, title)
        if title is not None:
            title=re.sub(r'[\r\n\s/\\\\ \\ ]',"",title)
        if title is None or title=='' or title==' ':
            title=str(random.choice(range(0,9999999999)))

        print('正在下载%s'%title)
        # if not os.path.exists(title_path):
        #     os.mkdir(title_path)
        try:
            urlretrieve(urls, os.path.join(self.path,title+'.mp4' ))
            print('下载完成%s'%title)
            time.sleep(0.5)
            return item
        except:
            pass
class VideoPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        request_objs = super(VideoPipeline, self).get_media_requests(item, info)
        for request_obj in request_objs:
            request_obj.item=item
        return  request_objs

    def file_path(self, request, response=None, info=None):
        pass