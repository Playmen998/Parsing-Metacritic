import time
import pandas as pd
import numpy as np
from tqdm import tqdm
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import csv
import re
from selenium.webdriver.chrome.service import Service




def search_woking_link(game, platform,driver):
    "Ищем страницу с нужной игрой и платформой"
    url = "https://www.metacritic.com/search/game/results?search_type=advanced"
    driver.get(url)
    WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.ID, "primary_search_box")))
    enter = driver.find_element("css selector", "#primary_search_box")
    enter.clear()
    enter.send_keys(game)
    element = WebDriverWait(driver, 5).until(ec.element_to_be_clickable(("css selector",
                                                                         "#primary_menu_item_enter_search > span")))
    element.click()
    element = WebDriverWait(driver, 5).until(ec.element_to_be_clickable(("css selector",
                                                                         "#main_content > div > div.search_filters_nav.fxdcol.gu3 > div > div:nth-child(3) > a > span.title")))
    element.click()
    WebDriverWait(driver, 5).until(ec.presence_of_element_located(("css selector",
                                                                   "#main_content > div > div.search_filters_nav.fxdcol.gu3 > div > div.adv_filters_dialog > div:nth-child(2) > div:nth-child(22) > a > span")))
    "Ищем нужную платформу"
    if platform == "PS4":
        driver.find_element("css selector",
                            '#main_content > div > div.search_filters_nav.fxdcol.gu3 > div > div.adv_filters_dialog > div:nth-child(2) > div:nth-child(3) > a > span').click()
    elif platform == "PS3":
        driver.find_element("css selector",
                            '#main_content > div > div.search_filters_nav.fxdcol.gu3 > div > div.adv_filters_dialog > div:nth-child(2) > div:nth-child(4) > a > span').click()
    elif platform == "XOne":
        driver.find_element("css selector",
                            '#main_content > div > div.search_filters_nav.fxdcol.gu3 > div > div.adv_filters_dialog > div:nth-child(2) > div:nth-child(5) > a > span').click()
    elif platform == "X360":
        driver.find_element("css selector",
                            '#main_content > div > div.search_filters_nav.fxdcol.gu3 > div > div.adv_filters_dialog > div:nth-child(2) > div:nth-child(6) > a > span').click()
    elif platform == "PC":
        driver.find_element("css selector",
                            '#main_content > div > div.search_filters_nav.fxdcol.gu3 > div > div.adv_filters_dialog > div:nth-child(2) > div:nth-child(7) > a > span').click()
    elif platform == "DS":
        driver.find_element("css selector",
                            '#main_content > div > div.search_filters_nav.fxdcol.gu3 > div > div.adv_filters_dialog > div:nth-child(2) > div:nth-child(8) > a > span').click()
    elif platform == "3DS":
        driver.find_element("css selector",
                            '#main_content > div > div.search_filters_nav.fxdcol.gu3 > div > div.adv_filters_dialog > div:nth-child(2) > div:nth-child(9) > a > span').click()
    elif platform == "PSV":
        driver.find_element("css selector",
                            '#main_content > div > div.search_filters_nav.fxdcol.gu3 > div > div.adv_filters_dialog > div:nth-child(2) > div:nth-child(10) > a > span').click()
    elif platform == "PSP":
        driver.find_element("css selector",
                            '#main_content > div > div.search_filters_nav.fxdcol.gu3 > div > div.adv_filters_dialog > div:nth-child(2) > div:nth-child(11) > a > span').click()
    elif platform == "Wii":
        driver.find_element("css selector",
                            '#main_content > div > div.search_filters_nav.fxdcol.gu3 > div > div.adv_filters_dialog > div:nth-child(2) > div:nth-child(12) > a > span').click()
    elif platform == "PS2":
        driver.find_element("css selector",
                            '#main_content > div > div.search_filters_nav.fxdcol.gu3 > div > div.adv_filters_dialog > div:nth-child(2) > div:nth-child(15) > a > span').click()
    elif platform == "PS":
        driver.find_element("css selector",
                            '#main_content > div > div.search_filters_nav.fxdcol.gu3 > div > div.adv_filters_dialog > div:nth-child(2) > div:nth-child(16) > a > span').click()
    elif (platform == "GBA" or platform == "GB"):
        driver.find_element("css selector",
                            '#main_content > div > div.search_filters_nav.fxdcol.gu3 > div > div.adv_filters_dialog > div:nth-child(2) > div:nth-child(17) > a > span').click()
    elif platform == "XB":
        driver.find_element("css selector",
                            '#main_content > div > div.search_filters_nav.fxdcol.gu3 > div > div.adv_filters_dialog > div:nth-child(2) > div:nth-child(19) > a > span').click()
    elif platform == "GC":
        driver.find_element("css selector",
                            '#main_content > div > div.search_filters_nav.fxdcol.gu3 > div > div.adv_filters_dialog > div:nth-child(2) > div:nth-child(20) > a > span').click()
    elif platform == "N64":
        driver.find_element("css selector",
                            '#main_content > div > div.search_filters_nav.fxdcol.gu3 > div > div.adv_filters_dialog > div:nth-child(2) > div:nth-child(21) > a > span').click()
    elif platform == "DC":
        driver.find_element("css selector",
                            '#main_content > div > div.search_filters_nav.fxdcol.gu3 > div > div.adv_filters_dialog > div:nth-child(2) > div:nth-child(22) > a > span').click()
    else:
        return None, url
    url = driver.current_url # сохраняем ссылку
    soup = BeautifulSoup(driver.page_source, "html.parser") # сохраняем html страницы
    body = soup.find("div", class_ = "body")
    if body.text.strip() == "Enter your search term in the search bar above.":
        return None, url
    else:
        return soup, url

