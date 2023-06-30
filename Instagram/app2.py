import urllib.request

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()

''' 상단에 Chrome이 자동화된 소프트웨어에 의해 제어되고 있습니다 제거하기 '''
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
options.add_experimental_option("detach", True) # 브라우저 꺼짐 방지 오류 !!!!!!!!!!

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = "https://instagram.com/"
driver.get(url)

time.sleep(2) # 로딩 시간 오류 방지

''' 1. 로그인 '''
e = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
e.send_keys("instagramID")

e = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
e.send_keys("12345678910")

e.send_keys(Keys.ENTER)

''' 2. 해시태그 검색 페이지 이동 (url 변경)'''
driver.get('https://www.instagram.com/explore/tags/강아지/')
driver.implicitly_wait(10) # 요소가 안 보이면 최대 10초 기다리기

''' 3. 첫 번째 사진 클릭 '''
driver.find_elements(By.CSS_SELECTOR, '._aatp')[2].click()

''' 4. 이미지 저장 '''
img = driver.find_element(By.CSS_SELECTOR, '.FFVAD').get_attribute('src') # src 가져오기
urllib.request.urlretrieve(img, '1.jpg')