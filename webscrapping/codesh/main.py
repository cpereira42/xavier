from selenium_bot import Codesh
from beautiful_bot import get_perfil_infos, get_cidade_second_page
import json


BASE_URL = "https://coodesh.com/vagas"


bot = Codesh(
    driver_path=':/home/ferrari/SeleniumDrivers',
    implicit_wait=10,
)
bot.land_in_page(BASE_URL)
bot.scroll_site(sleep_time=1)
companies = bot.get_first_page_infos()

get_perfil_infos(companies)
get_cidade_second_page(companies)
print(json.dumps(companies, indent=4, sort_keys=True))
