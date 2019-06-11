from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest

class Logintest(unittest.TestCase):
     @classmethod
     def setUpclass(cls):
          cls.driver = webdriver.Chrome(ChromeDriverManager().install())
          cls.driver.get("https://opensource-demo.orangehrmlive.com/")
          cls.driver.maximize_window()
          cls.driver.implicitly_wait(20)
     def test_login_valid(self):
          self.driver.find_element_by_id("txtUsername").send_keys("Admin")
          self.driver.find_element_by_id("txtPassword").send_keys("admin123")
          self.driver.find_element_by_id("btnLogin").click()
          self.driver.find_element_by_id("welcome").click()
          self.driver.find_element_by_link_text("Logout").click()
          time.sleep(2)
     @classmethod
     def tearDownClass(cls):
          cls.driver.close()
          cls.driver.quit()
          print("test completed")
if __name__ == '__main__':
     unittest.main()
