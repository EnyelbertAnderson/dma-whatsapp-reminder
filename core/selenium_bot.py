from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def enviar_mensaje(numero, mensaje):
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.binary_location = "/usr/bin/chromium-browser"

    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=options)
    driver.get("https://web.whatsapp.com")

    input("Escanea el código QR y presiona ENTER...")

    url = f"https://web.whatsapp.com/send?phone={numero}&text={mensaje}"
    driver.get(url)
    time.sleep(10)

    try:
        boton_enviar = driver.find_element(By.XPATH, '//button[@data-testid="compose-btn-send"]')
        boton_enviar.click()
        print(f"✅ Mensaje enviado a {numero}")
    except Exception as e:
        print(f"❌ Error con {numero}: {e}")

    time.sleep(5)
    driver.quit()
