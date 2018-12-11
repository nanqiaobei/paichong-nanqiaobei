# coding:utf-8
from selenium import webdriver

m1=1
m2=13
year='2018'
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
for j in range(m1,m2):
    if j<10:
        url_initial='http://www.meteomanz.com/sy2?l=1&cou=2250&ind=58238&d1=01&m1=0'+str(j)+'&y1='+year+'&d2=31&m2=0'+str(j)+'&y2='+year
    else:
        url_initial='http://www.meteomanz.com/sy2?l=1&cou=2250&ind=58238&d1=01&m1='+str(j)+'&y1='+year+'d2=31&m2='+str(j)+'&y2='+year
    driver.get(url_initial)
    for i in range(2,33):
        try:
            Date=driver.find_element_by_xpath('/html/body/div[@class="center_aux"]/div[@class="center_d"]/table[@class="data"]/tbody/tr[%d]/td[1]/a'%i)
            print (Date.text)
            AveT=driver.find_element_by_xpath('/html/body/div[@class="center_aux"]/div[@class="center_d"]/table[@class="data"]/tbody/tr[%d]/td[2]'%i)
            print (AveT.text)
            MaxT=driver.find_element_by_xpath('/html/body/div[@class="center_aux"]/div[@class="center_d"]/table[@class="data"]/tbody/tr[%d]/td[3]'%i)
            print (MaxT.text)

            MinT=driver.find_element_by_xpath('/html/body/div[@class="center_aux"]/div[@class="center_d"]/table[@class="data"]/tbody/tr[%d]/td[4]'%i)
            print (MinT.text)
            Prec=driver.find_element_by_xpath('/html/body/div[@class="center_aux"]/div[@class="center_d"]/table[@class="data"]/tbody/tr[%d]/td[5]'%i)
            print (Prec.text)
            Press=driver.find_element_by_xpath('/html/body/div[@class="center_aux"]/div[@class="center_d"]/table[@class="data"]/tbody/tr[%d]/td[6]'%i)
            print (Press.text)
            Wind=driver.find_element_by_xpath('/html/body/div[@class="center_aux"]/div[@class="center_d"]/table[@class="data"]/tbody/tr[%d]/td[7]'%i)
            print (Wind.text)
            Windsp=driver.find_element_by_xpath('/html/body/div[@class="center_aux"]/div[@class="center_d"]/table[@class="data"]/tbody/tr[%d]/td[8]'%i)
            print (Windsp.text)
            Cloud=driver.find_element_by_xpath('/html/body/div[@class="center_aux"]/div[@class="center_d"]/table[@class="data"]/tbody/tr[%d]/td[9]'%i)
            print (Cloud.text)
        except:
            break