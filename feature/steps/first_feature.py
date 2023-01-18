# from behave import *
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
#
#
#
# @given(u'launch chrome')
# def step_impl(context):
#     context.driver = webdriver.Chrome()
#
#
# @when(u'open url')
# def step_impl(context):
#     context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     time.sleep(3)
#
#
# @then(u'verify logo present')
# def step_impl(context):
#     context.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[1]/img").is_displayed()
#
#
# @then(u'close browser')
# def step_impl(context):
#     context.driver.close()
#
