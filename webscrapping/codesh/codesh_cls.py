from bs4 import BeautifulSoup
import re
BASE_URL = "https://coodesh.com"


class Codesh:
    @staticmethod
    def get_company_name(soup: BeautifulSoup) -> str:
        return soup.select_one(
                selector='span[class="link-muted"]'
                ).text

    @staticmethod
    def get_company_location(soup: BeautifulSoup) -> str:
        return soup.select_one(
                selector='#content > div:nth-child(2) >\
                        div > div > div.col-lg-4 > div >\
                        div.jsx-3539478241.mb-7 > address > span:nth-child(1)'
                ).text

    @staticmethod
    def get_company_stacks(soup: BeautifulSoup) -> list:
        html_stacks = soup.select_one(
                selector='#content > div:nth-child(2) >\
                        div > div > div.mb-9.mb-lg-0.col-lg-8 >\
                        div > div:nth-child(4) > ul'
                ).find_all(
                        name='li'
                        )
        return [stack.text for stack in html_stacks]

    @staticmethod
    def get_company_link_to_perfil(soup: BeautifulSoup):
        return soup.select_one(
                selector='#content > div:nth-child(1) > div > div >\
        div.media-body > div > div.mb-3.mb-lg-0.col-lg-7 > div > ul > li > a'
                )
        # name = re.sub('[^a-zA-Z ]', '',
        #               name.encode().decode('utf-8'))
        # name = name.replace(' ', '-')
        # return f'{BASE_URL}/empresas/{name.lower()}'
