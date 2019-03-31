
# 测试题

## 0. 请问 URL 是“统一资源标识符”还是“统一资源定位符”？
url 是统一资源定位符(Uniform Resource Locator),URI 是统一资源标识符（Universal Resource Identifier）.

## 1. 什么是爬虫？
是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本

## 2. 设想一下，如果你是负责开发百度蜘蛛的攻城狮，你在设计爬虫时应该特别注意什么问题？
爬虫和存储效率要高、
爬出干扰信息怎么排除


## 3. 设想一下，如果你是网站的开发者，你应该如何禁止百度爬虫访问你网站中的敏感内容？（课堂上没讲，可以自行百度答案）
robots协议，告知百度爬虫不要爬敏感内容，但是robots协议是道德约束而非法律约束，搜索引擎能做到忽略robots协议自行爬去内容。

## 4. urllib.request.urlopen() 返回的是什么类型的数据？
### This function always returns an object which can work as a context manager and has methods such as "geturl()"、"info()"和"getcode()"
### 返回一个对象，能像一个上下管理器对象一样工作，拥有 geturl()、info()和getcode()等方法。
### type(response)  ------->    <class 'http.client.HTTPResponse'>



## 5. 如果访问的网址不存在，会产生哪类异常？
Raises URLError on protocol errors 或者 HTTPError????? ，貌似都是 URLError了


```python
import urllib.request
#responce = urllib.request.urlopen('htt://www.baidu.com')
responce = urllib.request.urlopen('http://www.123445568745212345493edjkcxkndsejwkdbjhcgksdfhisdh.com')
```


    ---------------------------------------------------------------------------

    gaierror                                  Traceback (most recent call last)

    C:\ProgramData\Anaconda3\lib\urllib\request.py in do_open(self, http_class, req, **http_conn_args)
       1316                 h.request(req.get_method(), req.selector, req.data, headers,
    -> 1317                           encode_chunked=req.has_header('Transfer-encoding'))
       1318             except OSError as err: # timeout error
    

    C:\ProgramData\Anaconda3\lib\http\client.py in request(self, method, url, body, headers, encode_chunked)
       1228         """Send a complete request to the server."""
    -> 1229         self._send_request(method, url, body, headers, encode_chunked)
       1230 
    

    C:\ProgramData\Anaconda3\lib\http\client.py in _send_request(self, method, url, body, headers, encode_chunked)
       1274             body = _encode(body, 'body')
    -> 1275         self.endheaders(body, encode_chunked=encode_chunked)
       1276 
    

    C:\ProgramData\Anaconda3\lib\http\client.py in endheaders(self, message_body, encode_chunked)
       1223             raise CannotSendHeader()
    -> 1224         self._send_output(message_body, encode_chunked=encode_chunked)
       1225 
    

    C:\ProgramData\Anaconda3\lib\http\client.py in _send_output(self, message_body, encode_chunked)
       1015         del self._buffer[:]
    -> 1016         self.send(msg)
       1017 
    

    C:\ProgramData\Anaconda3\lib\http\client.py in send(self, data)
        955             if self.auto_open:
    --> 956                 self.connect()
        957             else:
    

    C:\ProgramData\Anaconda3\lib\http\client.py in connect(self)
        927         self.sock = self._create_connection(
    --> 928             (self.host,self.port), self.timeout, self.source_address)
        929         self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    

    C:\ProgramData\Anaconda3\lib\socket.py in create_connection(address, timeout, source_address)
        706     err = None
    --> 707     for res in getaddrinfo(host, port, 0, SOCK_STREAM):
        708         af, socktype, proto, canonname, sa = res
    

    C:\ProgramData\Anaconda3\lib\socket.py in getaddrinfo(host, port, family, type, proto, flags)
        747     addrlist = []
    --> 748     for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
        749         af, socktype, proto, canonname, sa = res
    

    gaierror: [Errno 11001] getaddrinfo failed

    
    During handling of the above exception, another exception occurred:
    

    URLError                                  Traceback (most recent call last)

    <ipython-input-12-a05b34d5ef24> in <module>
          1 import urllib.request
          2 #responce = urllib.request.urlopen('htt://www.baidu.com')
    ----> 3 responce = urllib.request.urlopen('http://www.123445568745212345493edjkcxkndsejwkdbjhcgksdfhisdh.com')
    

    C:\ProgramData\Anaconda3\lib\urllib\request.py in urlopen(url, data, timeout, cafile, capath, cadefault, context)
        220     else:
        221         opener = _opener
    --> 222     return opener.open(url, data, timeout)
        223 
        224 def install_opener(opener):
    

    C:\ProgramData\Anaconda3\lib\urllib\request.py in open(self, fullurl, data, timeout)
        523             req = meth(req)
        524 
    --> 525         response = self._open(req, data)
        526 
        527         # post-process response
    

    C:\ProgramData\Anaconda3\lib\urllib\request.py in _open(self, req, data)
        541         protocol = req.type
        542         result = self._call_chain(self.handle_open, protocol, protocol +
    --> 543                                   '_open', req)
        544         if result:
        545             return result
    

    C:\ProgramData\Anaconda3\lib\urllib\request.py in _call_chain(self, chain, kind, meth_name, *args)
        501         for handler in handlers:
        502             func = getattr(handler, meth_name)
    --> 503             result = func(*args)
        504             if result is not None:
        505                 return result
    

    C:\ProgramData\Anaconda3\lib\urllib\request.py in http_open(self, req)
       1343 
       1344     def http_open(self, req):
    -> 1345         return self.do_open(http.client.HTTPConnection, req)
       1346 
       1347     http_request = AbstractHTTPHandler.do_request_
    

    C:\ProgramData\Anaconda3\lib\urllib\request.py in do_open(self, http_class, req, **http_conn_args)
       1317                           encode_chunked=req.has_header('Transfer-encoding'))
       1318             except OSError as err: # timeout error
    -> 1319                 raise URLError(err)
       1320             r = h.getresponse()
       1321         except:
    

    URLError: <urlopen error [Errno 11001] getaddrinfo failed>


