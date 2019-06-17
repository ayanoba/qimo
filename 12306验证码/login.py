import requests
from PIL import Image
import json
import config
#cookie保持
#第一步：请求首页面，获取cookie
UA = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.13 Safari/537.36"
header = {"User-Agent": UA,
          "Referer": "http://www.v2ex.com/signin"
          }
session=requests.Session()
url="https://kyfw.12306.cn/otn/login/userLogin"
response=session.get(url)
#第二步：下载验证码
captcha_url="https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.5604448691516117"
cap_response=session.get(captcha_url)
#保存验证码
with  open('1.jpg','wb')   as   f:
    f.write(cap_response.content)
img=Image.open('1.jpg')
img.show()#将图片表示出来，用画图工具打开，然后就能看见像素
ver=input("请输入验证码>>>")#从验证码中得知的像素
f.close()
#第三步：校验验证码
check_url="https://kyfw.12306.cn/passport/captcha/captcha-check"
data={
    "answer":ver,
    "login_site":"E",
    "rand":"sjrand"
    }
check_response=session.post(check_url,data=data,headers = header)
print(check_response.text)
#判断校验结果
#if not check_response["result_code"]=="4":
   # exit("验证码校验失败，请重新登陆")
#第四步：登录
login_url="https://kyfw.12306.cn/passport/web/login"
login_data={
    "username":config.username,
    "password":config.password,
    "appid":"otn"
    }
login_response=session.post(login_url,data=login_data,headers = header)
print(login_response)
#第五步：获取权限token
f_url="https://kyfw.12306.cn/passport/web/auth/uamtk"
f_data={
    "appid":"otn"
    }
res=session.post(f_url,data=f_data)
print(res)
#第六步：获取权限
#auth_url="https://kyfw.12306.cn/otn/uamauthclient"
#auth_data={
   # "tk":token['newapptk']
   # }
#res=session.post(auth_url,data=auth_data,headers = header)
#print(res.text)
#最后一步：跳转登录
login_redirect="https://kyfw.12306.cn/otn/index/initMy12306Api"
response=session.get(login_redirect)
print(response.text)
