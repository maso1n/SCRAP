import codecs
import csv
import datetime
import os
import random
import re
from random import randint
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager



def accept_button(driver):
    time.sleep(random_time_interval(2, 4))
    confirm_bottom = driver.find_element(By.XPATH, "//a[@class='cookies-eu-message-button cookies-eu-message-button-accept action-accept-cookies-eu']")
    confirm_bottom.click()

def olx_page(driver, link, arr_links_of_publication, number):
    time.sleep(random_time_interval(2, 3))
    driver.get(
        url=link
    )
    time.sleep(random_time_interval(10, 15))
    driver.execute_script("window.scrollTo(0, 2500);")
    time.sleep(random_time_interval(5, 8))
    driver.execute_script("window.scrollTo(0, 3500);")
    time.sleep(random_time_interval(10, 13))
    driver.execute_script("window.scrollTo(0, 5500);")
    time.sleep(random_time_interval(5, 7))
    driver.execute_script("window.scrollTo(0, 6500);")
    time.sleep(random_time_interval(2, 3))
    driver.execute_script("window.scrollTo(0, 7500);")
    time.sleep(random_time_interval(3, 4))
    driver.execute_script("window.scrollTo(0, 10000);")
    time.sleep(random_time_interval(5, 9))
    completeName = os.path.join("bol.html")
    file_object = codecs.open(completeName, "w", "utf-8")
    html = driver.page_source
    file_object.write(html)
    a = get_href("bol.html")
    for a1 in a:
        #print(a1)
        get_information(a1)
    print("====================================", number)
    return arr_links_of_publication

