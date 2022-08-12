from urllib.parse import quote_plus

from selenium import webdriver
from selenium.webdriver.common.by import By

init_url = "https://www.google.com/search?q="
search_term = input("Search: ")
url = init_url + quote_plus(search_term)

driver = webdriver.Chrome()
driver.get(url)

for x in driver.find_elements(By.CLASS_NAME, "yuRUbf"):
    aTag = x.find_element(By.TAG_NAME, "a")
    aH3 = x.find_element(By.TAG_NAME, "h3")
    href = aTag.get_attribute("href")
    print("제목: ", aH3.text)
    print("링크: ", href)
