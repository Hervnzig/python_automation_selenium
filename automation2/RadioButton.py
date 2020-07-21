from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as E

exec_path = r"C:\Users\ALU\Desktop\selenium_python\drivers\geckodriver.exe"
URL = r"https://inderpsingh.blogspot.com/2013/04/SeleniumWebDriverQuiz4.html"
wait_time_out = 5
answer_1_radio_id_locator = "12"
answer1_name_locator = "answer1"

driver = webdriver.Firefox(executable_path=exec_path)
wait = W(driver, wait_time_out)
driver.get(URL)
radio_element = wait.until(E.presence_of_element_located((By.ID, answer_1_radio_id_locator)))
radio_element.click()
answer1_element = wait.until(E.presence_of_element_located((By.NAME, answer1_name_locator)))

# validation
if "Correct." in answer1_element.get_attribute("value"):
    print("Test verified true")
else:
    print("Test verified false !!!!")
