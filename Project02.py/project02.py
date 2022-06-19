from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class latish:
    driver=webdriver.Firefox()
    url="https://www.amazon.in/"
    url2="https://www.flipkart.com/"
    
    #method for retrieving amazon and flipkart laptop
    def a_f_laptop(self):
        #creating empty list for retrieving name and price
        laptop_name=[]
        laptop_price=[]
        #opening amazon and collecting  info
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.maximize_window()
        #finding the element and searching the configuration
        input=self.driver.find_element(by=By.ID,value='twotabsearchtextbox')
        input.send_keys("Laptop i5 8GB RAM with 1 TB HDD")
        search=self.driver.find_element(by=By.ID,value='nav-search-submit-button')
        search.click()
        time.sleep(5)
        #sorting the product from low to high in prices
        sort_by=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/span/div/h1/div/div[2]/div/div/form/span/span/span/span/span[1]')
        sort_by.click()
        low_high=self.driver.find_element(by=By.ID,value="s-result-sort-select_1")
        low_high.click()
        time.sleep(3)
        #HP - finding element and retrieving data
        HP=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[4]/ul/li[1]/span/a/div/label/i')
        HP.click()
        time.sleep(2)
        Laptop_HPname=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span")
        Laptop_HPprice=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a/span[1]/span[2]/span[2]")
        #printing data in text
        a=print(Laptop_HPname.text)
        b=print(Laptop_HPprice.text)
        #appending the data to text
        laptop_name.append(a)
        laptop_price.append(b)
        time.sleep(5)
        #clicking the clear so that next brand can be selected
        clear=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[4]/ul/li[1]/span/a/span[2]")
        clear.click()
        
        #lenovo- finding element and retrieving data
        Lenovo=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[4]/ul/li[5]/span/a/div/label/i")
        Lenovo.click()
        time.sleep(3)
        Laptop_Lenovoname=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span")
        Laptop_Lenovoprice=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a/span[1]/span[2]/span[2]")
        #print data in text
        c=print(Laptop_Lenovoname.text)
        d=print(Laptop_Lenovoprice.text)
        #appending to list
        laptop_name.append(c)
        laptop_price.append(d)
        time.sleep(5)
        #clicking clear so that next brand can be selected
        clear=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[4]/ul/li[1]/span/a/span[2]")
        clear.click()
        time.sleep(5)

        #Asus- finding element and retrieving data
        Asus=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[4]/ul/li[4]/span/a/div/label/i")
        Asus.click()
        time.sleep(3)
        Laptop_Asusname=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span")
        Laptop_Asusprice=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/a/span[1]/span[2]/span[2]")
        time.sleep(5)
        #print data in text
        e=print(Laptop_Asusname.text)
        f=print(Laptop_Asusprice.text)
        #appending data in list
        laptop_name.append(e)
        laptop_price.append(f)
        clear=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[4]/ul/li[1]/span/a/span[2]")
        clear.click()
        time.sleep(8)

        #Dell- finding element and retrieving data
        Dell=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[4]/ul/li[1]/span/a/div/label/i")
        Dell.click()
        time.sleep(3)
        Laptop_Dellname=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span")
        Laptop_Dellprice=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/a/span[1]/span[2]/span[2]")
        #print(f"{Laptop_Dellname.text}  :-  ₹{Laptop_Dellprice.text}")
        time.sleep(5)
        g=print(Laptop_Dellname.text)
        h=print(Laptop_Dellprice.text)
        laptop_name.append(g)
        laptop_price.append(h)
        #clicking clear so that other brand can be found
        clear=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[4]/ul/li[1]/span/a/span[2]")
        clear.click()
        time.sleep(5)

        #Acer- finding element and retrieving data
        Acer=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[4]/ul/li[3]/span/a/div/label/i")
        Acer.click()
        time.sleep(3)
        Laptop_Acername=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span")
        Laptop_Acerprice=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[2]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a/span[1]/span[2]/span[2]")
        #print data in text
        i=print(Laptop_Acername.text)
        j=print(Laptop_Acerprice.text)
        #append data to list
        laptop_name.append(i)
        laptop_price.append(j)
        #switching the tab to flipkart
        self.driver.execute_script("window.open('about:blank','secondtab');")
        self.driver.switch_to.window("secondtab")
        #opening flipkart url
        self.driver.get(self.url2)
        time.sleep(3)
        
        #HP2 - entering the brand 
        input=self.driver.find_element(by=By.XPATH,value='/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
        input.send_keys(" HP Laptop i5 8GB RAM with 1 TB HDD")
        search=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
        search.click()
        time.sleep(3)
        #to select laptop which have lowest price
        Low_High=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[3]/div[1]/div[2]/div[1]/div/div/div[2]/div[3]")
        Low_High.click() 
        time.sleep(3)
        Laptop_HP2name=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]")
        Laptop_HP2price=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]")
        #printing retrieved data into text
        a2=Laptop_HP2name.text
        b2=Laptop_HP2price.text
        print(a2)
        print(b2)
        #appendind info to list
        laptop_name.append(a2)
        laptop_price.append(b2)
        
        
        #clearing the input field so that next brand can be searched
        input=self.driver.find_element(by=By.CSS_SELECTOR,value='._3704LK').clear()
        #Lenovo2-checking for lenovo
        input=self.driver.find_element(by=By.XPATH,value='/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
        input.send_keys(" Lenovo Laptop i5 8GB RAM with 1 TB HDD")
        search=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
        search.click()
        time.sleep(3)
        Low_High=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[3]/div[1]/div[2]/div[1]/div/div/div[2]/div[3]")
        Low_High.click() 
        time.sleep(3) 
        Laptop_Lenovo2name=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]")
        Laptop_Lenovo2price=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]")
        c2=Laptop_Lenovo2name.text
        d2=Laptop_Lenovo2price.text
        print(c2)
        print(d2)
        time.sleep(3)
        input=self.driver.find_element(by=By.CSS_SELECTOR,value='._3704LK').clear()
        #appending to list
        laptop_name.append(c2)
        laptop_price.append(d2)
        time.sleep(5)
        #Asus2-checking for Asus
        input=self.driver.find_element(by=By.XPATH,value='/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
        input.send_keys("  Asus Laptop i5 8GB RAM with 1 TB HDD")
        search=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
        search.click()
        time.sleep(3)
        Low_High=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[3]/div[1]/div[2]/div[1]/div/div/div[2]/div[3]")
        Low_High.click()
        time.sleep(3)
        Laptop_Asus2name=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]")
        Laptop_Asus2price=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]")
        
        e2=Laptop_Asus2name.text
        f2=Laptop_Asus2price.text
        print(e2)
        print(f2)
        laptop_name.append(e2)
        laptop_price.append(f2)
        time.sleep(2)
        #searching the input field and clearing it 
        input=self.driver.find_element(by=By.CSS_SELECTOR,value='._3704LK').clear()

        
        #Dell2-checking for Dell
        input=self.driver.find_element(by=By.XPATH,value='/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
        input.send_keys("  Dell Laptop i5 8GB RAM with 1 TB HDD")
        search=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
        search.click()
        time.sleep(3)
        Low_High=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[3]/div[1]/div[2]/div[1]/div/div/div[2]/div[3]")
        Low_High.click()

        Laptop_Dell2name=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]")
        Laptop_Dell2price=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]")
        #time.sleep(5)
        g2=Laptop_Dell2name.text
        h2=Laptop_Dell2price.text
        print(g2)
        print(h2)
        laptop_name.append(g2)
        laptop_price.append(h2)
        time.sleep(2)
        input=self.driver.find_element(by=By.CSS_SELECTOR,value='._3704LK').clear()
        
        #Acer2-checking for acer
        input=self.driver.find_element(by=By.XPATH,value='/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
        input.send_keys("  Acer Laptop i5 8GB RAM with 1 TB HDD")
        search=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
        search.click()
        time.sleep(3)
        Low_High=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[3]/div[1]/div[2]/div[1]/div/div/div[2]/div[3]")
        Low_High.click()
        Laptop_Acer2name=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]")
        Laptop_Acer2price=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]")
        time.sleep(5)
        i2=Laptop_Acer2name.text
        j2=Laptop_Acer2price.text
        laptop_name.append(i2)
        laptop_price.append(j2)
        print(i2)
        print(j2)
        #printing the list 
        print(laptop_name)
        print(laptop_price)
        #closing all the tabs that were open
        self.driver.quit()
        finallist=zip(laptop_name,laptop_price)

        for data in list(finallist):
            print(data)
        #all the retrieved info is saved to excel file
        wb=self.Workbook()
        sh1.wb.active
        for x in list(finallist):
            sh1.append(x)
        
        wb.save("FinalNames.xlsx")

    #method for retrieving amazon and flipkart mobile
    def a_f_mobile(self):
        #creating empty list 
        mobile_name=[]
        mobile_price=[]
        #opening the amazon website
        self.driver.get(self.url)
        time.sleep(3)
        #maximizing the window
        self.driver.maximize_window()
        #finding the input field
        input=self.driver.find_element(by=By.ID,value='twotabsearchtextbox')
        #sending info that is to be seached
        input.send_keys("4G 6GB RAM and 128 GB memory")
        search=self.driver.find_element(by=By.ID,value='nav-search-submit-button')
        search.click()
        time.sleep(5)

        #oneplus-finding and retrieving info
        oneplus=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[4]/ul/li[1]/span/a/div/label/i')
        oneplus.click()
        time.sleep(2)
        oneplus_name=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span')
        oneplus_price=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[2]/a/span/span[2]/span[2]')
        #time.sleep(5)
        #printing info in text
        a=oneplus_name.text
        b=oneplus_price.text
        #appending to list
        mobile_name.append(a)
        mobile_price.append(b)
        time.sleep(5)
        print(a)
        print(b)
        #clearing so that next brand can be searched
        clear=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[4]/ul/li[1]/span/a/span[2]")
        clear.click()
        
        #oppo-finding and retrieving info
        oppo=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[4]/ul/li[2]/span/a/div/label/i')
        oppo.click()
        time.sleep(2)
        #retrieving name and price 
        oppo_name=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span')
        oppo_price=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a/span[1]/span[2]/span[2]')
        time.sleep(5)
        c=oppo_name.text
        d=oppo_price.text
        #appending to list
        mobile_name.append(c)
        mobile_price.append(d)
        time.sleep(3)
        print(c)
        print(d)
        clear=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[4]/ul/li[1]/span/a/span[2]")
        clear.click()
        
         
        #Realme
        Realme=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[4]/ul/li[6]/span/a/div/label/i')
        Realme.click()
        time.sleep(2)
        Realme_name=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span')
        Realme_price=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[2]/a/span[1]/span[2]/span[2]')
        #time.sleep(5)
        e=oppo_name.text
        f=oppo_price.text
        #appending to list
        mobile_name.append(e)
        mobile_price.append(f)
        time.sleep(2)
        print(e)
        print(f)
        clear=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[4]/ul/li[1]/span/a/span[2]")
        clear.click()
        time.sleep(5)

        #iqoo
        iqoo=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[4]/ul/li[3]/span/a/div/label/i')
        iqoo.click()
        time.sleep(2)
        iqoo_name=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span')
        iqoo_price=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a/span[1]/span[2]/span[2]')
        g=iqoo_name.text
        h=iqoo_price.text
        #appending to list
        mobile_name.append(g)
        mobile_price.append(h)
        time.sleep(2)
        print(g)
        print(h)
        #clearing so that other brand can be searched
        clear=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[4]/ul/li[1]/span/a/span[2]")
        clear.click()
        time.sleep(5)

        #Tecno
        Tecno=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[4]/ul/li[5]/span/a/div/label/i')
        Tecno.click()
        time.sleep(2)
        Tecno_name=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span')
        Tecno_price=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[3]/div/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div[1]/a/span[1]/span[2]/span[2]')
        #printing info to text
        i=Tecno_name.text
        j=Tecno_price.text
        #appending to list
        mobile_name.append(i)
        mobile_price.append(j)
        time.sleep(2)
        print(i)
        print(j)
        clear=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div[1]/div[2]/div/div[3]/span/div[1]/div/div/div[4]/ul/li[1]/span/a/span[2]")
        clear.click()
        time.sleep(5)
       
        #switching the tab to flipkart
        self.driver.execute_script("window.open('about:blank','secondtab');")
        self.driver.switch_to.window("secondtab")
    
        self.driver.get(self.url2)
        time.sleep(3)
        #seaching the input field and searching
        input=self.driver.find_element(by=By.XPATH,value='/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
        input.send_keys("Realme 4G 6GB RAM and 128 GB memory")
        search=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
        search.click()
        #realme2
        Realme2_name=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]')
        Realme2_price=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]')
        #data into text
        a2=Realme2_name.text
        b2=Realme2_price.text
        #appending to list
        mobile_name.append(a2)
        mobile_price.append(b2)
        time.sleep(2)
        print(a2)
        print(b2)
        clear_all=self.driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[3]/div/div[1]/div/div[1]/div/section[3]/div[2]/div[1]/div[1]/div[2]/span")
        clear_all.click()
        time.sleep(5)

        
        #iqoo
        input=self.driver.find_element(by=By.XPATH,value='/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
        input.send_keys("iqoo 4G 6GB RAM and 128 GB memory")
        search=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
        search.click()
        
        iqoo2_name=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]')
        iqoo2_price=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div')
        #time.sleep(5)
        c2=iqoo2_name.text
        d2=iqoo2_price.text
        mobile_name.append(c2)
        mobile_price.append(d2)
        time.sleep(2)
        print(c2)
        print(d2)
        time.sleep(2)
        #clearing the input field so that it can be checked for other brand
        input=self.driver.find_element(by=By.CSS_SELECTOR,value='._3704LK').clear()
        
        

        #oppo
        input=self.driver.find_element(by=By.XPATH,value='/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
        input.send_keys("oppo 4G 6GB RAM and 128 GB memory")
        search=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
        search.click()
        oppo2_name=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]')
        oppo2_price=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]')
        #time.sleep(5)
        e2=oppo2_name.text
        f2=oppo2_price.text
        mobile_name.append(e2)
        mobile_price.append(f2)
        time.sleep(2)
        print(e2)
        print(f2)
        time.sleep(2)
        input=self.driver.find_element(by=By.CSS_SELECTOR,value='._3704LK').clear()
        
        #oneplus
        input=self.driver.find_element(by=By.XPATH,value='/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
        input.send_keys("oneplus 4G 6GB RAM and 128 GB memory")
        search=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
        search.click()
        oneplus2_name=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]')
        oneplus2_price=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]')
        #time.sleep(5)
        g2=oppo2_name.text
        h2=oppo2_price.text
        mobile_name.append(g2)
        mobile_price.append(h2)
        time.sleep(2)
        print(g2)
        print(h2)
        time.sleep(2)
        #clearing the input field
        input=self.driver.find_element(by=By.CSS_SELECTOR,value='._3704LK').clear()
        
        #techno
        #searching the input field 
        input=self.driver.find_element(by=By.XPATH,value='/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
        input.send_keys("Techno 4G 6GB RAM and 128 GB memory")
        search=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
        search.click()
        #retrieving the info
        Techno2_name=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]')
        Techno2_price=self.driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]')
        #time.sleep(5)
        i2=Techno2_name.text
        j2=Techno2_price.text
        #appending to list
        mobile_name.append(i2)
        mobile_price.append(j2)
        time.sleep(2)
        print(i2)
        print(j2)
        time.sleep(2)
        #searching the input field and clearing it
        input=self.driver.find_element(by=By.CSS_SELECTOR,value='._3704LK').clear()
         
        #printing the list 
        print(mobile_name)
        print(mobile_price)

        finallist=zip(mobile_name,mobile_price)

        for data1 in list(finallist1):
            print(data1)
        #creating an excel file for mobile
        wb=self.Workbook()
        sh1.wb.active
        for z in list(finallist1):
            sh1.append(z)
        
        wb.save("FinalMobileNames.xlsx")

#creating an object for class
s=latish()
s.a_f_laptop()
s.a_f_mobile()


