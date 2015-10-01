# encoding=utf-8
#coding=utf-8
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

def createTable(sql):
    try:
        conn = MySQLdb.connect(host='127.0.0.1', user='root',passwd='wangmurong',db='meipai',use_unicode=1,charset='utf8')
    except Exception, e:
        print e
        sys.exit()
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
    except Exception,e:
        print e
    print "Create Table Success!"

def insertUser(user):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    sql_content = """insert into user(reposts_count,has_password,gender,constellation,id,
                                   city,photo_count,verified,locked_videos_count,followers_count,
                                   province,screen_name_all,friends_count,birthday,be_liked_count,
                                   real_videos_count,real_locked_videos_count,screen_name,videos_count,country,
                                   age,url,status,avatar,locked_photos_count,
                                   created_at)
                                   values(%s,%s,%s,%s,%s,
                                           %s,%s,%s,%s,%s,
                                           %s,%s,%s,%s,%s,
                                           %s,%s,%s,%s,%s,
                                           %s,%s,%s,%s,%s,
                                           %s)"""

    insertValue = (user['reposts_count'],user['has_password'],user['gender'],user['constellation'],user['id'],
                    user['city'],user['photos_count'],user['verified'],user['locked_videos_count'],user['followers_count'],
                    user['province'],user['screen_name_all'],user['friends_count'],user['birthday'],user['be_liked_count'],
                    user['real_videos_count'],user['real_locked_videos_count'],user['screen_name'],user['videos_count'],user['country'],
                    user['age'],user['url'],user['status'],user['avatar'],user['locked_photos_count'],
                    user['created_at'])
    try:
        conn = MySQLdb.connect(host='127.0.0.1', user='root',passwd='wangmurong',db='meipai',use_unicode=1,charset='utf8')
    except Exception, e:
        print e
        sys.exit()
    cursor = conn.cursor()
    try:
        cursor.execute(sql_content,insertValue)
    except Exception,e:
        print e
    conn.commit()
    print 'insert success'

def insertMedia(media):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    sql_content = """insert into media(is_popular,is_long,reposts_count,feed_id,
                                   video,show_controls,category,campaign,id,
                                   caption_url_params,cover_pic,user_id,likes_count,
                                   locked,url,created_at,caption_all,comments_count,
                                   time)
                                   values(%s,%s,%s,%s,
                                           %s,%s,%s,%s,%s,
                                           %s,%s,%s,%s,
                                           %s,%s,%s,%s,%s,
                                           %s)"""

    insertValue = (media['is_popular'],media['is_long'],media['reposts_count'],media['feed_id'],
                   media['video'],media['show_controls'],media['category'],media['campaign'],media['id'],
                   media['caption_url_params'],media['cover_pic'],media['user_id'],media['likes_count'],
                   media['locked'],media['url'],media['created_at'],media['caption_all'],media['comments_count'],
                   media['time'])
    try:
        conn = MySQLdb.connect(host='127.0.0.1', user='root',passwd='wangmurong',db='meipai',use_unicode=1,charset='utf8')
    except Exception, e:
        print e
        sys.exit()
    cursor = conn.cursor()
    try:
        cursor.execute(sql_content,insertValue)
    except Exception,e:
        print e
    conn.commit()
    print 'insert success'



def queryUser():
    querySql = "select *from user"
    try:
        conn = MySQLdb.connect(host='127.0.0.1', user='root',passwd='wangmurong',db='meipai',use_unicode=1,charset='utf8')
    except Exception, e:
        print e
        sys.exit()
    cursor = conn.cursor()
    cursor.execute(querySql)
    row = cursor.fetchone()
    print row
    comment = "u'" + row[4] + "'"

    print row[4]
    print u'\u9b54\u7faf\u5ea7'
    #text = "u" +eval(row[4])
    #comment = "u'" + row[4].encode('gbk') + "'"
    #print text

create_user_table_sql = """CREATE TABLE USER (
        REPOSTS_COUNT INT,
        HAS_PASSWORD CHAR(6),
        GENDER CHAR(1),
        CONSTELLATION VARCHAR(200),
        ID INT NOT NULL PRIMARY KEY ,
        CITY INT,
        PHOTO_COUNT INT,
        VERIFIED CHAR(6),
        LOCKED_VIDEOS_COUNT INT,
        FOLLOWERS_COUNT INT,
        PROVINCE INT,
        SCREEN_NAME_ALL VARCHAR(200),
        FRIENDS_COUNT INT,
        BIRTHDAY VARCHAR(30),
        BE_LIKED_COUNT INT,
        REAL_VIDEOS_COUNT INT,
        REAL_LOCKED_VIDEOS_COUNT INT,
        SCREEN_NAME VARCHAR(200) CHARACTER SET utf8 COLLATE utf8_unicode_ci,
        VIDEOS_COUNT INT,
        COUNTRY INT,
        AGE VARCHAR(20),
        URL VARCHAR(200),
        STATUS INT,
        AVATAR VARCHAR(200),
        LOCKED_PHOTOS_COUNT INT,
        CREATED_AT VARCHAR(30)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8"""

create_media_table_sql = """CREATE TABLE MEDIA (
        IS_POPULAR VARCHAR(6),
        IS_LONG CHAR(6),
        REPOSTS_COUNT INT,
        FEED_ID VARCHAR(50),
        VIDEO VARCHAR(200),
        SHOW_CONTROLS VARCHAR(6),
        CATEGORY INT,
        CAMPAIGN VARCHAR(6),
        ID INT NOT NULL PRIMARY KEY ,
        CAPTION_URL_PARAMS VARCHAR(6),
        COVER_PIC VARCHAR (200),
        USER_ID INT,
        LIKES_COUNT INT,
        LOCKED VARCHAR(6),
        URL VARCHAR (100),
        CREATED_AT VARCHAR(30),
        CAPTION_ALL VARCHAR(300),
        COMMENTS_COUNT INT,
        TIME INT
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8"""

#createTable(create_user_table_sql)
#createTable(create_media_table_sql)
for i in range(10):
    url = "http://www.meipai.com/squares/new_timeline?page=" + str(i+1) +"&count=100&tid=19&maxid=414124079"
    print url
    contents = getContent(url)
    contents = contents.encode('GBK','ignore')
    contentsJson = json.loads(contents)
    mediaInfoList = contentsJson['medias']
    #print mediaInfoList[1]['user']
    print len(mediaInfoList)
    #print mediaInfoList[0]
    for mediaInfo in mediaInfoList:
       #print medianInfo
       user = mediaInfo['user']
       del mediaInfo['qq_share_caption']
       del mediaInfo['weibo_share_caption']
       del mediaInfo['qzone_share_caption']
       del mediaInfo['weixin_share_caption']
       del mediaInfo['instagram_share_caption']
       del mediaInfo['weixin_friendfeed_share_caption']
       del mediaInfo['facebook_share_caption']
       del mediaInfo['user']
       del mediaInfo['geo']
       del mediaInfo['caption_origin']
       mediaInfo['user_id'] = user['id']
       #print mediaInfo
       #print user
       insertMedia(mediaInfo)
       insertUser(user)
    time.sleep(5)
#insertUser()
   #print user+

#insertUser(mediaInfoList[1]['user'])
#queryUser()
#getMediaInfo(contents)