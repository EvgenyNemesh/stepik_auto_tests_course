from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
   link = "http://suninjuly.github.io/redirect_accept.html"
   browser = webdriver.Chrome()
   browser.get(link)

   button = browser.find_element_by_class_name("btn.trollface.btn-primary")
   button.click()

   new_window = browser.window_handles[1]
   browser.switch_to.window(new_window)

   x_element = browser.find_element_by_css_selector("#input_value")
   x = x_element.text
   y = calc(x)

   input1 = browser.find_element_by_css_selector("#answer")
   input1.send_keys(y)

   button = browser.find_element_by_class_name("btn.btn-primary")
   button.click()

finally:
    time.sleep (10)
    browser.quit()