from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#вільний лайф
def VilLife():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver_path = "шлях_до_файлу_драйвера_chrome"

    driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

    url = "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/"
    driver.get(url)

    driver.implicitly_wait(5)

    tariff_name_element = driver.find_element(By.XPATH, '//a[contains(text(), "Вільний Лайф")]')
    tariff_name = tariff_name_element.text.strip()

    print(tariff_name)
    driver.quit()


#Смарт Лайф
def SmartLayfLife():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver_path = "шлях_до_файлу_драйвера_chrome"

    driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

    url = "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/"
    driver.get(url)

    driver.implicitly_wait(5)

    tariff_name_element = driver.find_element(By.XPATH, '//a[contains(text(), "Смарт Лайф")]')
    tariff_name = tariff_name_element.text.strip()

    print(tariff_name)
    driver.quit()



# Просто Лайф
def ProstoLife():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver_path = "шлях_до_файлу_драйвера_chrome"

    driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

    url = "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/"
    driver.get(url)

    driver.implicitly_wait(5)

    tariff_name_element = driver.find_element(By.XPATH, '//a[contains(., "Просто Лайф")]')
    tariff_name = tariff_name_element.text.strip()

    print(tariff_name)
    driver.quit()



#PlatinumLife
def PlatinumLife():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver_path = "шлях_до_файлу_драйвера_chrome"

    driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

    url = "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/"
    driver.get(url)

    driver.implicitly_wait(5)

    tariff_name_element = driver.find_element(By.XPATH, '//a[contains(text(), "Platinum Лайф")]')
    tariff_name = tariff_name_element.text.strip()

    print(tariff_name)
    driver.quit()


#Шкільний Лайф
def SchollLife():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver_path = "шлях_до_файлу_драйвера_chrome"

    driver = webdriver.Chrome(service=Service(driver_path), options=chrome_options)

    url = "https://www.lifecell.ua/uk/mobilnij-zvyazok/taryfy/"
    driver.get(url)

    driver.implicitly_wait(5)

    tariff_name_element = driver.find_element(By.XPATH, '//a[contains(text(), "Шкільний Лайф")]')
    tariff_name = tariff_name_element.text.strip()

    print(tariff_name)
    driver.quit()


ProstoLife()
SmartLayfLife()
VilLife()
PlatinumLife()
SchollLife()
