from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E
import time

# exec_path = r"C:\Users\ALU\Desktop\selenium_python\drivers\geckodriver.exe"
exec_path = r"C:\Users\ALU\Desktop\selenium_python\drivers\chromedriver.exe"
URL = r"https://www.wikipedia.org/"
language_locators = ["js-link-box-en", "js-link-box-fr", "js-link-box-ja", "js-link-box-de"]
search_locator = "searchInput"
search_text = "language"
wait_time = 5


# driver = webdriver.Firefox(executable_path=exec_path)
driver = webdriver.Chrome(executable_path=exec_path)
driver.get(URL)
wait = W(driver, wait_time)
# driver.implicitly_wait(5)
driver.maximize_window()

for i in range(len(language_locators)):
    # language_link = driver.find_element(By.ID, language_locators[i])

    language_link = wait.until(E.presence_of_element_located((By.ID, language_locators[i])))
    language_link.click()

    # input_box_element = driver.find_element(By.ID, search_locator)
    input_box_element = wait.until(E.presence_of_element_located((By.ID, search_locator)))

    input_box_element.send_keys(search_text)
    input_box_element.submit()

    time.sleep(5)
    driver.back()
    driver.back()

# driver.quit()