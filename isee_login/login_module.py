# -*- coding: UTF-8 -*- 
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from logindata import get_webinfo,get_userinfo,get_infodata
from log_module import Loginfo


# logindata={'url':'https://www.itouzi.com/','test_name':'//*[@id="top_header_sign_out"]/li[2]/a','test_username':'/html/body/div[2]/div/div/form/div[1]/input','test_pwd':'/html/body/div[2]/div/div/form/div[2]/input','test_login':'/html/body/div[2]/div/div/form/div[5]/button'}
# userdata=[{'uname':'18210149904','pwd':'123'}]
# infodata={'allnull':'/html/body/div[2]/div/div/form/div[1]/div','pwdnull':'/html/body/div[2]/div/div/form/div[2]/div',
# 'allerror':'/html/body/div[2]/div/div/form/div[5]/div'}

#从文件txt中读取web的元素，用户的信息，web的提示错误信息元素定位
logindata=get_webinfo('webinfo.txt')
userdata=get_userinfo('userinfo.txt')
infodata=get_infodata('infodata.txt')

#从xls上读取用户信息（用户名，密码）
# xinfo = xluserinfo('/Users/ply/Documents/pythontest/login/userinfo.xls')
# userdata = xinfo.get_sheetinfo_by_index(0)


#打开浏览器，输入URL
def openBrower(url):
	options = webdriver.ChromeOptions()
	prefs = {"":""}
	prefs["credentials_enable_service"] = False
	prefs["profile.password_manager_enabled"] = False
	options.add_experimental_option("prefs", prefs)
	driver = webdriver.Chrome(chrome_options=options)   #配置chrome，不出现保存密码等弹窗
	# driver=webdriver.Chrome()
	driver.get(url['url'])
	driver.implicitly_wait(3)
	return driver


#找到页面的关于登录web元素，返回一组元组
def findElement(d,arg):
	# ele_login=d.find_element_by_xpath(arg['test_name'])
	# ele_login.click()
	d.implicitly_wait(3)
	d.maximize_window()
	userEle=d.find_element_by_xpath(arg['test_username'])
	pwdEle=d.find_element_by_xpath(arg['test_pwd'])
	loginEle=d.find_element_by_xpath(arg['test_login'])
	return userEle,pwdEle,loginEle


#登录后退出页面刷新，元素过时需要在重新调用下定位元素方法，但是没有点击登录按钮这步
def findElement_q(d,arg):
	d.implicitly_wait(3)
	userEle=d.find_element_by_xpath(arg['test_username'])
	pwdEle=d.find_element_by_xpath(arg['test_pwd'])
	loginEle=d.find_element_by_xpath(arg['test_login'])
	return userEle,pwdEle,loginEle


#对返回的一组元组发送登录数据
def sendValus(tuples,arg):
	listkey=['uname','pwd']
	i=0
	time.sleep(2)
	for key in listkey:
		tuples[i].send_keys('')
		tuples[i].clear()
		tuples[i].send_keys(arg[key])
		i+=1
	tuples[2].click()
	time.sleep(3)


#不成功登录的case进行提示元素定位是否存在，存在则打印元素的text,并且把所有用户登录信息写入日志
def checkresult(driver,infodata,arg,log):
	result=False
	time.sleep(4)
	try:
		for key in infodata:
		    driver.implicitly_wait(5)
		    # driver.switch_to_alert().accept()
		    ele_err=driver.find_element_by_xpath(infodata[key])
		    if ele_err.text:
		    	print('username or pwd error')
		    	msg='%s: error: %s' %(arg,ele_err.text)
		    	log.log_write(msg)
		    	# print(ele_err.text)
	except:
		print('username and pwd right!')
		msg='%s :pass' %(arg)
		log.log_write(msg)
		result=True
	return result


def loginout(d,logindata):
	time.sleep(2)
	ele=d.find_element_by_xpath(logindata['test_loginout'])
	ActionChains(d).move_to_element(ele).perform()
	time.sleep(5)
	ele1=d.find_element_by_xpath(logindata['test_loginout1'])
	ele1.click()

def login_test(logindata,userdata,infodata):
	d=openBrower(logindata)
	log=Loginfo()
	ele_tuple=findElement(d,logindata)
	for arg in userdata:
		sendValus(ele_tuple,arg)
		result=checkresult(d,infodata,arg,log)
		if result:
			loginout(d,logindata)
			ele_tuple=findElement_q(d,logindata)
	log.log_close()


if __name__=='__main__':
	login_test(logindata,userdata,infodata)


