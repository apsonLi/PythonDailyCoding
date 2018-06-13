# -*- coding: utf-8 -*-
import pymysql
import Error
__author__ = '''
       ________  ________   __
      / /  _/  |/  /  _/ | / /
 __  / // // /|_/ // //  |/ / 
/ /_/ // // /  / // // /|  /  
\____/___/_/  /_/___/_/ |_/ '''


class DB(object):
    @staticmethod
    def __get_db():
        try:
            db = pymysql.connect(**{
                "host": "127.0.0.1",
                "port" : 3307,
                "user": "root",
                "password": "root",
                "database": "video",
                'charset': 'utf8',
            })
        except pymysql.err.Error as e:
            if e.args[0] == 1049:
                raise Error.DatabaseNameError(e.args[1])
            else:
                raise Error.ConnectDatabaseError(e)
       # except Exception as e:
        #    raise Error.UnknownError(e)
        return db

    def select(self,title,table):
        db = self.__get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM  %s "
                    "WHERE `title` = %s ", (table,title))
        db.close()
        return cursor.fetchall()#返回全部匹配的值，以二维元祖的方式

    def write_video(self, title, keywords, desc, img, url, is_vip, pv, status, add_time, score):
        db = self.__get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO `video` ( `title`, `keywords`, `desc`, `img`, `url`, `is_vip`, `pv`, `status`, `add_time`, `score`) "
                       "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (title, keywords, desc, img, url, is_vip, pv, status, add_time, score))
        db.close()

    def write_douban_id(self, title,douban_id,keywords,desc):
        db = self.__get_db()
        cursor = db.cursor()

        cursor.execute("INSERT INTO `douban_id` ( `title`, `douban_id` ,`keywords`, `desc`) "
                       "VALUES (%s, %s, %s, %s)", (title, douban_id,keywords,desc))
        db.close()


    def update(self, desc, keywords, title):
        db = self.__get_db()
        cursor = db.cursor()
        cursor.execute("UPDATE `video` SET `desc` = %s, `keywords` = %s "
                       "WHERE `video`.`title` = %s", (desc, keywords, title))
        db.close()