from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from requests.api import options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib.request
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["enable-logging"])

def today(request):
    # 지역은 서울로 고정
    city = 'location'
    # 서울 지역의 날씨 정보 불러오기
    URL = f'https://www.google.com/search?q=weather+{city}'
    # 헤더 설정
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36 OPR/67.0.3575.115'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser', from_encoding="utf8")
    result = dict()

    # 가져올 데이터 세팅
    # 1. 지역
    result['region'] = soup.find("div", {"id": "wob_loc"}).text
    # 2. 시간
    result['dayhour'] = soup.find("div", {"id": "wob_dts"}).text
    # 3. 기온
    result['temp_now'] = soup.find("span", {"id": "wob_tm"}).text
    # 4. 날씨
    result['weather_now'] = soup.find("span", {"id": "wob_dc"}).text
    # 5. 강수
    result['precipitation'] = soup.find("span", {"id": "wob_pp"}).text
    # 6. 습도
    result['humidity'] = soup.find("span", {"id": "wob_hm"}).text
    # 7. 풍속
    result['wind'] = soup.find("span", {"id": "wob_ws"}).text
    temp_int=int(result['temp_now'])
    precipitation_int=int(result['precipitation'].rstrip('%'))
    humidity_int=int(result['humidity'].rstrip('%'))
    wind_float=float(result['wind'].rstrip('m/s'))
    
    return render(request, 'mainPage/today.html',{'weather': result , 'temp_int' : temp_int , 'precipitation_int': precipitation_int , 'humidity_int': humidity_int , 'wind_float': wind_float})

def mainpage(request):
     # 지역은 서울로 고정
    city = 'location'
    # 서울 지역의 날씨 정보 불러오기
    URL = f'https://www.google.com/search?q=weather+{city}'
    # 헤더 설정
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36 OPR/67.0.3575.115'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser', from_encoding="utf8")
    result = dict()

    # 가져올 데이터 세팅
    # 1. 지역
    result['region'] = soup.find("div", {"id": "wob_loc"}).text
    # 2. 시간
    result['dayhour'] = soup.find("div", {"id": "wob_dts"}).text
    # 3. 기온
    result['temp_now'] = soup.find("span", {"id": "wob_tm"}).text
    # 4. 날씨
    result['weather_now'] = soup.find("span", {"id": "wob_dc"}).text
    # 5. 강수
    result['precipitation'] = soup.find("span", {"id": "wob_pp"}).text
    # 6. 습도
    result['humidity'] = soup.find("span", {"id": "wob_hm"}).text
    # 7. 풍속
    result['wind'] = soup.find("span", {"id": "wob_ws"}).text
    temp_int=int(result['temp_now'])
    precipitation_int=int(result['precipitation'].rstrip('%'))
    humidity_int=int(result['humidity'].rstrip('%'))
    wind_float=float(result['wind'].rstrip('m/s'))
    return render(request, 'mainPage/mainPage.html',{'weather': result })