def get_href(file_path):
    with open(file_path, encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")
    #items_divs = soup.find_all("a", class_="ecl-link ecl-link--standalone jv-result-summary-title ng-star-inserted")
    bloks_arr = soup.find_all("article", class_="ecl-u-border-bottom ecl-u-border-color-grey-15 ecl-u-pv-m ecl-u-box-sizing-content ng-star-inserted")
    #print(items_divs)
    #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!bloks_arr",bloks_arr)
    urls = []

    for block in bloks_arr:
        block_text = block.find("span", "ecl-u-type-s jv-result-employer-name").text
        block_text = block_text.lower()
        is_true = True;
        words = ["ingenieur", "glaser", "verkäuferin", "klempner", "servicetechniker ", "monteur", " cnc", "arzt", " work ","betriebsschlosser","berufskraftfahrer","elektriker ","mechatroniker","personal","tierarzthelfer", "randstad", "deutsche bahn ag", " teamleiter ", " trenkwalder ", "datenschutz", "manpower", "pamec", " personaldienstl", "bremen", " a/m/e ", "adiro", "gi group", "persona", "perzukunft", "people", " hr ", "jobimpulse", " akko ", "job", "bindan", " adecco ", "aurea",  "xing", "experts", "people", "yakabuna", "worx", "accurat", "tempton", "zeitarbeit", "apero", "bstlux-werft u schifffahrt gmbh", "acordiz"]
        for word in words:
            if word in block_text:
                is_true=False;
                print("**",word,"**")
                break
            else:
                pass
        link = "https://ec.europa.eu" + block.find("a",
                                                   "ecl-link ecl-link--standalone jv-result-summary-title ng-star-inserted").get(
            "href")
        if is_true:
            urls.append(link)
            print(block_text, link)
        else:
            print("-1--nie podchodit", block_text, link)

    return urls

def get_information(link):
    try:
        driver.execute_script(f'window.open("{link}")')
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(3)
        completeName = os.path.join("bol1.html")
        file_object = codecs.open(completeName, "w", "utf-8")
        html = driver.page_source
        time.sleep(1.5)
        driver.execute_script("window.scrollTo(0, 2500);")
        file_object.write(html)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        with open("bol1.html", encoding='utf-8') as file:
            src = file.read()
        soup = BeautifulSoup(src, "lxml")
        time.sleep(1)
        words_list = ["Befristete Überlassung von Arbeitskräften", "Sonstige Überlassung von Arbeitskräften", "Überlassung von Arbeitskräften", "Junior", " Mechaniker", "Elektriker", "Senior", " CAD",  "Tierarzthelfer", "Fullstack", "DevOps", "Bauingenieur", "Fahrbahnmechaniker", "Lokführer", "Cloud", "Fachinformatiker", "Verbundmanager", "Verkäufer", "Consultant", "Objektleiter", "Entwickler"]
        is_true=True
        for word in words_list:
            if word in soup.find("section", "ecl-col-m-9").text:
                is_true = False;
                print("-2--nie podchodit","**", word,"**", link)
        if is_true:
            try:
                title = soup.find("h1").text
            except:
                title = "none"
            arr_link = set()
            arr_mail = set()
            block_link = soup.find("section", "ecl-col-m-9")
            links = block_link.find_all("a")

            for link1 in links:
                    #print(link.get("href"))
                if "@" in link1.get("href"):
                        #print("mail = ", link.get("href"))
                    if "mailto" in link1.get("href"):
                        arr_mail.add(link1.get("href")[7:])
                    else:
                        arr_mail.add(link1.get("href"))

                else:
                        #print("site = ", link.get("href"))
                    site = link1.get("href")
                    arr_link.add(site)
            arr_mail=list(arr_mail )
            try:
                arr_mail0 = arr_mail[0]
            except:
                arr_mail0 = " "
            try:
                arr_mail1 = arr_mail[1]
            except:
                arr_mail1 = " "
            arr_link = list(arr_link)
            try:
                arr_link0 = arr_link[0]
            except:
                arr_link0=" "

            try:
                arr_link1 = arr_link[1]
            except:
                arr_link1 = " "

            try:
                arr_link2 = arr_link[2]
            except:
                arr_link2 = " "
            arr_link=list(arr_link)
            print(title, arr_mail0, arr_mail1,arr_link0, arr_link1, arr_link2, link)

            df.loc[len(df.index)] = title, arr_mail0, arr_mail1,arr_link0, arr_link1, arr_link2, link;

    except:
        pass
def create_driver():

    #options = webdriver.ChromeOptions()
    options = webdriver.FirefoxOptions()
    ua = UserAgent()
    userAgent = ua.random
    print(userAgent)
    options.add_argument("--disable-blink-features=AutomationControlled")
    #фоновое выполнение
    #options.headless = True

    #options.add_extension("extension_1_50_1_0.crx")
    # options.add_argument("start-maximized")
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    driver = FirefoxService(executable_path=GeckoDriverManager().install())

    # Создайте драйвер Firefox, передав объект службы
    driver = webdriver.Firefox(service=driver, options=options)

    #driver.set_preference("dom.webdriver.enabled", False)
    # driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    #     'source': '''
    #         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
    #         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
    #         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
    #         '''
    #     }
    # )

    time.sleep(random_time_interval(2, 3))
    return driver


def random_time_interval(min, max):
    number = randint(min * 10, max * 10) / 15
    return number


def close_all(driver):
    driver.delete_all_cookies()
    driver.close()
    driver.quit()
    print("Delete driver")
    time.sleep(random_time_interval(17, 25))

try:
    i=0
    links = {
#"https://ec.europa.eu/eures/portal/jv-se/search?page=1&resultsPerPage=50&orderBy=BEST_MATCH&locationCodes=de&keywordsEverywhere=Packer&sector=c&lang=en": 179,
#"https://ec.europa.eu/eures/portal/jv-se/search?page=1&resultsPerPage=50&orderBy=BEST_MATCH&locationCodes=de&keywordsEverywhere=Packer&sector=NS,g&lang=en": 162,
#"https://ec.europa.eu/eures/portal/jv-se/search?page=1&resultsPerPage=50&orderBy=BEST_MATCH&locationCodes=de&keywordsEverywhere=Packer&sector=a,d,e,f,h,i,j,k,l,m,p,q,r,s,u,t&lang=en": 134,
"https://ec.europa.eu/eures/portal/jv-se/search?page=1&resultsPerPage=50&orderBy=BEST_MATCH&keywordsEverywhere=Packer&sector=n&availableLanguages=de&educationLevel=NS&positionOfferingCodes=NS,contract,contracttohire,temporary,temporarytohire&lang=en": 78,
#"https://ec.europa.eu/eures/portal/jv-se/search?page=1&resultsPerPage=50&orderBy=BEST_MATCH&keywordsEverywhere=Packer&sector=n&availableLanguages=de&positionOfferingCodes=directhire&publicationPeriod=LAST_MONTH&escoIsco=C8,C9&minNumberPost=1&lang=en": 167,
#"https://ec.europa.eu/eures/portal/jv-se/search?page=1&resultsPerPage=50&orderBy=BEST_MATCH&keywordsEverywhere=Packer&sector=n&availableLanguages=de&positionOfferingCodes=directhire&publicationPeriod=LAST_MONTH&escoIsco=C3,C4,C5,C6,C7&minNumberPost=1&lang=en": 126,
#"https://ec.europa.eu/eures/portal/jv-se/search?page=1&resultsPerPage=50&orderBy=BEST_MATCH&keywordsEverywhere=Packer&sector=n&availableLanguages=de&positionOfferingCodes=directhire&publicationPeriod=LAST_MONTH&escoIsco=C0,C1,C2,C3,C4,C5,C6,C7&minNumberPost=1&lang=en": 128,
"https://ec.europa.eu/eures/portal/jv-se/search?page=1&resultsPerPage=50&orderBy=BEST_MATCH&locationCodes=de&keywordsEverywhere=Verpacker&positionScheduleCodes=NS,parttime,flextime&lang=en": 190,
#"https://ec.europa.eu/eures/portal/jv-se/search?page=1&resultsPerPage=50&orderBy=BEST_MATCH&locationCodes=de&keywordsEverywhere=Verpacker&positionScheduleCodes=fulltime&sector=NS,a,c,d,e,f,g,h,i,j,k,m,o,p,q,r,s,u&lang=en": 176,
"https://ec.europa.eu/eures/portal/jv-se/search?page=1&resultsPerPage=50&orderBy=BEST_MATCH&locationCodes=de&keywordsEverywhere=Verpacker&positionScheduleCodes=fulltime&sector=n&positionOfferingCodes=directhire&escoIsco=C9&minNumberPost=1&lang=en": 200,
"https://ec.europa.eu/eures/portal/jv-se/search?page=1&resultsPerPage=50&orderBy=MOST_RECENT&locationCodes=de&keywordsEverywhere=Verpacker&positionScheduleCodes=fulltime&sector=n&positionOfferingCodes=directhire&escoIsco=C9&minNumberPost=1&lang=en": 200,
"https://ec.europa.eu/eures/portal/jv-se/search?page=1&resultsPerPage=50&orderBy=BEST_MATCH&locationCodes=de&keywordsEverywhere=Verpacker&positionScheduleCodes=fulltime&sector=n&positionOfferingCodes=directhire&escoIsco=C1,C2,C3,C4,C5,C6,C7,C8&minNumberPost=1&lang=en": 122,

"https://ec.europa.eu/eures/portal/jv-se/search?page=1&resultsPerPage=50&orderBy=BEST_MATCH&locationCodes=de&keywordsEverywhere=Packkraft&sector=m,c&availableLanguages=de&minNumberPost=1&lang=en": 186,
"https://ec.europa.eu/eures/portal/jv-se/search?page=1&resultsPerPage=50&orderBy=MOST_RECENT&locationCodes=de&keywordsEverywhere=Packkraft&sector=NS&availableLanguages=de&minNumberPost=1&lang=en": 200,
"https://ec.europa.eu/eures/portal/jv-se/search?page=1&resultsPerPage=50&orderBy=BEST_MATCH&locationCodes=de&keywordsEverywhere=Packkraft&sector=NS&availableLanguages=de&minNumberPost=1&lang=en": 200,
"https://ec.europa.eu/eures/portal/jv-se/search?page=1&resultsPerPage=50&orderBy=BEST_MATCH&locationCodes=de&keywordsEverywhere=Packkraft&sector=m,c&availableLanguages=de&minNumberPost=1&lang=en": 186,
"https://ec.europa.eu/eures/portal/jv-se/search?page=1&resultsPerPage=50&orderBy=BEST_MATCH&locationCodes=de&keywordsEverywhere=Packkraft&sector=f,g,h,p,s&availableLanguages=de&minNumberPost=1&lang=en": 180,

    }
    for link in links.keys():
        driver = create_driver()
        df = pd.DataFrame(
            {"title": [], "arr_mail0": [], "arr_mail1": [], "arr_link0": [], "arr_link1": [], "arr_link2": [],
             "link": []})
        arr_links_of_publication = []
        # Найдите индекс символа "=", чтобы получить позицию значения "page"
        equals_index = link.index("=")
        # Найдите индекс символа "&", чтобы получить позицию конца значения "page"
        ampersand_index = link.index("&", equals_index)
        # Получите исходное значение "page"
        original_page = int(link[equals_index + 1:ampersand_index])
        i+=1
        for j in range(1, links[link]+1):
            modified_link = link[:equals_index + 1] + str(j) + link[ampersand_index:]
            print(j)
            driver.get(url="https://ec.europa.eu/eures/portal/jv-se/search?page=1&resultsPerPage=50&orderBy=BEST_MATCH&locationCodes=de&keywordsEverywhere=Lader&positionScheduleCodes=fulltime&sector=c&availableLanguages=de&positionOfferingCodes=contract,directhire&lang=de")
            time.sleep(random_time_interval(2, 3))
            arr_links_of_publication = olx_page(driver, modified_link, arr_links_of_publication, j)
            time.sleep(random_time_interval(2, 3))
            if (j % 10 == 0):
                df.to_excel(f'link_{i}page_{j}.xlsx', index=False)
                print("zapiska++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=")
        df.to_excel(f'link_{i}path_rez.xlsx', index=False)
        close_all(driver)
except Exception as ex:
    print(ex)
finally:
    pass
