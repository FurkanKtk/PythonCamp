from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec 

class Test_day5:
    def _init_(self):
        self.driver = driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

    def teardown_method(self):
        self.driver.quit()

    def empty_username_password(self):
        WebDriverWait(self.driver,5).until()(ec.visibility_of_element_located((By.ID,"user-name")))
        userNameInput=self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until()(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput=self.driver.find_element(By.ID,"password")
        userNameInput.send_keys("")
        passwordInput.send_keys("")
        loginBtn=self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        
        errorMassage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
        assert errorMassage.text== "Username is required"




    def empty_password(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        userNameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(2)
        userNameInput.send_keys("xxx")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn=driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
      
        errorMassage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
        print(errorMassage)
        testResult=errorMassage.text=="Password is required"
        print(f"TEST SONUCU: {testResult}")





    def locked_out(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        userNameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(2)
        userNameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn=driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
       
        errorMassage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        print(errorMassage)
        testResult=errorMassage.text=="Sorry, this user has been locked out."
        print(f"TEST SONUCU: {testResult}")



    def page(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        userNameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(2)
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn=driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        driver.get("https://www.saucedemo.com/inventory.html")
        sleep(5)



    def number_of_products(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        userNameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(2)
        userNameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn=driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        driver.get("https://www.saucedemo.com/inventory.html")
        sleep(5)
        products=driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Sitedeki toplam ürün sayısı: {len(products)}")




    def error_with_X(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        userNameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        sleep(2)
        userNameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)
        loginBtn=driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        sleep(5)
        closeBtn=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        sleep(2)
        closeBtn.click()
        sleep(30)
        
# testClass = Test_Sauce()
# testClass.empty_username_password()
# testClass.empty_password()
# testClass.locked_out()
# testClass.number_of_products()
# testClass.page()

# testClass.error_with_X()