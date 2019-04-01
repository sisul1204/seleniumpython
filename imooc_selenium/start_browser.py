#!/usr/bin/env python
#coding:utf-8

#Author:sisul

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.5itest.cn/register')
time.sleep(5)
print(EC.title_contains('注册'))
email_element = driver.find_element_by_id("register_email")
driver.save_screenshot("E:/imooc.png")
code_element = driver.find_element_by_id('getcode_num')
print(code_element.location)
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width'] + left
height = code_element.size['height'] + top
im = Image.open("E:/imooc.png")
img = im.crop((left,top,right,height))
img.save('E:/imooc1.png')

r = ShowapiRequest("http://route.showapi.com/184-5","81995","5df514155ac94e20b80363c8e9a921e0" )
r.addBodyPara("img_base64", "")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", r"E:/imooc1.png") #文件上传时设置
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息
time.sleep(2)
driver.find_element_by_id('captcha_code').send_keys(text)
time.sleep(2)



driver.close()













# for i in range(5):
# 	user_email = ''.join(random.sample('1234567890asdfghjklqwery', 5)) + '@163.com'
# 	print(user_email)
