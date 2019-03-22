import json
import re

import scrapy
from scrapy import Request

from app.items import AppItem


class app_spider(scrapy.Spider):
    name="app"
    alowed_domains=['http://360.cn']

    def start_requests(self):
        url_pr='http://comment.mobilem.360.cn/comment/getComments?callback=jQuery1720519799417783672_1553133732547&baike=%E5%BE%AE%E4%BF%A1android&c=message&a=getmessage&start='
        n=-10
        while n<10000:
            n=n+10
            url=url_pr+str(n)+'&count=10'
            yield Request(url)

    def parse(self,response):
        p=re.compile(r'{.*?}')
        l=p.findall(response.text)
        for com in l:
            app_com=AppItem()
            p_com=re.compile(r'\"content.{3}(.+?)\"\,')
            if p_com.search(com) is None:
                break
            r=p_com.search(com).group(1)
            app_com['com_content']=eval("u"+"\'"+r+"\'")
            p_tim=re.compile(r'\"create_time.{3}(.+?)\"\,')
            app_com['com_time']=p_tim.search(com).group(1)
            p_ver=re.compile(r'\"version_name.{3}(.*?)\"')
            app_com['com_ver']=p_ver.search(com).group(1)
            p_sco=re.compile(r'\"score\"\:(\d)|\"score\"\:\"(\d)\"')
            if p_sco.search(com).group(1) is not None:
                app_com['com_score']=p_sco.search(com).group(1)
            else:
                app_com['com_score']=p_sco.search(com).group(2)
            p_wei=re.compile(r'\"weight.{3}(.+?)\"\,')
            app_com['com_weight']=p_wei.search(com).group(1)
            p_lik=re.compile(r'\"likes.{3}(.+?)\"\,')
            app_com['com_likes']=p_lik.search(com).group(1)
            yield app_com
