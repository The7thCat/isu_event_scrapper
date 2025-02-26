

def set_filter(driver, EC, By, WebDriverWait, sleep):

    try:
        #Select Eventbox
        event_box = driver.find_element(By.ID, value='isu-events')
        event_box.click()
        sleep(1)

        #Open Discipline
        discipline_arrow = driver.find_element(By.XPATH, value='//h3[contains(text(), "Discipline")]/following-sibling::div//span')
        discipline_arrow.click()
        sleep(1)

        #Select Discipline
        discipline_box = driver.find_element(By.ID, value="FIGURE SKATING-events")
        discipline_box.click()

        #Open Series Type
        series_arrow = driver.find_element(By.XPATH, value='//h3[contains(text(), "Series Type")]/following-sibling::div//span')
        series_arrow.click()
        sleep(1)

        #Select Series
        series_box = driver.find_element(By.ID, value='ISU Championships-events')
        #series_box = driver.find_element(By.CSS_SELECTOR, css_selector[0]) #temporary workaround
        series_box.click()
        sleep(1)

        #Apply Filter Button
        apply_filter_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@data-hover='Apply Filters']"))
        )
        driver.execute_script("arguments[0].click();", apply_filter_button)
        sleep(1)


    except Exception as e:

        print(f"Error: {e}")