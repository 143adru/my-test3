import datetime
import time
from functools import wraps
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class chrome():
    def driver_init(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        return driver


class edge():
    def driver_init(self):
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        return driver


class firefox():
    def driver_init(self):
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        return driver


class driverFactory():

    def __init__(self,dri):
       self.dri = globals()[dri]()
       self.driver = self.dri.driver_init()

    def get_url(self):
       self.driver.get('https://www.google.com/')
       time.sleep(2)
       return self.driver

    def quit_dirver(self):
       self.driver.close()


class selenium_actions():
     def __init__(self, driver):
         self.driver = driver
     def click_element(self, identifer, value):
         self.driver.find_element(identifer, value).click()
     def sendkeys(self, identifer, value, data):
         self.driver.find_element(identifer, value).send_keys(data)

def exe_time(func):
    def run_time(*args,**kwargs):
       start = datetime.datetime.now()
       result = func(*args, **kwargs)
       end_time = datetime.datetime.now() - start
       print(f'test function exeuted in {end_time}')
       return result
    return run_time()


@exe_time
def launch_edge():
      driver_obj = driverFactory('edge')
      driver = driver_obj.get_url()
      search_box = "//input[@title='Search']"
      searchbox_btn = "//input[@value='Google Search']"
      action_obj = selenium_actions(driver)
      action_obj.sendkeys(By.XPATH, search_box, "gmail")
      driver.implicitly_wait(2)
      action_obj.click_element(By.XPATH, searchbox_btn)
      driver_obj.quit_dirver()

@exe_time
def launch_chrome():
      driver_obj = driverFactory('chrome')
      driver = driver_obj.get_url()
      search_box = "//input[@title='Search']"
      searchbox_btn = "//input[@value='Google Search']"
      action_obj = selenium_actions(driver)
      action_obj.sendkeys(By.XPATH, search_box, "gmail")
      driver.implicitly_wait(2)
      action_obj.click_element(By.XPATH, searchbox_btn)
      driver_obj.quit_dirver()
