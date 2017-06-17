#coding:utf-8
import codecs
import xlrd

#获取浏览器txt的相关元素
def get_webinfo(path):
	web_info={}
	webinfo_list=[]
	config=codecs.open(path,'r','utf-8')
	for line in config:
		result=[ele.strip() for ele in line.split(',')]
		webinfo_list.append(result)
	# print webinfo_list
	for i in webinfo_list:
		web_info[i[0]]=i[1]
	# print web_info
	return web_info

#获取用户相关的txt用户名和密码
def get_userinfo(path):
	user_info=[]
	config=codecs.open(path,'r','utf-8')
	for line in config:
		user_dict={}
		result=[ele.strip() for ele in line.split(' ')]
		for r in result:
			account=[ele.strip() for ele in r.split('=')]
			user_dict.update(dict([account]))
		user_info.append(user_dict)
	# print user_info
	return user_info

#获取错误信息元素txt的相关元素
def get_infodata(path):
	web_info={}
	webinfo_list=[]
	config=codecs.open(path,'r','utf-8')
	for line in config:
		result=[ele.strip() for ele in line.split(',')]
		webinfo_list.append(result)
	# print webinfo_list
	for i in webinfo_list:
		web_info[i[0]]=i[1]
	# print web_info
	return web_info

#对表格数据进行处理，关于用户的登录账户和密码
class xluserinfo(object):
	def __init__(self,path):
		self.xl=xlrd.open_workbook(path)

	def floattostr(self,val):
		if isinstance(val,float):
			val=str(int(val))
		return val

	def get_sheet_info(self):
		listkey=['uname','pwd']
		infolist=[]
		for row in range(self.sheet.nrows):
			info=[self.floattostr(val) for val in self.sheet.row_values(row)]
			tmp=zip(listkey,info)
			infolist.append(dict(tmp))
		return infolist

	def get_sheetinfo_by_name(self,name):
		self.sheet=self.xl.sheet_by_name(name)
		return self.get_sheet_info()

	def get_sheetinfo_by_index(self,index):
		self.sheet=self.xl.sheet_by_index(index)
		return self.get_sheet_info()


if __name__=='__main__':
	info=get_webinfo('/Users/ply/Documents/pythontest/login/webinfo.txt')
	info=get_userinfo('/Users/ply/Documents/pythontest/login/userinfo.txt')
	info=get_infodata('/Users/ply/Documents/pythontest/login/infodata.txt')
	xinfo = xluserinfo('/Users/ply/Documents/pythontest/login/userinfo.xls')
	info = xinfo.get_sheetinfo_by_index(0)

