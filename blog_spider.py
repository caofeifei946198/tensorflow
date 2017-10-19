import re
import datetime
import itertools
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool

class BlogSpider(object):
    '''爬取ｑｑ日志'''
    def __init__(self, spiderMessage, changer):
        self.message = spiderMessage
        self.changer = changer


    def beginer(self):
        blog_list = self.get_blog_list()#获取日志ＩＤ列表
        if blog_list:
            pool = Pool(self.changer.my_message.thread_num_Blog)
            myBlog = pool.map(self.get_blog, itertools.izip(blog_list.keys(), blog_list.values()))
            pool.close()
            pool.join()
            