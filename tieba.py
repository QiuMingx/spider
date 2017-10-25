#_*_ coding:utf-8 _*_

import urllib
import urllib2

def loadPage(url, filename):
	"""
		作用：根据url发送请求，获取服务器响应文件
		url:需要爬取的url地址

	"""
	print("正在下载" + filename)

	headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"
}
	request =  urllib2.Request(url, headers=headers)
	return  urllib2.urlopen(request).read()


def writePage(page, filename):
	"""
		作用：将html内容到本地
		url:服务器相应文件内容

	"""
	print("正在保存" + filename)
	with open(filename, "w") as f:
		f.write(page)
	print("_" * 30 )




def tiebaSpider(url, beginPage, endPage):
	"""
		作用：贴吧爬虫调度器，负责组合处理每个页面url
		url: 贴吧url的前部分
		benginPage:起始页
		endPage: 结束页
	"""
	for page in range(beginPage, endPage + 1):
		pn = (page - 1) * 50
		filename = "第" + str(page) + "页.html"
		fullurl = url + '&pn=' + str(pn)
		html = loadPage(fullurl,filename)
		writePage(html, filename)



	

if __name__ == '__main__':

	kw = raw_input("请输入需要的贴吧名： ")
	beginPage = int(raw_input("请输入起始页: "))
	endPage = int(raw_input("请输结束页:"))

	url = 'http://tieba.baidu.com/f?'
	key = urllib.urlencode({'kw':kw})
	fullurl = url + key
	tiebaSpider(fullurl, beginPage, endPage)