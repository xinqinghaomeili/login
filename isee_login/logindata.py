#coding:utf-8
import codecs
# import xlrd

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
	# print (user_info)
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

if __name__=='__main__':
	get_userinfo('userinfo.txt')
# 	info=get_webinfo('/Users/ply/Documents/pythontest/login/webinfo.txt')
# 	info=get_userinfo('/Users/ply/Documents/pythontest/login/userinfo.txt')
# 	info=get_infodata('/Users/ply/Documents/pythontest/login/infodata.txt')




