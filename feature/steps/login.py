from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# BDD behavior driven development

@given(u'launch chrome')
def step_impl(context):
    context.driver = webdriver.Chrome()



@when(u'open urll')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")





@when(u'Enter "{userName}" n "{Password}"')
def step_impl(context, userName, Password):
    time.sleep(4)
    context.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys(userName)
    context.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys(Password)




@when(u'Login button')
def step_impl(context):
    time.sleep(3)
    context.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
    time.sleep(5)



@then(u'verify login')
def step_impl(context):
    try:
        dashboard = context.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
    except:
        context.driver.close()
        assert True
    if dashboard == "Dashboard":
        assert True, "Test passed"


