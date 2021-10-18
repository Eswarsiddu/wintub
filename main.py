path = r'chromedriver.exe'

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from random import randrange
from string import ascii_lowercase


refrencelink = "https://wintub.com/?r=6387328"
s = Service(path)


def getdob():
    day = randrange(1,30)
    month = randrange(1,12)
    year = randrange(1985,2000)
    return str(day)+'/'+str(month)+'/'+str(year)

def getname():
    n = randrange(4,20)
    s = ''
    for i in range(n):
        s += ascii_lowercase[randrange(0,len(ascii_lowercase))]
    return s


while True:

    driver = webdriver.Chrome(service=s)
    driver.get(refrencelink)

    sleep(3)

    x = driver.find_element_by_xpath('//*[@id="header"]/div/nav/ul/li[2]/a')
    x.click()

    sleep(2)
    driver.find_element_by_xpath('//*[@id="data"]/div[1]/div[1]/div/input').send_keys(getname())

    driver.find_element_by_xpath('//*[@id="data"]/div[1]/div[2]/div/input').send_keys(getname())

    driver.find_element_by_xpath('//*[@id="data"]/div[2]/div[1]/div/div/input').send_keys(getdob())

    emailid = getname()+'@'+getname()+'.com'
    driver.find_element_by_xpath('//*[@id="data"]/div[3]/div[1]/div/input').send_keys(emailid)

    driver.find_element_by_xpath('//*[@id="data"]/div[3]/div[2]/div/input').send_keys(getname())

    inp = input("y/n:")
    driver.find_element_by_xpath('//*[@id="data"]/div[5]/button').click()
    sleep(10)
    driver.close()
    driver.quit()
    if inp == 'n':
        exit(0)
