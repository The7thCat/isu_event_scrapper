from read_events import *

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

# Iteration through months
def iterate_month(driver, EC, By, WebDriverWait, sleep):
    with open("error_log.txt", 'w') as error_log:
        list_of_events = []
        for month in MONTHS:
            xpath = f"//div[contains(text(),'{month}')]"

            try:

                month_element = driver.find_element(By.XPATH, value=xpath)

                # using JS
                driver.execute_script("arguments[0].scrollIntoView(true);", month_element)
                sleep(1)
                driver.execute_script("arguments[0].click();", month_element)
                sleep(1)
                events_for_month = read_events(driver, EC, By, WebDriverWait)
                for _ in events_for_month:
                    list_of_events.append(_)

            except Exception as e:
                error_log.write(f"could not click {month}: or extract events: {str(e)}\n")
        return list_of_events