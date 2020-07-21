from selenium import webdriver
from selenium.webdriver.common.by import By

exec_path = r"C:\Users\ALU\Desktop\selenium_python\drivers\chromedriver.exe"
# exec_path = r"C:\Users\ALU\Desktop\selenium_python\drivers\geckodriver.exe"
URL = r"https://www.wikipedia.org/"
english_link_locator = "js-link-box-en"
search_locator = "searchInput"
search_text = "Kigali city"


# driver = webdriver.Firefox(executable_path=exec_path)
driver = webdriver.Chrome(executable_path=exec_path)
driver.get(URL)
driver.maximize_window()
english_link_element = driver.find_element(By.ID, english_link_locator)
english_link_element.click()
input_box_element = driver.find_element(By.ID, search_locator)
input_box_element.send_keys(search_text)
input_box_element.submit()
driver.quit()