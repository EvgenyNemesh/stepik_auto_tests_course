from selenium import webdriver
import time

#Ссылка №2 "https://suninjuly.github.io/registration2.html" 

try: 
    link = "https://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)


    first_name = browser.find_element_by_css_selector(".first_block .form-control.first")
    first_name.send_keys("tra-ta-ta")
    
    last_name = browser.find_element_by_css_selector(".first_block .form-control.second")
    last_name.send_keys("tra-ta-ta")
    
    email = browser.find_element_by_css_selector(".first_block .form-control.third")
    email.send_keys("tra-ta-ta")
 

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
