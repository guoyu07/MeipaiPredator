# encoding=utf-8
__author__ = 'Richard'
__homepage__ = 'http://data-vision.top/'
__email__ = 'data-vision@outlook'

import urllib
import urllib2
import re
import json
import MySQLdb
import sys
import time
import threading

g_mutex = threading.Condition()
g_queueURL = [] #等待爬取的 url 链接
g_existURL = [] #爬取过的链接
g_failedURL = [] # 失败 url
g_totalcount = 0 # 爬取数目

class Crawler:
    def __init__(self,crawlername, url, threadnum):
        self.crawlername = crawlername
        self.url = url
        self.threadnum = threadnum
        self.threadpool = []
        self.logfile=file("log.txt",'w')

    def craw(self):
        global g_queueURL
        g_queueURL.append(url)
        print self.crawlername + "Start...."

        while(len(g_queueURL) != 0):
            self.logfile.write("URL" + g_queueURL[0] + "...")
            self.insert()
            self.updateQueueURL()

    def insert(self):
        global g_queueURL

    def updateQueueURL(self):
        global g_queueURL

class CrawlerThread(threading.Thread):
