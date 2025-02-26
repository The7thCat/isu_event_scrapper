list_of_event_data = []

def read_events(driver, EC, By, WebDriverWait):

    WebDriverWait(driver, 3).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "event-card-content"))
    )
    content_cards = driver.find_elements(By.CLASS_NAME, "event-card-content")
    for card in content_cards:
        try:

            event_date = card.find_element(By.XPATH, './/h5[contains(@class, "fluid-text-sm") and contains(@class, "text-themegray")]').text
            event_name = card.find_element(By.XPATH, './/h3[contains(@class, "text-xl") and contains(@class, "font-bold")]').text
            event_location = card.find_element(By.XPATH, './/span[contains(@class, "text-xs") and contains(@class, "font-medium")]').text

            event_data = {
                'event_date': event_date,
                'event_name': event_name,
                'event_location': event_location,
            }
            list_of_event_data.append(event_data)

        except Exception as e:
            print(f"Error extracting data from event card: {e}")

    return list_of_event_data
