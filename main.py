from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a Chrome webdriver instance
driver = webdriver.Chrome()

# Open Cookie Clicker
driver.get("https://ozh.github.io/cookieclicker/")
time.sleep(5)
langSelect = driver.find_element(By.ID, "langSelect-EN")
langSelect.click()
time.sleep(1)
cookie = driver.find_element(By.ID, "bigCookie")
n = 0

try:
    cycle = 0
    while True:
        cycle += 1

        for _ in range(100 + n):
            cookie.click()

        shimmers = driver.find_elements(By.CLASS_NAME, "shimmer")
        for shimmers in reversed(shimmers):
            try:
                if shimmers.is_displayed():
                    shimmers.click()
            except:
                pass

        upgrades = driver.find_elements(By.CLASS_NAME, "upgrade")
        for upgrade in reversed(upgrades):
            try:
                upgrade.click()
            except:
                pass

        buildings = driver.find_elements(By.CLASS_NAME, "product")
        for building in reversed(buildings):
            try:
                building.click()
            except:
                pass
        n = n + 2
        print(f"Cycle {cycle} complete. Your cookies are accumulating rapidly.")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nBot stopped. Check your cookie count - it's probably ridiculous now.")
finally:
    driver.quit()