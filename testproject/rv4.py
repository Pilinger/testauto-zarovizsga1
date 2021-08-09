import time
# preparing selenium and chrome web driver manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# installing web driver manager and opening the page
URL = 'https://black-moss-0a0440e03.azurestaticapps.net/rv4.html'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)


# the full guessing method, reusable if page is refreshed
def guessing():
    time.sleep(2)
    # gathering the full cities, the possible cities, input, and button
    cities = driver.find_element_by_id('cites').text
    li_of_cities = driver.find_elements_by_tag_name('li')
    missing_city_input = driver.find_element_by_id('missingCity')
    submit_button = driver.find_element_by_id('submit')

    # generating the cities of the world list
    cities = cities.replace('"', '')
    cities_of_the_world_list = cities.split(', ')

    # generating the short list if cities
    short_list_of_cities = []
    for li in li_of_cities:
        short_list_of_cities.append(li.text)

    # getting the missing city
    missing_city = ''
    for city in cities_of_the_world_list:
        if city not in short_list_of_cities:
            missing_city = city

    # clearing the input and guessing the city
    missing_city_input.clear()
    time.sleep(0.5)
    missing_city_input.send_keys(missing_city)
    submit_button.click()
    time.sleep(0.5)

    # checking if the missing city is correct
    assert (driver.find_element_by_id('result').text == 'Eltaláltad.')


# calling the guessing function, callable if page is refreshed
guessing()
