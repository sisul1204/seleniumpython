#!/usr/bin/env python
#coding:utf-8

#Author:sisul

import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest
# image = Image.open('E:/imooc1.png')
# text = pytesseract.image_to_string(image)
# print(text)

r = ShowapiRequest("http://route.showapi.com/184-5","81995","5df514155ac94e20b80363c8e9a921e0" )
r.addBodyPara("img_base64", "")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", r"E:/imooc1.png") #文件上传时设置
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息