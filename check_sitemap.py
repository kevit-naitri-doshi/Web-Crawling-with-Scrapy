import requests
from bs4 import BeautifulSoup
from config import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def check_sitemap(url):
    all_sitemaps=[]
    try:
        page=requests.get(f'{complete_url}robots.txt').text
        source=BeautifulSoup(page,'lxml')
        ans=source.find('body').text.split('\n')
        for _ in ans:
            if 'Sitemap' in _:
                all_sitemaps.append(_.split(' ')[1])
        print(all_sitemaps)
        return all_sitemaps
    except Exception as e:
        print(str(e))



def traverse_sitemaps(sitemap_list):
    cService = webdriver.ChromeService(executable_path=path)
    driver = webdriver.Chrome(service = cService)
    links=[]
    for sitemap in sitemap_list:
        driver.get(sitemap)
        tr_index=1
        while True:
            try:
                map=driver.find_element(By.XPATH,f'//*[@id="sitemap"]/tbody/tr[{tr_index}]/td[1]/a')
                time.sleep(0.5)
                # for map in maps:
                map.click()
                time.sleep(0.5)
                inner_tr_index=1
                while True:
                    try:
                        sub_map=driver.find_element(By.XPATH,f'//*[@id="sitemap"]/tbody/tr[{inner_tr_index}]/td[1]/a').text
                        links.append({'link':sub_map})
                        inner_tr_index+=1
                    except:
                        print(f'Map {tr_index} over')
                        driver.get(sitemap)
                        tr_index+=1
                        break
            except:
                print('All maps over')
                break

    return links






