# -*- coding: UTF-8 -*- 
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys
import unittest
from HTMLTestRunner import HTMLTestRunner
sys.path.append('D:\\test\\isee_login')
sys.path.append('D:\\test\\center')
sys.path.append('D:\\test\\peinvest')
# import login_module
from selenium.webdriver.support.ui import WebDriverWait
from log_module import Loginfo
from logindata import get_webinfo,get_userinfo,get_infodata
import center_module
import peinvest_module
import login_module
import logindata


test_dir='.'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')

class TotalTest(unittest.TestCase):
	"""添加进其他的测试文件"""
	def setUp(self):
		pass

	def test_center(self):
		center_module.account_center('https://www.iseecapital.com')

	def test_peinvest(self):
		peinvest_module.peinvest_opmp('https://www.iseecapital.com')

	def test_login(self):
		logindata1=logindata.get_webinfo('D:\\test\\isee_login\\webinfo.txt')
		userdata1=logindata.get_userinfo('D:\\test\\isee_login\\userinfo.txt')
		infodata1=logindata.get_infodata('D:\\test\\isee_login\\infodata.txt')
		login_module.login_test(logindata1,userdata1,infodata1)

	def tearDown(self):
		pass


if __name__=="__main__":
	now=time.strftime("%Y-%m-%d %H_%M_%S")
	filename='./'+now+'_result.html'
	fp=open(filename,'wb')
	runner=HTMLTestRunner(stream=fp,title='test report',description='test result')
	runner.run(discover)
	fp.close()