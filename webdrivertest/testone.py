#coding=utf-8
>>> b=webdriver.Ie()
>>> b.get("http://www.baidu.com")
>>> b.find_element_by_id("kw").send_keys("selenium")
>>> b.back()
>>> b.get("http://www.baidu.com")
>>> "baidu" in b.title
False
>>> "百度" in b.title
True
>>> b.current_url()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    b.current_url()
TypeError: 'str' object is not callable
>>> b.current_url
'https://www.baidu.com/'
>>> ele2=b.find_element_by_name("wd")
>>> ele2.send_keys("selenium")
>>> ele2=b.find_element_by_tag_name("input")
>>> id(ele2)
52059888
>>> ele2=b.find_element_by_name("wd")
>>> id(ele2)
52023152
>>> 
