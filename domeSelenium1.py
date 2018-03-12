# #调用异常
# from selenium.common.exceptions import NoSuchElementException
# #调用键盘
# from selenium.webdriver.common.keys import Keys
import time

from selenium import webdriver

# 手动添加驱动路径
# path = "./chromedriver.exe"
# path = "./IEDriverServer.exe"
# path = "F:\\Work\\domeSelenium1\\IEDriverServer.exe"
# 打开谷歌浏览器
driver = webdriver.Ie()
# driver = webdriver.Chrome()
# driver = webdriver.Chrome(executable_path=path)
# driver = webdriver.Ie(executable_path=path)
# driver.get("http://trade.develop.wei3dian.com") # Load page 在地址栏输入http://www.baidu.com 进入百度
# 定位元素的五中方式 id name xpath link class
driver.get("http://login.develop.wei3dian.com/login.html")

driver.find_element_by_id('loginId').clear()  # 先清除用户名
driver.find_element_by_id('loginId').send_keys(
    'dghmyy2018')  # 根据id找到对应的输入框  输入用户名dghmyy2018

driver.find_element_by_id('password').clear()  # 先清除密码
driver.find_element_by_id('password').send_keys(
    'dghmyy2018')  # 根据id找到对应的输入框  输入密码dghmyy2018

time.sleep(1)
driver.find_element_by_class_name(
    'login_box_r').click()  # 根据id找到对应的输入框  输入密码dghmyy2018
time.sleep(2)
driver.find_element_by_class_name('btn-block').click()  # 找到对应的按钮  登陆
time.sleep(1)
driver.find_element_by_class_name('fa-balance-scale').click()  # 找到对应的按钮  东莞交易
time.sleep(3)
driver.find_element_by_xpath(
    '/html/body/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div/ul/span[7]').click()  # 点击订单管理
time.sleep(1)
driver.find_element_by_xpath(
    '/html/body/div[2]/div/div/div[1]/div/div/div[2]/div[1]/div/ul/span[7]/li/ul/li/ul/li[1]').click()  # 点击采购计划
time.sleep(1)
driver.find_element_by_class_name('page_left').click()  # 点击新增
time.sleep(1)
driver.find_element_by_xpath(
    '/html/body/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/form/div/div[3]/div/div/div/button[1]/span').click()  # 点击添加明细
time.sleep(1)
# driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[4]/div/div/div/div[2]/div[2]/div[3]/table/tbody/tr[1]').click()  #选中一行
driver.find_element_by_xpath(
    '/html/body/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[4]/div/div/div/div[2]/div[2]/div[2]/table/thead/tr/th[1]/div/label/span').click()  # 全部选中
time.sleep(1)
driver.find_element_by_xpath(
    '/html/body/div[2]/div/div/div[1]/div/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[4]/div/div/div/div[2]/div[3]/div/span/button[1]/span').click()  # 点击确认

time.sleep(5)
driver.quit()