## 6. 鱼C工作室（http://www.fishc.com）  的主页采用什么编码传输的？
### meta charset="UTF-8"
###  查看网页源代码可知，主页源代码的编码是 UTF-8

## 7. 为了解决 ASCII 编码的不足，什么编码应运而生？
ASCII只能保存英文字符，全世界字符种类那么多，Unicode诞生了.

# 动动手

# 0. 下载鱼C工作室首页（http://www.fishc.com） ，并打印前三百个字节。


```python
import urllib.request
responce = urllib.request.urlopen('http://www.fishc.com')
html = responce.read().decode('UTF-8') # html = responce.read(300)
print(html[:300])

```

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="keywords" content="鱼C工作室|免费编程视频教学|Python教学|Web开发教学|全栈开发教学|C语言教学|汇编教学|Win32开发|加密与解密|Linux教学">
        <meta name="description" content="鱼C工作室为大家提供最
    

# 1. 写一个程序，检测指定 URL 的编码
演示：请输入URL: http://www.fishc.com  该网页使用的编码是: utf-8


```python
import urllib.request
import chardet

url_src = input('请输入URL:')
response = urllib.request.urlopen(url_src)
html = response.read()
result = chardet.detect(html)
print('该网页使用的编码是:',result['encoding'])
print('可信度为:',result['confidence'])



```

    请输入URL:http://www.baidu.com
    该网页使用的编码是: utf-8
    可信度为: 0.99
    

## 2. 写一个程序，依次访问文件中指定的站点，并将每个站点返回的内容依次存放到不同的文件中。


```python
import urllib.request
import chardet
import sys
import io
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码,若不加上这句可能会有UnicodeEncodeError,貌似还有错误
with open(r'C:\Users\fengs\Desktop\urls.txt','r') as f:
    urls = f.readlines()  
for ind in range(len(urls)):
    responce = urllib.request.urlopen(urls[ind])
    html = responce.read()
    charinfo = chardet.detect(html)
    
    html = html.decode(charinfo['encoding'], "ignore")
    txt_file_name = r'C:\Users\fengs\Desktop\url_' + str(ind+1) + '.txt'
    with open(txt_file_name,'w',encoding=charinfo['encoding']) as f:  #搞掂
        f.write(html)
    

```

UnicodeEncodeError: 'gbk' codec can't encode character '\xbb' in position 29531: illegal multibyte sequence
解决方法:
    https://www.cnblogs.com/feng18/p/5646925.html
    
在Spyder运行又出现:
AttributeError: 'OutStream' object has no attribute 'buffer'    
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码,若不加上这句可能会有UnicodeEncodeError,貌似还有错误
