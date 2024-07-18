import requests
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configuration
tiktok_url = 'https://www.tiktok.com'
report_reason = 'Violation of community guidelines'
proxyscrape_url = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=all'

# Function to fetch proxies from ProxyScrape
def fetch_proxies():
    response = requests.get(proxyscrape_url)
    if response.status_code == 200:
        proxies = response.text.split('\n')
        return [proxy.strip() for proxy in proxies if proxy.strip()]
    else:
        print("Failed to fetch proxies")
        return []

# Function to set up Selenium WebDriver with proxy
def setup_webdriver(proxy):
    chrome_options = Options()
    chrome_options.add_argument(f'--proxy-server={proxy}')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

# Function to report a TikTok user
def report_user(driver, user_id):
    try:
        driver.get(f"{tiktok_url}/@{user_id}")
        time.sleep(5)  # Wait for the page to load

        # Click on the report button (this is an example, actual selector may vary)
        report_button = driver.find_element(By.XPATH, '//button[text()="Report"]')
        report_button.click()
        time.sleep(2)

        # Select the reason (actual selector may vary)
        reason_button = driver.find_element(By.XPATH, f'//button[text()="{report_reason}"]')
        reason_button.click()
        time.sleep(2)

        # Submit the report (actual selector may vary)
        submit_button = driver.find_element(By.XPATH, '//button[text()="Submit"]')
        submit_button.click()
        time.sleep(2)

        print(f"Reported user {user_id} successfully")
    except Exception as e:
        print(f"Failed to report user {user_id}: {e}")

# Main function
if __name__ == "__main__":
    user_id = '1234567890'  # Replace with the actual user ID

    proxies = fetch_proxies()
    if proxies:
        random.shuffle(proxies)  # Shuffle proxies to rotate through them

        for proxy in proxies:
            print(f"Using proxy: {proxy}")
            driver = setup_webdriver(proxy)

            report_user(driver, user_id)

            driver.quit()
            time.sleep(5)  # Sleep to avoid hitting rate limits

            # Add more logic for retries or handling multiple reports as needed
    else:
        print("No proxies available")
