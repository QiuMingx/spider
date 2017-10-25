# encoding:utf-8
import urllib2
import urllib
import random

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom= HTTP/1.1"

headers = {
"Host":"fanyi.youdao.com",
"Connection":"keep-alive",
"Content-Length":"208",
"Accept":"application/json, text/javascript, */*; q=0.01",
"Origin":"http://fanyi.youdao.com",
"X-Requested-With":"XMLHttpRequest",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
"DNT":"1",
"Referer":"http://fanyi.youdao.com/?keyfrom=dict2.index",

"Accept-Language":"zh-CN,zh;q=0.8",
}

#key = raw_input("请输入需要翻译的文字：")

formdata ={
"i":"有",
"from":"AUTO",
"to":"AUTO",
"smartresult":"dict",
"client":"fanyideskweb",
"salt":"1508390738816",
"sign":"fba493c01766932b0ed304877632dfd0",
"doctype=json&version":"2.1",
"keyfrom":"fanyi.web",
"action":"FY_BY_CLICKBUTTION",
"typoResult":"true",
}

data = urllib.urlencode(formdata)

request = urllib2.Request(url, data = data, headers = headers)

response = urllib2.urlopen(request)
print(response.read())