from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

treasure_img = browser.find_element_by_id("treasure")
x_element = treasure_img.get_attribute("valuex")
x = x_element
y = calc(x)

input1 = browser.find_element_by_css_selector("#answer")
input1.send_keys(y)

option1 = browser.find_element_by_css_selector("#robotCheckbox")
option1.click()

option2 = browser.find_element_by_css_selector("#robotsRule")
option2.click()

button = browser.find_element_by_class_name("btn.btn-default")
button.click()


time.sleep(10)

browser.quit()