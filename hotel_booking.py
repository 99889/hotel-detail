from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    
    driver.get("https://www.booking.com")

    
    try:
        sign_in_popup = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[aria-label='Dismiss sign-in info.']"))
        )
        sign_in_popup.click()
    except Exception as e:
        print("No sign-in popup appeared or failed to close it:", e)

    
    search_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='ss']"))
    )

    
    search_input.clear()
    search_input.send_keys("New Delhi")

    
    location_suggestion = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "ul.c-autocomplete__list > li[data-i='0']"))
    )
    location_suggestion.click()

    
    check_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='date-display-field-start']"))
    )
    check_in_button.click()

    
    check_in_date = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "td[data-date='2024-07-15']"))  # Adjust the date as needed
    )
    check_in_date.click()

    
    check_out_date = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "td[data-date='2024-07-20']"))  # Adjust the date as needed
    )
    check_out_date.click()

    
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.sb-searchbox__button"))
    )
    search_button.click()

    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='property-card']"))
    )

    
    hotels = driver.find_elements(By.CSS_SELECTOR, "div[data-testid='property-card']")
    hotel_details = []

    for hotel in hotels:
        try:
            hotel_name = hotel.find_element(By.CSS_SELECTOR, "div[data-testid='title']").text
            hotel_address = hotel.find_element(By.CSS_SELECTOR, "span[data-testid='address']").text
            hotel_price = hotel.find_element(By.CSS_SELECTOR, "div[data-testid='price-and-discounted-price'] span").text
            hotel_details.append({
                "name": hotel_name,
                "address": hotel_address,
                "price": hotel_price
            })
        except Exception as e:
            print(f"Error extracting hotel details: {e}")
            continue

    # Print collected hotel details
    for detail in hotel_details:
        print(detail)

except Exception as e:
    print("An error occurred:", e)

finally:
    time.sleep(50)  
    driver.quit()
