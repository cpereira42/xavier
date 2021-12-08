from dotenv import load_dotenv
import test_class
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

load_dotenv(dotenv_path='../login.env')


def tester(estados: list, mercados: list, stacks: list, name: str):
    with test_class.TestSelenium() as bot:
        bot.get("http://localhost:8000")
        estados_box = bot.find_element(By.ID, "txt_estados")
        stack_box = bot.find_element(By.ID, "txt_stacks")
        mercado_box = bot.find_element(By.ID, "txt_mercados")
        for estado in estados:
            estados_box.send_keys(estado)
            bot.find_element(By.ID, "add_estado").click()
        for mercado in mercados:
            mercado_box.send_keys(mercado)
            bot.find_element(By.ID, "add_mercado").click()
        for stack in stacks:
            stack_box.send_keys(stack)
            bot.find_element(By.ID, "add_stack").click()

        csv_name = bot.find_element(By.ID, "file_name")
        csv_name.send_keys(name, Keys.ENTER)

        bot.find_element(By.ID, "submit").click()
        time.sleep(2)
