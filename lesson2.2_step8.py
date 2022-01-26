from selenium import webdriver
import time
import os

try:
   link = "http://suninjuly.github.io/file_input.html"
   browser = webdriver.Chrome()
   browser.get(link)

   input1 = browser.find_element_by_name("firstname")
   input1.send_keys("Jeka")

   input1 = browser.find_element_by_name("lastname")
   input1.send_keys("Nemesh")

   input1 = browser.find_element_by_name("email")
   input1.send_keys("Alexeevich")

   current_dir = os.path.abspath(os.path.dirname(__file__))
   file_name = "xxx.txt"
   file_path = os.path.join(current_dir, file_name)
   element = browser.find_element_by_id("file")
   element.send_keys(file_path)

   button = browser.find_element_by_class_name("btn.btn-primary")
   button.click()
finally:
    time.sleep (10)
    browser.quit()