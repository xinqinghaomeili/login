# -*- coding: UTF-8 -*- 
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys
sys.path.append('D:\\test\\isee_login')
from log_module import Loginfo

def openBrower(url):
	options = webdriver.ChromeOptions()
	prefs = {"":""}
	prefs["credentials_enable_service"] = False
	prefs["profile.password_manager_enabled"] = False
	options.add_experimental_option("prefs", prefs)
	driver = webdriver.Chrome(chrome_options=options)   #配置chrome，不出现保存密码等弹窗
	# driver=webdriver.Chrome()
	driver.get(url)
	driver.implicitly_wait(3)
	return driver

#登录成功
def sendValus(d):
	# ele_login=d.find_element_by_xpath(arg['test_name'])
	# ele_login.click()
	d.implicitly_wait(3)
	d.maximize_window()
	d.find_element_by_xpath('//*[@id="top_header_right"]/a[1]').click()
	d.implicitly_wait(3)
	userEle=d.find_element_by_xpath('/html/body/div[3]/div/form/div[1]/input')
	userEle.clear()
	userEle.send_keys('18210149904')
	pwdEle=d.find_element_by_xpath('/html/body/div[3]/div/form/div[2]/input')
	pwdEle.clear()
	pwdEle.send_keys('123456')
	loginEle=d.find_element_by_xpath('/html/body/div[3]/div/form/div[5]/button')
	loginEle.click()
	time.sleep(3)

def center(d):
	toaccount(d)
	reviewEle=d.find_element_by_xpath('//*[@id="safe_items"]/li[4]/a')
	reviewEle.click()          #重新测评元素
	time.sleep(2)
	titleEle=d.find_element_by_xpath('/html/body/div[3]/h1')  #风险评估页面title
	if titleEle.text :
		log=Loginfo()
		# log.log_write(titleEle.text)
		log.log_write('风险评估重测功能正常')
		toaccount(d)
		changepwdEle=d.find_element_by_xpath('//*[@id="safe_items"]/li[5]/span[3]')
		changepwdEle.click()             #修改密码元素
		#修改登录密码
		oldpwdEle=d.find_element_by_xpath('//*[@id="set_pwd"]/form[2]/div[1]/input')
		newpwdEle=d.find_element_by_xpath('//*[@id="set_pwd"]/form[2]/div[2]/input')
		repeatpwdEle=d.find_element_by_xpath('//*[@id="set_pwd"]/form[2]/div[3]/input')
		buttonEle=d.find_element_by_xpath('//*[@id="set_pwd"]/form[2]/div[4]/button')
		oldpwdEle.send_keys('123456')
		newpwdEle.send_keys('123456789')
		repeatpwdEle.send_keys('123456789')
		buttonEle.click()
		time.sleep(5)
		regEle=d.find_element_by_xpath('//*[@id="top_header_right"]/a') #注册元素，说明修改成功跳到注册页面
		if regEle.text:
			log.log_write('修改密码成功')



#进入个人账户的安全设置页面
def toaccount(d):
	time.sleep(2)
	ele=d.find_element_by_xpath('//*[@id="top_header_right"]/div[1]')
	ActionChains(d).move_to_element(ele).perform()
	time.sleep(5)
	ele1=d.find_element_by_xpath('//*[@id="top_header_right"]/div[2]/ul/li[1]/a')
	ele1.click()
	safeEle=d.find_element_by_xpath('/html/body/div[4]/div[1]/ul[2]/li/a')
	safeEle.click()

def account_center(url):
	d=openBrower(url)
	sendValus(d)
	center(d)


if __name__=='__main__':
	url='https://isc01.iseecapital.com'
	sys.path.append('D:\\test\\isee_login\\log_module')
	account_center(url)
