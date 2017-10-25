# encoding:utf-8
import urllib2
import urllib
import random

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
#url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=null'
headers = {
"Accept":"application/json, text/javascript, */*; q=0.01",
"X-Requested-With":"XMLHttpRequest",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
"Accept-Language":"zh-CN,zh;q=0.8",
}

key = raw_input("请输入需要翻译的文字：")

formdata ={
"i":key,
"from":"AUTO",
"to":"AUTO",
"smartresult":"dict",
"doctype" : "json",
"client":"fanyideskweb",
"salt":"1508390738816",
"doctype=json&version":"2.1",
"keyfrom":"fanyi.web",
"typoResult":"true",
}


data = urllib.urlencode(formdata)

request = urllib2.Request(url, data = data, headers = headers)

response = urllib2.urlopen(request)
print(response.read())