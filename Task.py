import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select



class Latish:
    driver = webdriver.Firefox()
    url = "https://www.zenclass.in "
    
    #method created to login zenclass
    def start_up(self):
        self.driver.get(self.url)
        email_input =self.driver.find_element(by=By.XPATH,value="/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input")
        password_input = self.driver.find_element(by=By.XPATH,value="/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input")
        email_input.send_keys("latishKumar24@gmail.com")
        password_input.send_keys("Latish@24")
        time.sleep(10)
        login_button = self.driver.find_element(by=By.XPATH,value="/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/button")
        login_button.click()

    def entry(self):
        #maximizing the window
        self.driver.maximize_window()
        time.sleep(15)
        #finding the query element to click
        queries = self.driver.find_element(by=By.XPATH,value="/html/body/div/div[1]/nav/ul/div[6]")
        queries.click()
        #giving sleep time
        time.sleep(5)
        #this is used for mouse actions
        action = ActionChains(webdriver.Firefox())
        action.move_by_offset(173, 128)
        action.perform()
        time.sleep(5)
        #finding create query element to click
        create_queries = self.driver.find_element(by=By.XPATH,value="/html/body/div/div[2]/div/div[1]/div[1]/button")
        time.sleep(2)
        create_queries.click()
        #find cancel element to click
        cancel= self.driver.find_element(by=By.XPATH,value="/html/body/div/div[2]/div/div[2]/div[6]/div[2]/div/div/section[3]/div[2]/button[1]")
        cancel.click()
        time.sleep(5)
        #finding category element to select index 1
        cate_gory=self.driver.find_element(by=By.NAME,value="category")
        drp=Select(cate_gory)
        drp.select_by_index(1)
        #finding subcategory element to select index 2
        sub_category=self.driver.find_element(by=By.NAME,value="subcategory")
        drp1=Select(sub_category)
        drp1.select_by_index(1)
        #find language element to select index 1
        lang_uage=self.driver.find_element(by=By.NAME,value="language")
        drp2=Select(lang_uage)
        drp2.select_by_index(1)
        #finding query title element to input the title
        query_title =self.driver.find_element(by=By.XPATH,value="/html/body/div/div[2]/div/div[2]/div/div/form/div[5]/div/input")
        #finding query desc element to input the description
        query_Desc=self.driver.find_element(by=By.XPATH,value="/html/body/div/div[2]/div/div[2]/div/div/form/div[5]/textarea")
        #scrolling the page from up to down
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        #sending keys to input the query title
        query_title.send_keys("Guvi Python AT :- 1 &2 Automation Project")
        time.sleep(5)
        #sending keys  to query desc to input description
        query_Desc.send_keys("This is a Project Test Code Running for the Python Automation 1&2 Project Given by mentor Mr. Suman Gangopadhyay.")
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #finding create element to click
        Create_button=self.driver.find_element(by=By.XPATH,value="/html/body/div/div[2]/div/div[2]/div/div/form/div[13]/div/button")
        Create_button.click()

#creating an obj for class
s=Latish()
s.start_up()
#calling this method five times as it was asked to create query 5 times
s.entry()
s.entry()
s.entry()
s.entry()
s.entry()