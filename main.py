import time
import csv 

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

START_URL = 'https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'
service = Service(executable_path='./chromedriver.exe')
driver = webdriver.Chrome(service=service)
browser = webdriver.Chrome('chromedriver')
browser.get(START_URL)

time.sleep(10)

