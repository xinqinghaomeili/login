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
	userEle=d.find_element_by_name('username')
	userEle.clear()
	userEle.send_keys('18210149904')
	pwdEle=d.find_element_by_name('password')
	pwdEle.clear()
	pwdEle.send_keys('123456789')
	loginEle=d.find_element_by_xpath('/html/body/div[3]/div/form/div[5]/button')
	loginEle.click()
	time.sleep(3)

def invest(d):
	time.sleep(2)
	d.find_element_by_link_text(u"投资项目").click()
	time.sleep(2)
	d.find_element_by_xpath('/html/body/div[4]/a[1]/ul').click()
	time.sleep(2)
	d.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/span').click()
	time.sleep(3)
	ele=d.find_element_by_xpath('//*[@id="shortcut_skip_step1"]/div[1]')
	ActionChains(d).move_to_element(ele).perform()
	d.find_element_by_xpath('//*[@id="shortcut_skip_step1"]/div[1]/label/input').click()
	d.find_element_by_xpath('//*[@id="shortcut_skip_step1"]/div[1]/span').click()
	time.sleep(3)


	d.find_element_by_xpath("//input[@type='text']").clear()
	d.find_element_by_xpath("//input[@type='text']").send_keys("300")
	d.find_element_by_xpath("//li[4]/div/button").click()
	time.sleep(2)
	successEle=d.find_element_by_xpath('/html/body/div[3]/div/h2')
	if successEle.text:
		print ('11111111111')
		log=Loginfo()
		log.log_write(successEle.text)

def peinvest_opmp(url):
	d=openBrower(url)
	sendValus(d)
	invest(d)

if __name__=='__main__':
	url='https://isc01.iseecapital.com'
	peinvest_opmp(url)


