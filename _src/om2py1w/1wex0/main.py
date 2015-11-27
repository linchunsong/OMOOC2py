# _*_ coding:utf-8 _*_

from sys import argv #获取外部命令的参数
script, wr = argv
prompt = ">> "
if wr == "w":
	target = open('daily.txt','a')
	print "开始写吧,输入'end'结束"
	while True:
		s = raw_input(prompt)
		target.write(s)
		target.write('\n')
		if s == 'end':
			break
	target.close()
	print '日记已保存。'
elif wr == "r":
	print "It's reading"
	target = open("daily.txt")
	print target.read()
