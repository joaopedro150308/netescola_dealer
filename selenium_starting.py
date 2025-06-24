from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chorme_arguments = ['--window-size=1000,640', '--incognito']

for argument in chorme_arguments:
    chrome_options.add_argument(argument)

wait_errors = [NoSuchElementException, ElementNotInteractableException, ElementNotSelectableException, NoSuchElementException]

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver,40,1, ignored_exceptions=wait_errors)