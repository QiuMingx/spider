#_*_ coding:utf-8 _*_

import urllib
import urllib2

url = "http://www.baidu.com/s"

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"
}
keyword = raw_input("请输入你要搜索的关键字：")

wd = {'wd':keyword}

# 通过urllib.urlencode()参数是一个dict类型

wd = urllib.urlencode(wd)


url = url  + '?' + wd

request = urllib2.Request(url, headers= headers)
	
response = urllib2.urlopen(request)

print(response.read())