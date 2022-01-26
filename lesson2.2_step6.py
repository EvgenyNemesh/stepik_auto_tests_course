from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
   link = "http://SunInJuly.github.io/execute_script.html"
   browser = webdriver.Chrome()
   browser.get(link)

   x_element = browser.find_element_by_css_selector("#input_value")
   x = x_element.text
   y = calc(x)

   input1 = browser.find_element_by_css_selector("#answer")
   input1.send_keys(y)

   option1 = browser.find_element_by_css_selector("#robotCheckbox")
   option1.click()

   button = browser.find_element_by_css_selector("#robotsRule")
   browser.execute_script("return arguments[0].scrollIntoView(true);", button)
   button.click()

   button = browser.find_element_by_class_name("btn.btn-primary")
   button.click()

finally:
    time.sleep (10)
    browser.quit()