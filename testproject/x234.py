import time
# preparing selenium and chrome web driver manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

URL = 'https://black-moss-0a0440e03.azurestaticapps.net/x234.html'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)


# clearing fields, fill in, and submit
def fill_in_and_submit(a_value, b_value):
    a_input.clear()
    time.sleep(0.5)
    b_input.clear()
    time.sleep(0.5)
    a_input.send_keys(a_value)
    time.sleep(0.5)
    b_input.send_keys(b_value)
    time.sleep(0.5)
    submit_button.click()
    time.sleep(0.5)


# checking the result, gaining result_span each time to refresh value
def check_result(result_value):
    result_span = driver.find_element_by_id('result')
    assert (result_value == result_span.text)


# gathering a, b inputs, submit button
a_input = driver.find_element_by_id('a')
b_input = driver.find_element_by_id('b')
submit_button = driver.find_element_by_id('submit')

# test values for a, b, and expected result
a_list = ['99', 'kiskutya', '']
b_list = ['12', '12', '']
expected_result_list = ['222', 'NaN', 'NaN']

# TC001 checking with a = 99, b = 12
fill_in_and_submit(a_list[0], b_list[0])
check_result(expected_result_list[0])

# TC002 checking with a = kiskutya, b = 12
fill_in_and_submit(a_list[1], b_list[1])
check_result(expected_result_list[1])

# TC003 checking with a = '', b = ''
fill_in_and_submit(a_list[2], b_list[2])
check_result(expected_result_list[2])
