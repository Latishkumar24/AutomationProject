import time
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import pytest


class Test_latish():
    driver = webdriver.Firefox()
    url = "https://www.zenclass.in "

    
    def test_setup(self):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.maximize_window()
     
    
    def test_login(self):  
        self.driver.get(self.url)  
        email_input =self.driver.find_element(by=By.XPATH,value="/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input")
        password_input = self.driver.find_element(by=By.XPATH,value="/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input")
        email_input.send_keys("latishKumar24@gmail.com")
        password_input.send_keys("Latish@24")
        time.sleep(10)
        login_button = self.driver.find_element(by=By.XPATH,value="/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/button")
        login_button.click()
    
    
    def test_query(self):
        time.sleep(15)
        queries = self.driver.find_element(by=By.XPATH,value="/html/body/div/div[1]/nav/ul/div[6]")
        queries.click()
        time.sleep(5)
        action = ActionChains(webdriver.Firefox())
        action.move_by_offset(173, 128)
        action.perform()
        time.sleep(5)
        create_queries = self.driver.find_element(by=By.XPATH,value="/html/body/div/div[2]/div/div[1]/div[1]/button")
        time.sleep(2)
        create_queries.click()
    
    
    def test_info(self):
        cancel= self.driver.find_element(by=By.XPATH,value="/html/body/div/div[2]/div/div[2]/div[6]/div[2]/div/div/section[3]/div[2]/button[1]")
        cancel.click()
        time.sleep(5)
        cate_gory=self.driver.find_element(by=By.NAME,value="category")
        drp=Select(cate_gory)
        drp.select_by_index(1)
        sub_category=self.driver.find_element(by=By.NAME,value="subcategory")
        drp1=Select(sub_category)
        drp1.select_by_index(1)
        lang_uage=self.driver.find_element(by=By.NAME,value="language")
        drp2=Select(lang_uage)
        drp2.select_by_index(1)
        query_title =self.driver.find_element(by=By.XPATH,value="/html/body/div/div[2]/div/div[2]/div/div/form/div[5]/div/input")
        query_Desc=self.driver.find_element(by=By.XPATH,value="/html/body/div/div[2]/div/div[2]/div/div/form/div[5]/textarea")
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        query_title.send_keys("Guvi Python AT :- 1 &2 Automation Project")
        time.sleep(5)
        query_Desc.send_keys("This is a Project Test Code Running for the Python Automation 1&2 Project Given by mentor Mr. Suman Gangopadhyay.")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        Create_button=self.driver.find_element(by=By.XPATH,value="/html/body/div/div[2]/div/div[2]/div/div/form/div[13]/div/button")
        Create_button.click()

    
    def test_teardown(self):
        self.driver.close()
        self.driver.quit()
        print("test completed")



