import requests
from urllib.parse import  urlencode
import json
from  bs4 import  BeautifulSoup
#from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import  expected_conditions as EC
from  selenium.webdriver.support.wait import  WebDriverWait
def get_page_index(offset,keyword):
    data={
        'offset': '80',
        'format': 'json',
        'keyword': '爱粮节粮',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesi'
    }
    url="https://www.toutiao.com/search_content/?"+urlencode(data)
    response=requests.get(url)
    if response.status_code==200:
        return response.text
    else:
        return None
def parse_page_index(html):
    data=json.loads(html)  #转化为一个对象
    if data and 'data' in data.keys():  #data.keys()返回的是JSON里面的所有的键名
       for item in data.get("data"):
            s= item.get('id')
            yield s    #yield关键字用于函数中，会把函数保障为generator进行迭代

#def get_page_detial(url):
    #soup=BeautifulSoup(html,'lxml')
    #title=soup.find(name='h1',attrs={'class':'article-title'}).text
    #source=soup.find(name='')
    #content=soup.find()
    #brower = webdriver.Chrome()
    #brower.get(url=url)
    #title = brower.find_element_by_class_name("article-title").text
    #print(title)
    #content = brower.find_element_by_class_name("article-content").text
    #print(content)
    #source = brower.find_element_by_class_name("article-sub").text
    #print(source)
    #data_dict = {}
    #data_dict["title"] = title
    #data_dict[content] = content
    #data_dict[source] = source
    #data_list = []
    #data_list.append(data_dict)
    #print(data_list)
    #with open('demo1.text', 'a+', encoding='utf-8') as f:
       # f.write(str(data_list))
        #f.close()
def main ():
    url2="https://www.toutiao.com/a"
    html=get_page_index('0','爱粮节粮')
    print(html)
    for url in parse_page_index(html):
        if url!="6342689974949232898" and url!="6477870236073722126" and url!="6477777683202703886"and url!="6342032176989602050" and url!="6612831306562667016"and url!="6477506283221025294":
            print(url2+url)
            brower = webdriver.Chrome()
            brower.get(url=url2+url)
            title =brower.find_element_by_class_name("article-title").text
            print(title)
            content = brower.find_element_by_class_name("article-content").text
            print(content)
            source = brower.find_element_by_class_name("article-sub").text
            print(source)
            data_dict = {}
            data_dict["link"]=url2+url
            data_dict["title"] = title
            data_dict["content"] = content
            data_dict["source"] = source
            data_list = []
            data_list.append(data_dict)
            print(data_list)
            with open('demo3.text', 'a+', encoding='utf-8') as f:
                f.write(str(data_list))
                f.close()
        else:
            continue

if __name__=='__main__':
    main()


