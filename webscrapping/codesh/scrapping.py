from webscrapping import WebScrapping
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests

BASE_URL = "https://coodesh.com/vagas"

bot = WebScrapping(
        driver_path='/home/gvitor-s/Downloads/chromedriver',
        implicit_wait=10,
        )

bot.land_in_page(BASE_URL)
bot.scroll_site(sleep_time=0.5)
list_contents = bot.get_informations(
        find_by=By.CSS_SELECTOR,
        value='div[class="space-2 container"] > a'
        )

links = bot.get_info_by_attribute(
        selenium_element=list_contents,
        attribute='href'
        )

body_list = [requests.get(link).content for link in links]

soup = BeautifulSoup(
        markup=body_list[0],
        features='html.parser'
        )
