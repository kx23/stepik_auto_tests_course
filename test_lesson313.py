import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestSelenium(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CLASS_NAME, "first_class").find_element(
            By.CSS_SELECTOR, "input[required]"
        )

        input1.send_keys("Ivan")
        input2 = browser.find_element(
            By.XPATH, '//div[contains(@class,"second_class")]/input[@required]'
        )

        input2.send_keys("Petrov")
        input3 = browser.find_element(
            By.CSS_SELECTOR, "div.third_class input[required]"
        )

        input3.send_keys("Smolensk")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта

        self.assertEqual(
            "Congratulations! You have successfully registered!",
            welcome_text,
            "Welcome text is incorrect",
        )

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.CLASS_NAME, "first_class").find_element(
            By.CSS_SELECTOR, "input[required]"
        )

        input1.send_keys("Ivan")
        input2 = browser.find_element(
            By.XPATH, '//div[contains(@class,"second_class")]/input[@required]'
        )

        input2.send_keys("Petrov")
        input3 = browser.find_element(
            By.CSS_SELECTOR, "div.third_class input[required]"
        )

        input3.send_keys("Smolensk")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(
            "Congratulations! You have successfully registered!",
            welcome_text,
            "Welcome text is incorrect",
        )


if __name__ == "__main__":
    unittest.main()
