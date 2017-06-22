import re
import scrapy
from ding.mysqlpipelines.sql import Sql
from bs4 import BeautifulSoup
from scrapy.http import Request
from ding.items import DingItem
from ding.items import DcontentItem

class Myspider(scrapy.Spider):
    name = 'ddxiaoshuo'
    bash_url = 'http://www.23us.so/list/'
    bashurl ='.html'
    def start_requests(self):
        for i in range(1,10):
            url = self.bash_url+str(i)+'_1'+self.bashurl
            yield Request(url,self.parse)
    def parse(self, response):
        max_page = BeautifulSoup(response.text).find('a',class_='last').get_text()
        burl = response.url[:26]
        for i in range(1,int(max_page)+1):
            url = burl+str(i)+self.bashurl
            yield Request(url,self.getname)
    def getname(self,response):
        trs = BeautifulSoup(response.text).find_all('tr',bgcolor='#FFFFFF')
        for tr in trs:
            name = tr.find('td',class_='L').find('a').get_text()
            url = tr.find('td',class_='L').find('a')['href']
            yield Request(url,self.getitems,meta={'name':name,
                                                'novelurl':url
                                                })
    def getitems(self,response):
        item = DingItem()
        items = BeautifulSoup(response.text).find('table',cellspacing='1').find_all('td')
        item['category'] = items[0].get_text().replace('\xa0','')
        item['author'] = items[1].get_text().replace('\xa0','')
        # item['nameid'] = response.url[28:32]
        # http://www.23us.so/xiaoshuo/6158.html>
        # item['nameid'] = re.search(r'xiaoshuo/(.*).html',str(response.url)).group(0)
        a = re.search(r'xiaoshuo/(.*).html', str(response.url)).group(1)
        item['nameid'] = a
        item['novelnumber'] = items[4].get_text().replace('\xa0','')
        item['name'] = response.meta['name'].replace('\xa0','')
        item['novelurl'] = response.meta['novelurl']
        bash_url = BeautifulSoup(response.text,'lxml').find('a',class_='read')['href']
        yield item
        yield Request(bash_url,self.getchapter,meta={'nameid':a})
    def getchapter(self,response):
        tds = BeautifulSoup(response.text,'lxml').find_all('td',class_='L')
        num = 0
        for td in tds:
            num += 1
            url = td.find('a')['href']
            chaptername = td.find('a').get_text()
            rets = Sql.selectchapter(url)
            if rets[0]==1:
                print('章节已经存在。')
                pass
            else:
                # print(aurl)
                yield Request(url,self.getchaptercontent,meta={'num':num,'chaptername':chaptername,'url':url})
    def getchaptercontent(self,response):
        item = DcontentItem()
        item['url'] = response.meta['url']
        item['num'] = response.meta['num']
        item['chaptername'] = str(response.meta['chaptername']).replace('\xa0','')
        content = BeautifulSoup(response.text,'lxml').find('dd',id='contents').get_text()
        item['chaptercontent'] = str(content).replace('\xa0','')
        return item







