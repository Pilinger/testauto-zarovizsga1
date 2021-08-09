import time
# preparing selenium and chrome web driver manager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# installing web driver manager and opening the page
URL = 'https://black-moss-0a0440e03.azurestaticapps.net/mm43.html'
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(URL)


# fill in the email, and submit
def filling_in_and_clicking(email):
    email_input.clear()
    time.sleep(0.5)
    email_input.send_keys(email)
    time.sleep(0.5)
    submit_button.click()
    time.sleep(0.5)


# checking the validation error if appears or not and with the message
def checking_validation(expected_result):
    validation_error = driver.find_elements_by_class_name('validation-error')
    if expected_result == 0:
        assert (len(validation_error) == 0)
    else:
        assert (validation_error[0].text == expected_result_list[expected_result])


# test data
email_list = ['teszt@elek.hu', 'teszt@', '']
expected_result_list = ['',
                        'Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes.',
                        'Kérjük, töltse ki ezt a mezőt.']

# gathering the input field, and submit button
email_input = driver.find_element_by_id('email')
submit_button = driver.find_element_by_id('submit')

# TC001 with valid teszt@elek.hu email
filling_in_and_clicking(email_list[0])
checking_validation(0)

# TC002 with invalid teszt@ email
filling_in_and_clicking(email_list[1])
checking_validation(1)

# TC003 with empty field
filling_in_and_clicking(email_list[2])
checking_validation(2)
