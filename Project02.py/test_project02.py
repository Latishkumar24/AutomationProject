from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest


class Test_latish:
    driver=webdriver.Firefox()
    url="https://www.amazon.in/"
    url2="https://www.flipkart.com/"
    

    @pytest.mark.first
    def test_amazon(self):
       self.driver.get(self.url)
       assert " Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in" != self.driver.title
    
    @pytest.mark.second
    def test_login(self):
        self.driver.get(self.url)
        account=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/header/div/div[1]/div[3]/div/a[2]/span")
        account.click()
        email_input=self.driver.find_element(by=By.ID,value="ap_email")
        email_input.send_keys("latishKumar24@gmail.com")
        time.sleep(2)
        continuebtn=self.driver.find_element(by=By.ID,value="continue")
        continuebtn.click()
        password=self.driver.find_element(by=By.ID,value="ap_password")
        password.send_keys("Latish@24")
        time.sleep(2)
        signin=self.driver.find_element(by=By.ID,value="signInSubmit")
        signin.click()
    
    @pytest.mark.third 
    def test_flipkart(self):
        self.driver.execute_script("window.open('about:blank','secondtab');")
        self.driver.switch_to.window("secondtab")
        self.driver.get(self.url2)
        assert "flipkart" != self.driver.title
    
    @pytest.mark.fourth
    def test_loginflipkart(self):
        login_button=self.driver.find_element(by=By.XPATH,value="/html/body/div/div/div[1]/div[1]/div[2]/div[3]/div/div/div/a")
        login_button.click()
        time.sleep(2)
        phoneno=self.driver.find_element(by=By.XPATH,value="/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input")
        phoneno.send_keys("****************")
        password=self.driver.find_element(by=By.XPATH,value="/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input")
        password.send_keys("************")
        time.sleep(2)
        login=self.driver.find_element(by=By.XPATH,value="/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button")
        login.click()





