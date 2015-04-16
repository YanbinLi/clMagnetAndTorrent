#coding=utf8
 
import urllib
import re
import requests

class downloadTorrent:
  def __init__(self,url = ""):
    self.url = url
  def getTorrent(self,URL,filepath):
    try:
      if URL is None:
        URL = self.url
      BOUNDARY = '----WebKitFormBoundaryyyQtXVW2CgASAIsq'
      start = URL.find('hash=')+5
      HASHCODE =  URL[start:]
      headers = {'Host': 'www.rmdown.com',
                 'Connection': 'keep-alive',
                 'Cache-Control': 'max-age=0',
                 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                 'Origin': 'http://www.rmdown.com',
                 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36 LBBROWSER',
                 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryyyQtXVW2CgASAIsq',
                 'Referer': '%s' % URL,
                 'Accept-Encoding': 'gzip, deflate',
                 'Accept-Language': 'zh-CN,zh;q=0.8',
                 }
      headersget = {'Host': 'www.rmdown.com',
                    'Connection': 'keep-alive',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.99 Safari/537.36 LBBROWSER',
                    'Accept-Encoding': 'gzip, deflate, sdch',
                    'Accept-Language': 'zh-CN,zh;q=0.8'
                  }
      s = requests.Session()
      response = s.get(URL,headers=headersget)
      res = str(response.content)
      reg  = r'NAME="reff" value="(.*?)=="'
      content = re.findall(re.compile(reg),res)
      #print(content[0])
      data = []
      data.append('--%s' % BOUNDARY)
      data.append('Content-Disposition: form-data; name="ref"\r\n\r\n%s' % HASHCODE)
      data.append('--%s' % BOUNDARY)
      data.append('Content-Disposition: form-data; name="reff"\r\n\r\n%s' % content[0])
      data.append('--%s' % BOUNDARY)
      data.append('Content-Disposition: form-data; name="submit"\r\n\r\n%s' % 'download')
      #data.append('--%s' % BOUNDARY)
      #data.append('Content-Type: application/force-download\n\r')
      data.append('--%s--' % BOUNDARY)
      data.append('')
      body = '\r\n'.join(data)
      
      url = 'http://www.rmdown.com/download.php'
      res = s.post(url,data=body,headers=headers)
      import os
      filepath = os.path.join(filepath,"%s.torrent" % HASHCODE)
      fw = open(filepath,'wb') 
      fw.write(res.content) 
      #print("%s.torrent done" % HASHCODE)
    except Exception as e:
      print(e)
    finally:
      fw.close()
      s.close()
      
    




