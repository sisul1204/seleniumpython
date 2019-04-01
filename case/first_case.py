#!/usr/bin/env python
#coding:utf-8

#Author:sisul
from busniess.register_busniess import RegisterBusniess
from selenium import webdriver
class FirtCase(object):
	def __init__(self):
		driver = webdriver.Chrome()
		driver.get('http://www.5itest.cn/register')
		self.login = RegisterBusniess(driver)

	def test_login_email_error(self):
		email_error = self.login.login_email_error('34','user111','111111','test1')
		if email_error == True:
			print('注册成功了，此条case执行失败')
		#通过assert判断是否为error

	def test_login_username_error(self):
		username_error = self.login.login_email_error('34@qq.com', 'ss', '111111', 'test1')
		if username_error == True:
			print('注册成功了，此条case执行失败')

	def test_login_code_error(self):
		code_error = self.login.login_email_error('34@qq.com', 'ss', '111111', 'test1')
		if code_error == True:
			print('注册成功了，此条case执行失败')

	def test_login_password_error(self):
		password_error = self.login.login_email_error('34@qq.com', 'ss', '111111', 'test1')
		if password_error == True:
			print('注册成功了，此条case执行失败')

	def test_login_success(self):
		success = self.login.login_email_error('34@qq.com', 'ss', '111111', 'test1')
		if self.login.register_success() == True:
			print('注册成功')


def main():
	first = FirtCase()
	first.test_login_code_error()
	first.test_login_email_error()
	first.test_login_password_error()
	first.test_login_success()
	first.test_login_username_error()

if __name__ == '__main__':
	main()