def search_gamename_rating(soup):
    "Ищем все названия игр на данной странице сайта"
    dict = {}
    class_games = soup.find_all("h3",class_="product_title basic_stat")
    for class_game in class_games:
        text = class_game.text.strip()
        href ="https://www.metacritic.com" + class_game.find('a').get('href')
        dict[text] = href
    return dict

def search_all_info(game,game_names,driver):
    "Поиск Metascore, User Score, Год "
    start_time = time.time()
    name_game = game[0]
    platform = game[1]
    index = game_names.index(game)
    print("Игра:",name_game, "Платформа:", platform)
    exit = [] #спользуем для выхода из цикла
    games_score = []
    soup, url = search_woking_link(name_game, platform,driver)
    if soup != None:
        try:
            max_page = int(soup.find("li", class_="page last_page").find("a", class_="page_num").text.strip())
        except:
            max_page = 1
        for i in range(max_page): # проходимся по каждой странице
            dict_onerequest = search_gamename_rating(soup)  # содержит название и ссылку
            for n in range(len(dict_onerequest)): # проходимся по каждому названию игры на странице
                list_onerequest = list(dict_onerequest.keys())
                if re.sub(r'[.,"\'-?:!;]', '', name_game.lower()) == re.sub(r'[.,"\'-?:!;]', '',   # ищем полное вхождения названия игры
                                                                            list_onerequest[n].lower()):
                    link = dict_onerequest[list_onerequest[n]]  # получаем ссылку  на нужную игру
                    exit = game
                    break
            if exit != []:
                break
            if max_page == 1: # если стр 1, то ничего не перезагружаем
                link = "https://www.metacritic.com" + soup.find(class_ = "result first_result").find("a").get('href')


                break
            if i == max_page - 1:
                break
            url = url + "&page=0"
            url = url.replace(f'page={i}', f'page={i + 1}')
            driver.get(url)  # переходим на следующую страницу
            WebDriverWait(driver, 5).until(ec.element_to_be_clickable(("css selector",
                                                                       "#main_content > div > div.module.search_results.fxdcol.gu6 > div > ul > li.result.first_result")))
            soup = BeautifulSoup(driver.page_source, "html.parser")
    else:
        link = None
    if link == None:
        games_score.extend([[game_names[index][0], game_names[index][1], None, None, None]])
        print(None)
        print("--- %s seconds ---" % (time.time() - start_time), '\n')
        return games_score
    else:
        driver.get(link)  # переходим на страницу, где содержится информация об оценках и годе
        WebDriverWait(driver, 5).until(ec.presence_of_element_located(("class name", "content_nav")))
        soup = BeautifulSoup(driver.page_source, "html.parser")
        if soup.find(class_="section product_scores").find("span").text.strip() == "No score yet":
            meta_score = None

            "Далее обрабатываем все возможные варианты, когда есть вся необходимая информация," \
            "когда чего-то не хватает из metascore, user score, year"

            try:
                user_score = float(soup.find_all("a", class_="metascore_anchor")[1].find("div").text.strip())
                release_year = soup.find_all(class_="data")[1].text.strip().replace("  ", " ").split(" ")[2]
                games_score.extend([[game_names[index][0], game_names[index][1], meta_score, user_score, release_year]])
                print("Игра имеет данные")
                print(games_score)
                print("--- %s seconds ---" % (time.time() - start_time), '\n')
                return games_score
            except:
                try:
                    user_score = None
                    release_year = soup.find_all(class_="data")[1].text.strip().replace("  ", " ").split(" ")[2]
                    games_score.extend([[game_names[index][0], game_names[index][1], meta_score, user_score, release_year]])
                    print("Игра имеет данные")
                    print(games_score)
                    print("--- %s seconds ---" % (time.time() - start_time), '\n')
                    return games_score
                except:
                    meta_score = None
                    user_score = None
                    release_year = None
                    games_score.extend(
                        [[game_names[index][0], game_names[index][1], meta_score, user_score, release_year]])
                    print("Игра имеет данные")
                    print(games_score)
                    print("--- %s seconds ---" % (time.time() - start_time), '\n')
                    return games_score
        else:
            try:
                meta_score = float(soup.find(class_="section product_scores").find("span").text.strip())
                user_score = float(soup.find_all("a", class_="metascore_anchor")[1].find("div").text.strip())
                release_year = soup.find_all(class_="data")[1].text.strip().replace("  ", " ").split(" ")[2]
                games_score.extend([[game_names[index][0], game_names[index][1], meta_score, user_score, release_year]])
                print("Игра имеет данные")
                print(games_score)
                print("--- %s seconds ---" % (time.time() - start_time), '\n')
                return games_score
            except:
                try:
                    user_score = None
                    release_year = soup.find_all(class_="data")[1].text.strip().replace("  ", " ").split(" ")[2]
                    games_score.extend([[game_names[index][0], game_names[index][1], meta_score, user_score, release_year]])
                    print("Игра имеет данные")
                    print(games_score)
                    print("--- %s seconds ---" % (time.time() - start_time), '\n')
                    return games_score
                except:
                    user_score = None
                    release_year = None
                    games_score.extend(
                        [[game_names[index][0], game_names[index][1], meta_score, user_score, release_year]])
                    print("Игра имеет данные")
                    print(games_score)
                    print("--- %s seconds ---" % (time.time() - start_time), '\n')
                    return games_score




