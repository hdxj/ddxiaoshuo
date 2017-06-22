import mysql.connector
from ding import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = mysql.connector.connect(user=MYSQL_USER,password=MYSQL_PASSWORD,host=MYSQL_HOSTS,database=MYSQL_DB)
cur = cnx.cursor(buffered=True)

class Sql:
    @classmethod
    def insert_dingdianname(cls,xs_name,xs_author,category,nameid):
        sql = 'INSERT INTO dingdianname(xs_name,xs_author,category,nameid)VALUES(%(xs_name)s,%(xs_author)s,%(category)s,%(nameid)s)'
        value = {
            'xs_name':xs_name,
            'xs_author':xs_author,
            'category':category,
            'nameid':nameid
        }
        cur.execute(sql,value)
        cnx.commit()
    @classmethod
    def selectname(cls,nameid):
        sql = 'SELECT EXISTS(SELECT 1 FROM dingdianname WHERE nameid=%(nameid)s)'
        value ={
            'nameid':nameid
        }
        cur.execute(sql,value)
        return cur.fetchall()[0]
    @classmethod
    def insert_chaptername(cls,xs_chaptername,xs_content,num,url):
        sql = 'INSERT INTO chaptername(xs_chaptername,xs_content,num,url)VALUES(%(xs_chaptername)s,%(xs_content)s,%(num)s,%(url)s)'
        value = {
            'xs_chaptername':xs_chaptername,
            'xs_content':xs_content,
            'num':num,
            'url':url
        }
        cur.execute(sql,value)
        cnx.commit()
    @classmethod
    def selectchapter(cls,url):
        sql = 'SELECT EXISTS(SELECT 1 FROM chaptername WHERE url=%(url)s)'
        value ={
            'url':url
        }
        cur.execute(sql,value)
        return cur.fetchall()[0]

