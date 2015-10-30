# _*_ coding:utf-8 _*_

from sys import argv #获取外部命令的参数
script, wr = argv

if wr == "w": 
	target = open('daily.txt','a') 
	print "我要开始装逼了"
	while True:
		s = raw_input('Enter something : ')
		target.write(s)
		target.write('\n')
		if s == 'end':
			break
	target.close()
	print 'Done'	
elif wr == "r":
	print "It's reading"
	target = open("daily.txt")
	print target.read()
