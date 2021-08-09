import time
# preparing selenium and chrome web driver manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# installing web driver manager and opening the page
URL = 'https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)


def the_whole_checking_function():
    # calculating the result
    def calculating_result(n1, n2, operator):
        if operator == '*':
            return n1 * n2
        elif operator == '+':
            return n1 + n2
        elif operator == '-':
            return n1 - n2

    # getting the result on the page
    def result_on_the_page():
        return int(driver.find_element_by_id('result').text)

    # gathering the numbers, operator, and submit button
    num1 = int(driver.find_element_by_id('num1').text)
    num2 = int(driver.find_element_by_id('num2').text)
    op = driver.find_element_by_id('op').text
    submit_button = driver.find_element_by_id('submit')

    # clicking on submit_button, and checking the result
    submit_button.click()
    assert (calculating_result(num1, num2, op) == result_on_the_page())


# evoking the_whole_checking_function, callable if page is refreshed multiple times
the_whole_checking_function()
