from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
   link = "http://suninjuly.github.io/explicit_wait2.html"
   browser = webdriver.Chrome()
   browser.get(link)

   button = WebDriverWait(browser, 12).until(
       EC.text_to_be_present_in_element((By.ID, "price"), "100")
   )

   button1 = browser.find_element_by_class_name("btn.btn-primary")
   browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
   button1.click()

   x_element = browser.find_element_by_css_selector("#input_value")
   x = x_element.text
   y = calc(x)

   input1 = browser.find_element_by_css_selector("#answer")
   input1.send_keys(y)

   button2 = browser.find_element_by_id("solve")
   browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
   button2.click()

finally:
    time.sleep (10)
    browser.quit()
