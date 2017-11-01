#coding:utf-8
import time

class Loginfo(object):
	def __init__(self,mode='wb'):
		now=time.strftime('%Y-%m-%d')
		filename=now+'.txt'
		self.log=open(filename,mode)

	def log_write(self,msg):
		self.log.write(msg)

	def log_close(self):
		self.log.close()


if __name__=='__main__':
	log=Loginfo()
	log.log_write('hahahha')
	log.log_close()

		