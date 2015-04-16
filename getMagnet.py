#coding=utf-8
import requests
import re

def getHtml(url):
    page = requests.get(url)
    html = page.content
    return str(html)


def getMagent(html):
    reg = r'(magnet.*?)<'
    magnetre = re.compile(reg)
    magnetlist = re.findall(magnetre,html)
    return magnetlist
    #for magnet in magnetlist:
        #print(magnet)


def getSomething(html,pattern):
    reg = re.compile(pattern)
    lists = re.findall(reg,html)
    return lists

#url = input('url:')
#getMagent(getHtml(url))

#import downloadTorrent
#url = input("url=")
#turl = getSomething(getHtml(url),r'(http://www.rmdown.com/link.php\?hash=.*?)<')
#a = downloadTorrent.downloadTorrent()
#for i in turl:
    #a.getTorrent(i)

