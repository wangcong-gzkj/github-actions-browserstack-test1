from selenium import webdriver
from threading import Thread
caps = [
    {
    'os_version': '10',
    'os': 'Windows',
    'browser': 'chrome',
    'browser_version': '86.0',
    'name': 'gg1', 
    'build': 'ggCase_bulid',
    },

]
username =  'wangcong1'
accessKey = 'cDEx8QD3UMfxCnVuAE9H'

def test_t1(cap):
    driver = webdriver.Remote('https://'+username+':'+accessKey+'@hub-cloud.browserstack.com/wd/hub', desired_capabilities=cap)
    driver.get('https://www.google.com')

for cap in caps:
    Thread(target=test_t1, args=(cap,)).start()  