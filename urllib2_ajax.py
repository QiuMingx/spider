# encoding:utf-8
import urllib2
import urllib

url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action"
headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",

}

formdata ={
	
"start" : "0"
"limit" : "20",

}

data = urllib.urlencode(formdata)

request = urllib2.Request(url, data = data , headers = headers)

response = urllib2.urlopen(request)

print(response.read())