def save_file(save_file):
    "Записываем полученную информацию в csv"
    df_game = pd.DataFrame(save_file, columns=['Name',"Platform",'Critic_Score', "User_Score", "Year_of_Release"])
    df_game.to_csv('Game_Score.csv', index=False)

def main():
    "Задаем настройки webdriver и указываем путь к драйверу"
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--headless")
    s = Service(executable_path="D:\lavru\Metacritic_2\chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=options)

    "В файле csv хранятся: названия игр - название платформы"
    with open('Game_Platform_Example.csv', newline='',encoding='utf-8') as File:
        reader = csv.reader(File)
        game_names = []
        for row in reader:
            game_names.append(row) # сохраняем название игры и платформы в список

    game_info = []
    for game in tqdm(game_names[1:]):
        try:
            index = game_names.index(game)
            print(index)
            game_info.extend(search_all_info(game,game_names,driver))
            save_file(game_info)
        except:
            "В случае обнаружения парсера - выбрасывается ошибка для повторения операции"
            try:
                driver.close()
                driver = webdriver.Chrome(service=s, options=options)
                game_info.extend(search_all_info(game, game_names,driver))
                save_file(game_info)
            except:
                "В случае повторного обнаружения парсера - записываем None значения"
                game_info.extend([[game_names[index][0], game_names[index][1], None, None, None]])
                save_file(game_info)
                continue

if __name__ == "__main__":
    main()



