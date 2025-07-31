from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def send_whatsapp(phone_number, message):
    options = Options()
    options.add_argument("--user-data-dir=/root/.config/google-chrome")  # Persistencia del QR
    driver = webdriver.Chrome(options=options)

    driver.get("https://web.whatsapp.com")
    input("Escanea el código QR y presiona Enter...")

    time.sleep(10)
    driver.get(f"https://wa.me/{phone_number}")
    time.sleep(5)

    try:
        driver.find_element(By.XPATH, '//a[contains(@href, "send")]').click()
        time.sleep(5)
        input_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"]')
        input_box.send_keys(message)
        time.sleep(1)
        input_box.send_keys("\n")
        time.sleep(5)
    except Exception as e:
        print("Error:", e)
    finally:
        driver.quit()
