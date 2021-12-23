from requests.api import request
from codesh_bot import WebScrapping
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import json
BASE_URL = "https://coodesh.com/vagas"

def get_body_html(perfil_url: str):
    response = requests.get(perfil_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def get_perfil_infos(companies: dict):
    for company in companies:
        soup = get_body_html(companies[company]['perfil'])
    print(soup)


bot = WebScrapping(
	driver_path=':/home/luigi/se_drivers',
	implicit_wait=10,
	)
    
bot.land_in_page(BASE_URL)
bot.scroll_site(sleep_time=1)
companies = bot.get_first_page_infos()

get_perfil_infos(companies)

    # links = bot.get_info_by_attribute(
#         selenium_element=list_contents,
#         attribute='href'
#         )

# body_list = [requests.get(link).content for link in links]

# soup = BeautifulSoup(
#         markup=body_list[0],
#         features='html.parser'
#         )

# print(Codesh.get_company_link_profile(bot, links[0]))
# for i in body_list:
#     soup = BeautifulSoup(
#             markup=i,
#             features='html.parser'
#             )
#     bot.land_in_page(Codesh.get_company_link_to_perfil(
#         Codesh.get_company_name(soup)))
#     sleep(1.2)
