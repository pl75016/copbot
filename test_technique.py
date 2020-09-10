import selenium
from selenium import webdriver

PATH = "/Users/pierre-louisbarbier/Desktop/copbot/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get('https://www.solebox.com/en_FR/login')

email_box = driver.find_element_by_name('dwfrm_profile_customer_email')

password_box = driver.find_element_by_name('dwfrm_profile_login_password')

email_box.send_keys('mails@gmail.com')

password_box.send_keys('password')

login_button = driver.find_element_by_type('submit')

login_button.click()