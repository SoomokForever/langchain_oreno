# 정적크롤링
import requests
from bs4 import BeautifulSoup as bs
import time
# 셀레니움
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# ChromeOptions 설정 (옵션 생략 가능)
chrome_options = webdriver.ChromeOptions()

# ChromeDriver 설정 및 브라우저 실행
driver = webdriver.Chrome(options=chrome_options)

# 브라우저 창 크기 설정
driver.set_window_size(1500, 750)

# Google 홈페이지 열기
driver.get('https://account.everytime.kr/login')

time.sleep(3)

# ID 입력란 찾기
id_input = driver.find_element(By.NAME, 'id')
# 입력란 클릭
id_input.click()
# 'ab9881' 입력
id_input.send_keys('ab9881')

# ID 입력란 찾기
password_input = driver.find_element(By.NAME, 'password')
# 입력란 클릭
password_input.click()
# 'ab9881' 입력
password_input.send_keys('ab9881')

time.sleep()