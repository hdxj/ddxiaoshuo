from .sql import Sql
from ding.items import DingItem
from ding.items import DcontentItem
class DingPipeline(object):
    def process_item(self,item,spider):
        if isinstance(item,DingItem):
            nameid = item['nameid']
            ret = Sql.selectname(nameid)
            if ret[0]==1:
                print('已经存在了。')
                pass
            else:
                xs_name = item['name']
                xs_author = item['author']
                category = item['category']
                Sql.insert_dingdianname(xs_name,xs_author,category,nameid)
                print('开始存小说标题。。。')
        if isinstance(item,DcontentItem):
            url = item['url']
            num = item['num']
            xs_chaptername = item['chaptername']
            xs_content = item['chaptercontent']
            Sql.insert_chaptername(xs_chaptername,xs_content,num,url)
            print('小说存储完毕。。。')
            return item