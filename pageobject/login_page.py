from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
   def __init__(self,driver):
       self.driver = driver
       self.wait = WebDriverWait(driver, 10)
       self.username=(By.XPATH, "//input[@type='text']")
       self.password=(By.XPATH, "//input[@type='password']")
       self.signin=(By.XPATH, "//button[text()='Sign in']")



   def login(self,username,password):
        # wait until username field is visible
        self.wait.until(EC.visibility_of_element_located(self.username)).send_keys(username)
        # wait until password field is visible
        self.wait.until(EC.visibility_of_element_located(self.password)).send_keys(password)
        # wait until signin buttons is clickable
        self.wait.until(EC.element_to_be_clickable(self.signin)).click()


   def is_login_page_displayed(self):
       try:
           self.wait.until(EC.visibility_of_element_located(self.signin))
           return True
       except:
           return False