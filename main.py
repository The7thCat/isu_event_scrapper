from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from set_filter import set_filter
from iterate_month import *
from sort_event_list import *
from write_event_file import *

#avoid browser being closed immediately
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.isu.org/events/")

# run code
def isu_scrapper():
    try:
        set_filter(driver, EC, By, WebDriverWait, sleep)
        write_event_file(sort_event_list(iterate_month(driver, EC, By, WebDriverWait, sleep)))

    except Exception as e:
        print(f"Error in main: {e}")

    finally:
        driver.quit()

isu_scrapper()