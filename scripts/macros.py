#!/usr/bin/python
# coding: utf-8

git_base_url = "https://github.com/begood0513/goodnews/blob/master/pages"

head = '####  [法轮功真相](../../../../basic/blob/master/README.md) &nbsp;|&nbsp; [九评共产党](../../../../9ping.md/blob/master/README.md) &nbsp;|&nbsp; [解体党文化](../../../../jtdwh.md/blob/master/README.md)  &nbsp;|&nbsp; [共产主义的终极目的](../../../../gczydzjmd.md/blob/master/README.md) &nbsp;|&nbsp; [魔鬼在统治我们的世界](../../../../mgztzwmdsj.md/blob/master/README.md) \n\n'
#'#### [💌武汉肺炎来势凶凶， 我要抛弃中共邪党保命](https://github.com/begood0513/goodnews/blob/master/quit/letter.md)\n\n'

menu = "#### [首页](../../README.md)  &nbsp;&nbsp;|&nbsp;&nbsp; _channellink_  &nbsp;&nbsp;|&nbsp;&nbsp; [热点推荐](../../indexes/热点推荐.md)  &nbsp;&nbsp;|&nbsp;&nbsp; [法轮功真相](../../../../../basic/blob/master/README.md) &nbsp;&nbsp;|&nbsp;&nbsp; [翻墙教程](https://github.com/gfw-breaker/guides/blob/master/README.md)\n\n"

links = "\n\n#### [ 💌 【特稿】越亲中共疫情越重 防疫有良方](https://github.com/begood0513/goodnews/blob/master/pages/nsc424/n12042989.md) &nbsp; | &nbsp;[ 病毒汹汹，抗毒有秘籍](https://github.com/begood0513/goodnews/blob/master/quit/letter.md) \n\n #### [ 🎬  翻墙必看视频（八九六四、法轮功、709大抓捕、香港反送中 ...）](https://github.com/gfw-breaker/banned-news1/blob/master/pages/link4.md)\n\n #### [ 🎬  《红墙的记忆》- 4.25中南海万人和平上访纪实 ](http://136.244.78.252:10000/videos/legend/425.html)\n\n #### 网站代理：[大纪元新闻网](http://141.164.54.31:10080/gb/) &nbsp;|&nbsp; [新唐人电视台](http://141.164.54.31:8000/gb/)\n\n"

tail = ""

def write_page(channel, f_name, f_path, title, link, content):
	clink = '[{}](../../indexes/{}.md) '.format(channel, channel)
	nmenu = menu.replace('_channellink_', clink)
	new_link = git_base_url + '/' + channel + '/' + f_name
	body = '### ' + title
	body += "\n------------------------\n\n" + nmenu + "\n\n" +  content
	body += "\n<hr/>\n手机上长按并复制下列链接或二维码分享本文章：<br/>"
	body += "\n" + new_link + " <br/>"
	body += "\n<a href='" + new_link + "'><img src='" + new_link + ".png'/></a> <br/>"
	body += "\n原文地址（需翻墙访问）：" + link + "\n"
	body += "\n\n------------------------\n" + nmenu 
	body += "\n<img src='http://gfw-breaker.win/goodnews/" + f_path[3:] + "' width='0px' height='0px'/>"
	fh = open(f_path, 'w')
	fh.write(body)
	fh.close()

