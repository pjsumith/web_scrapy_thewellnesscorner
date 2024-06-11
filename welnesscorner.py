import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By

dirpath = os.getcwd()

chrome_driver_path = dirpath + r'/features/resources/drivers/chromedriver.exe'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(options=chrome_options)

f = open("D:\Automation-Frameworks_and_enhancements\Welness_corner\Welness_product.txt", "a", encoding="utf-8")
driver.get("https://www.thewellnesscorner.com/login")
time.sleep(2)

driver.find_element(By.XPATH,"//input[@placeholder='Email']").clear()
driver.find_element(By.XPATH,"//input[@placeholder='Email']").send_keys("deepika.g.solanki@accenture.com")
time.sleep(1)
driver.find_element(By.XPATH,"//button[@type='submit']").click()

time.sleep(2)

driver.find_element(By.XPATH,"//input[@type='password']").clear()
driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Deepu@05")
time.sleep(1)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(2)

for item in range(500,601):
    product_url = "https://www.thewellnesscorner.com/wellness-store/"+str(item)+"/products"
    driver.get(product_url)
    time.sleep(3)
    Category = driver.find_element(By.XPATH, "(//span[@class='ant-breadcrumb-link'])[3]").text
    f.write(f"{Category}, {product_url}\n")

f.close()
print("Successfully Scraped the Website")
