# encoding=utf-8
__author__ = 'Richard'
__homepage__ = 'http://data-vision.top/'
__email__ = 'data-vision@outlook'

import urllib
import urllib2
import re


def getContent(url):
    page = urllib2.urlopen(url)
    content = page.read()
    page.close()
    content = content.decode('UTF-8','ignore')
    return content


def getNavUrls(content):
    navExp = r'<div\sclass=\"nav\smax\scenter\spr\"[\s\S]*?</div>'
    navUrlExp = r'href=[\s\S]*?>'
    navReg = re.compile(navExp)
    navUrlReg = re.compile(navUrlExp)
    navContent = re.findall(navReg, content)
    navUrlList = re.findall(navUrlReg,navContent[0])
    for navUrl in navUrlList:
        print "http://www.meipai.com/" + navUrl[6:len(navUrl)-2]
    return navUrlList


def getMediaInfo(content):
    mediaExp = r'<li\sclass=\"pr\sno-select loading\"[\s\S]*?</li>'
    mediaReg = re.compile(mediaExp)
    mediaInfoList = re.findall(mediaReg, content)
    print len(mediaInfoList)
    for medianInfo in mediaInfoList:
        print medianInfo
    return

def downloadMedia(content):
    return

def getUserInfo(content):
    return

contents = getContent("http://www.meipai.com//square/16")
contents = contents.encode('GBK','ignore')

getMediaInfo(contents)