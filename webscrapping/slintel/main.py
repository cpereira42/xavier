import pandas as pd
import requests
from bs4 import BeautifulSoup

def get_links(soup: BeautifulSoup):
    box = soup.select_one('div[class="row show_intial_data_subcall"]')
    links = box.find_all('a')
    links = [link['href'] for link in links]
    return links

def match_web(links: list, website: str):
    found = False
    for link in links:
        request = requests.get(f'https://www.slintel.com/{link}')
        if (request.status_code != 200):
            continue
        soup = BeautifulSoup(request.content, 'html.parser')
        website2 = soup.select_one('p[class="sl_subHeader hover_"]')
        if (website2.text.strip() == website):
            found = True
            break
    if found == True:
        return soup
    return ''

def get_stacks(soup: BeautifulSoup, website: str):
    links = get_links(soup)
    if links == []:
        return links
    match = match_web(links, website)
    if match == '':
        return []
    stacks = match.select_one('div[class="teck_stack_section st-48"]')
    stacks = stacks.select('div[class="media-body"]')
    stacks = [stack.a.text.strip() for stack in stacks]
    return stacks

def format_website(website: str)-> str:
    website = website.strip()
    website = website.replace('www.', '')
    website = website.replace('https://', '')
    website = website.replace('http://', '')
    if website[-1] == '/':
        website = website[:-1]
    return website

df = pd.read_parquet('../data_files/startup.parquet')
df['name'] = df['name'].str.lower()

data = list()

for i in range(len(df['name'])):
    name = df['name'][i]
    website = format_website(df['website'][i])
    print(name, website)
    soup = requests.get(f'https://www.slintel.com/directory/company?searchTerm={name})').content
    soup = BeautifulSoup(soup, 'html.parser')
    stacks = get_stacks(soup, website)
    data.append([name, stacks])


df = pd.DataFrame(
    data,
    columns=[
            'name', 'stacks'])

df.to_parquet('../data_files/slintel.parquet')

print(df)
