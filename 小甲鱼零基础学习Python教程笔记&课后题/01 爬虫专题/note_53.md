
# 一、网页爬虫
## 遵循一定规则访问网络资源、获取网络资源。
## 千里之行，始(死)于足下?????????

# 二、python 如何访问互联网
## url + lib = urllib
## url:统一资源定位
## url的一般格式：（带方括号[]的为可选项）:
## protocol://hostname[:port]/path/[;parameters][?query]#frament
## 三部分：
### 1、协议：http、https,ftp,file,ed2k....
### 2、存放资源的服务器域名系统或ip地址，有时包含端口号，各种传输协议都有默认的端口号，如http的默认端口是80
### 3、资源的具体地址
### 4、其他参数
  

# 三、urllib简要介绍
## urllib是个包，包含四个模块：urllib.request,urllib.error,urllib.parse,urllib.robotparser
## 主要讲解内容为urllib.request

# 四、urllib.request.urlopen


```python
import urllib.request
respone_obj = urllib.request.urlopen('http://www.baidu.com')
#print(respone_obj)
html = respone_obj.read()
print(respone_obj.geturl())
print(respone_obj.info())
print(respone_obj.getcode())
html = html.decode('utf-8')
#print(html)

```

    http://www.baidu.com
    Bdpagetype: 1
    Bdqid: 0xdea71a2f00105f84
    Cache-Control: private
    Content-Type: text/html
    Cxy_all: baidu+43fe4163991de796f9afb882ddeddd4d
    Date: Sun, 31 Mar 2019 15:36:33 GMT
    Expires: Sun, 31 Mar 2019 15:35:38 GMT
    P3p: CP=" OTI DSP COR IVA OUR IND COM "
    Server: BWS/1.1
    Set-Cookie: BAIDUID=759EB30321862015F863346A310FBAB5:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
    Set-Cookie: BIDUPSID=759EB30321862015F863346A310FBAB5; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
    Set-Cookie: PSTM=1554046593; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
    Set-Cookie: delPer=0; path=/; domain=.baidu.com
    Set-Cookie: BDSVRTM=0; path=/
    Set-Cookie: BD_HOME=0; path=/
    Set-Cookie: H_PS_PSSID=1468_21108_18559_28774_28723_28557_28697_28584_26350_28603_28627_28605; path=/; domain=.baidu.com
    Vary: Accept-Encoding
    X-Ua-Compatible: IE=Edge,chrome=1
    Connection: close
    Transfer-Encoding: chunked
    
    
    200
    


```python

```
