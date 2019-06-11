from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.facebook.com")
driver.maximize_window()
driver.implicitly_wait(20)
driver.find_element_by_id("email").send_keys("selenium webdriver")
driver.find_element_by_name("pass").send_keys("python")
driver.find_element_by_id("loginbutton").click()
driver.get_screenshot_as_file("//Users//madhava//Desktop//selenium screenshot//screenshots//Facebook.png")
driver.quit()

