import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


driver = webdriver.Firefox()

@allure.feature('Функциональное тестирование')
@allure.story('Ввод суммы для конвертации, получение результата, проверка того, что использовалась    введенная нами сумма')
class TestCalculatorMoneyCurrency:
    @allure.step('Запуск браузера Chrome, открытие и загрузка страницы с кальулятором.')
    def setup_method(self, method):

        """
        Открытие браузера Chrome v. 55.0.2883.87 m (64-bit)
        Загрузка калькулятора иностранных валют
        Проверка работоспособности поля ввода суммы и кнопки "Показать" для получения резульатата
        """

        driver.maximize_window()
        driver.get('http://www.sberbank.ru/ru/quotes/converter')
        assert 'Калькулятор иностранных валют' in driver.title
        driver.implicitly_wait(15)

    @allure.step('Возврат в исходное состояние, закрытие браузера.')
    def teardown_method(self, method):

        """
        Закрытие браузера
        """

        driver.quit()

    @allure.step('Ввод валидных данных в поле ввода суммы и проверка результата.')
    def test_input_amount(self):

            amount = ['1', '1 250', '999 999 999 999', '3 600,57', '666 745,95'] #список валидных вводных данных (с пробелами, чтобы проще было сравнить потом с результатом, который тоже выводится с пробелами)
            input_amount_field = driver.find_element_by_xpath("//input[@data-reactid='.0.$1.$0.0.1.0.0.0']") #находим поле для ввода суммы для конвертации
            input_amount_field.click() #кликаем по полю для ввода суммы

            for option in amount: #перебираем варианты вводимых данных
                input_amount_field.clear() #очищаем поле
                input_amount_field.send_keys(option) #вводим значения по очереди из списка правильных вариантов
                button_convert = driver.find_element_by_xpath("//button[@data-reactid='.0.$1.$0.6.0']").click() #клик по кнопке "Показать" конвертера

                with allure.step('При вводе валидных данных появляется результат конвертации'):
                    assert driver.find_element_by_xpath("//div[@class='converter-result' and @data-reactid='.0.$1.$1']"), 'Конвертация не осуществлена.' #подтверждаем, что появился блок с результатом конвертации

                    time.sleep(1)
                    num1 = driver.find_element_by_xpath("//span[@data-reactid='.0.$1.$1.1.0']").text #сумма 1 (отображается в результатах)
                    val1 = driver.find_element_by_xpath("//span[@data-reactid='.0.$1.$1.1.1']").text #валюта 1 (отображается в результатах)
                    #option = option + ',00' #добавляем десятичную часть, чтобы можно было сравнить с выводимым текстовым результатом (убеждаемся, что это не сумма по умолчанию)
                    if ',' not in option: #если нет дробной части в варианте (точки), то добавляем ее, чтобы можно было сравнить с информацией в результате
                        option = option + ',00'

                    with allure.step('Сравниваем введенную сумму с отображаемой в резульате'):
                        assert option == num1, 'Суммы не совпадают.'
