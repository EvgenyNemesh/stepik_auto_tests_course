from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math
import time

def sum(x, y):
  return int(int(x) + int(y))
try:
   link = "http://suninjuly.github.io/selects1.html"
   browser = webdriver.Chrome()
   browser.get(link)

   x_element = browser.find_element_by_id("num1")
   x = x_element.text

   y_element = browser.find_element_by_id("num2")
   y = y_element.text

   z = sum(x, y)

   select = Select(browser.find_element_by_tag_name("select"))
   select.select_by_value(str(z)) # ищем элемент со значением переменной "z"

   button = browser.find_element_by_class_name("btn.btn-default")
   button.click()

finally:
    time.sleep (10)
    browser.quit()