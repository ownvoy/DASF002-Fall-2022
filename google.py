from urllib.parse import quote_plus
from search.models import Data
from selenium import webdriver
from selenium.webdriver.common.by import By

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DASF002.settings")

import django
django.setup()

class Chrome:
    def googleCrawling(search_term):
        init_url = "https://www.google.com/search?q="
        url = init_url + quote_plus(search_term)

        driver = webdriver.Chrome()
        driver.get(url)
        data = []
        count = 0

        for x in driver.find_elements(By.CLASS_NAME, "yuRUbf"):
            atag = x.find_element(By.TAG_NAME, "a")
            h3 = x.find_element(By.TAG_NAME, "h3")
            href = atag.get_attribute("href")
            discription = "asfdasf"
            data.append([h3.text, href,discription])
            count += 1
            if count == 5:
                break
        return data

