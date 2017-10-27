#_*_ coding:utf-8 _*_

import urllib
import urllib2
from lxml import etree
from datetime import datetime

class Spider(object):
	
	def __init__(self):
		self.kw = raw_input("请输入需要的贴吧名： ")
		self.beginPage = int(raw_input("请输入起始页: "))
		self.endPage = int(raw_input("请输结束页:"))
		self.url = 'http://tieba.baidu.com/f'
		self.header =  {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}
		dt = datetime.now()
		self.image_name = dt.strftime('%Y%m%d') 

	def tieba_spider(self):
		"""
			作用：循环获取目标地址。

		"""
		for page in range(self.beginPage, self.endPage + 1):
			pn = (page - 1) * 50
			key = urllib.urlencode({'kw':self.kw})
			fullurl = self.url + '?'+ key +'&pn=' + str(pn)
			self.loadPage(fullurl)
		
	def loadPage(self,url):
		"""
			作用：根据url发送请求，获取服务器响应文件
			url:需要爬取的url地址

		"""
		request =  urllib2.Request(url, headers=self.header)
		html = urllib2.urlopen(request).read()
		# 解析HTML文档为HTML DOM模型
		content = etree.HTML(html)

		link_list = content.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
		for link in link_list:
			fulllink = "http://tieba.baidu.com" + link
			self.loadImage(fulllink)

	def loadImage(self, url):
		"""
			作用：根据url发送请求，获取服务器响应文件
			url: 帖子内容页
		
		"""
		request = urllib2.Request(url, headers = self.header)
		html = urllib2.urlopen(request).read()
		content = etree.HTML(html)
		# 获取帖子里所有图片的src路径
		link_list = content.xpath('//img[@class="BDE_Image"]/@src')
		# 获取图片地址，调用下载函数
		for link in link_list:
			self.writeImage(link)

	def writeImage(self, url):
		"""
			作用：将图片下载到本地
			url:图片相应文件地址

		"""
		request = urllib2.Request(url, headers = self.header)
		image = urllib2.urlopen(request).read()
		print url
		print("正在下载%s.%s..." % self.image_name)

		with open('./images/'+self.image_name, "wb") as f:
			
			f.write(image)
		
		self.image_name = str(int(self.image_name) + 1)


if __name__ == '__main__':

	ispider = Spider()
	ispider.tieba_spider()