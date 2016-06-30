
#爬下固定网页的图片数据
import urllib.request
import re

def getHtml(url):
	page = urllib.request.urlopen(url)
	html = page.read()
	page.close()
	return str(html)

def getImg(html):
	reg = r'src="([^"]*?\.jpg)" pic_ext'
	#reg = r'src="(.+?\.jpg)" pic_ext'
	imgre = re.compile(reg,re.M)
	imglist = re.findall(imgre,str(html))
	print(imglist)

	x = 0
	for imgurl in imglist:
		urllib.request.urlretrieve(imgurl,'%s.jpg'%x)
		x += 1
		if x>10:
			return


html = getHtml('http://tieba.baidu.com/p/2460150866')

getImg(html)