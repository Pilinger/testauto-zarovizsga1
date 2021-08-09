import time
# preparing selenium and chrome web driver manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# installing web driver manager and opening the page
URL = 'https://black-moss-0a0440e03.azurestaticapps.net/tts4.html'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)

# test data
count_of_trys = 100
minimum_fej_results = 30

# gathering the lastResult, result, and button
last_result = driver.find_element_by_id('lastResult')
submit_button = driver.find_element_by_id('submit')

# getting the 100 trys
for _ in range(count_of_trys):
    submit_button.click()
    time.sleep(0.1)

# gathering li-s and assigning a list of 'fej'
li_fej = driver.find_elements_by_xpath('//li')
fej_list = []
for li in li_fej:
    if li.text == 'fej':
        fej_list.append('fej')

# checkcing the count of 'fej'-s against minimum_fej_results
assert (len(fej_list) >= minimum_fej_results)
