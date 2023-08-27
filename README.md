# web-crawler

### 목차

1. [파이썬 기초와 웹 크롤러](#part-1-파이썬-기초와-웹-크롤러)

2. [자동화 봇](#part-2-자동화-봇)

3. [번역기 만들기](#part-3-번역기-만들기)

- - -
## Part 1. 파이썬 기초와 웹 크롤러

- #### [파이썬으로 파일 read / write](./FILES/FILE.md)



> ### **웹크롤러 1 : 파이썬으로 웹페이지 접속과 원하는 글자 찾기**
> 
- 웹 크롤러 :  웹에 있는 데이터를 수집해서 저장해주는 프로그램
    1. python으로 원하는 웹페이지에 접속해서 그 페이지에 있는 HTML을 전부 다운받음
    2. 원하는 글자가 있는 부분만 찝어냄
- 설치할 것
    - `requests` : 파이썬으로 웹사이트 접속을 도와주는 라이브러리
    - `bs4` : 파이썬으로 HTML 웹문서 분석을 도와주는 라이브러리
    <br>
    ```bash
    $ pip install requests
    $ pip install bs4
    ```
    
- 라이브러리 활용해서 원하는 정보 가져오기
    - `data.content` 를 하면 html 정보이지만, `BeautifulSoup`을 써야 우리가 아는 HTML로 저장됨
    - `find_all(’태그명’, 속성명)` : 속성명은 `id` 또는 `class_` (class는 하나만)
        
        → 리스트 형태로 반환되기 때문에 인덱싱이 중요함, 고유한 id가 없는 경우에는 class 써서 인덱싱 쓰기
        
    
    ```python
    import requests
    from bs4 import BeautifulSoup
    
    data = requests.get('https://finance.naver.com/item/sise.nhn?code=005930')
    print(data.content)
    print(data.status_code) # 200이면 접속이 제대로 된 것
    
    soup = BeautifulSoup(data.content, 'html.parser')
    
    print(soup.find_all('strong', id="_nowVal")[0].text) # 찾은 결과는 리스트 형태 
    print(soup.find_all('span', class_="tah")[5].text) 
    ```
<br>

> ### **웹크롤러 2 : Case study**
> 
- class, id가 하나도 없는 요소 찾기 `select()`
    
    → 상위 요소의 클래스명을 이용해서 그 안에 있는 `<em>` 찾기
    
    ```python
    import requests
    from bs4 import BeautifulSoup
    
    data = requests.get('https://finance.naver.com/item/sise.nhn?code=005930')
    
    soup = BeautifulSoup(data.content, 'html.parser')
    
    print(soup.select('.f_up em')[1].text) # .은 클래스, #은 id
    ```
    
- 이미지 수집
    - 이미지 src 알고 있을 때 파일 저장하기
        
        `urllib.request.urlretrieve(이미지URL, '파일명')`
        
    
    ```python
    import requests
    import urllib.request
    
    from bs4 import BeautifulSoup
    
    data = requests.get('https://finance.naver.com/item/sise.nhn?code=005930')
    
    soup = BeautifulSoup(data.content, 'html.parser')
    
    img = soup.select('#img_chart_area')[0]
    
    urllib.request.urlretrieve(img['src'], 'chart.png')
    ```
    
<br>

> ### **웹크롤러 3 : 함수 이용하기**
> 

    `data = requests.get(f'https://finance.naver.com/item/sise.nhn?code={num}')`
문자열 중간에 변수를 넣고 싶을 때는 `{변수}` 추가하고 맨 앞에 `f` 쓰기

```python
import requests
import urllib.request

from bs4 import BeautifulSoup

def 현재가(num):
    data = requests.get(f'https://finance.naver.com/item/sise.nhn?code={num}')

    soup = BeautifulSoup(data.content, 'html.parser')

    return soup.find_all('strong', id="_nowVal")[0].text

print(현재가('005930')) # 삼성전자
print(현재가('066575')) # LG전자
```

<br>

> ### **웹크롤러 4 : 파일 저장**
> 

```python
import requests
import urllib.request

from bs4 import BeautifulSoup

''' 삼성전자, LG전자, 현대차, 카카오, LG디스플레이, 대한항공'''
stocks = ['005930', '066575', '005380', '035720', '034220', '003490']

def 현재가(num):
    data = requests.get(f'https://finance.naver.com/item/sise.nhn?code={num}')

    soup = BeautifulSoup(data.content, 'html.parser')

    return soup.find_all('strong', id="_nowVal")[0].text

file = open('stock.txt', 'w') # write mode
for x in stocks:
    file.write('\n' + 현재가(x))

file.close()
```

<br>

>### **무한 스크롤 데이터 수집 (네이버 VIEW)**
> 

보통 웹사이트들은 페이지별로 url이 나뉘어져 있지만, 없는 경우도 있음 (무한 스크롤)

→ 추가 데이터를 달라고 서버에게 요청하기

`[개발자 도구] → [Network] → [추가된 데이터 검색] → [Headers]`

```python
import requests
from bs4 import BeautifulSoup

requests.get('https://s.search.naver.com/p/review/search.naver?rev=44&where=view&api_type=11&start=31&query=%EC%82%AC%EA%B3%BC&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22food_ingredient%22%7D%7D%7D&main_q=&mode=normal&q_material=&ac=0&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=32&sm=tab_sug.top&ssc=tab.view.view&ngn_country=KR&lgl_rcode=02590127&fgn_region=&fgn_city=&lgl_lat=37.1974492&lgl_long=127.0715009&abt=&_callback=viewMoreContents')
```

`data.text.replace('\\', '')` : 백슬래쉬 제거하기

```python
import requests
from bs4 import BeautifulSoup

data = requests.get('https://s.search.naver.com/p/review/search.naver?rev=44&where=view&api_type=11&start=31&query=%EC%82%AC%EA%B3%BC&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22food_ingredient%22%7D%7D%7D&main_q=&mode=normal&q_material=&ac=0&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=32&sm=tab_sug.top&ssc=tab.view.view&ngn_country=KR&lgl_rcode=02590127&fgn_region=&fgn_city=&lgl_lat=37.1974492&lgl_long=127.0715009&abt=&_callback=viewMoreContents')

soup = BeautifulSoup(data.text.replace('\\', ''), 'html.parser') 

titles = soup.select('a.api_txt_lines')
print(titles[0].text) # 블로그 글 제목
print(titles[0]['href']) # 블로그 주소
print(titles[1].text)
print(titles[2].text)
```
- - -
## Part 2. 자동화 봇

>###  **JSON 데이터 다루기**
> 
- 개발자 도구에서 `[Network]`는 현재 페이지에 필요한 모든 데이터파일을 보여줌
- 자료형
    - 딕셔너리 자료형 `{ '자료이름' : '값' }`
    - JSON 자료형 `{ "자료이름" : "값" }`
        
        → 딕셔너리 자료형으로 바꾸어야 파이썬으로 편하게 조작 가능 (`"`→ `'`)
        

```python
import requests
import json

data = requests.get('https://tb.coinone.co.kr/api/v1/chart/olhc?site=coinoneeth&type=1h')
print(data.content)

dict = json.loads(data.content)
print(dict)
```

- `"data" = [{ }, { }, { }, … ]` 형태 → [ ] 안은 리스트

```python
import requests
import json

data = requests.get('https://tb.coinone.co.kr/api/v1/chart/olhc?site=coinoneeth&type=1h')

dict = json.loads(data.content) # 딕셔너리 자료형으로 변환
**print(dict['data'][0]['Close'])**
```

- epoch / UNIX 시간 (msec) : `"DT" : 1610240400000`
    - Epoch 타임을 일반적인 시간 형식으로 변환하기
        
        `time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch시간형식))`
        
    
    ```python
    import requests
    import json
    import time
    
    data = requests.get('https://tb.coinone.co.kr/api/v1/chart/olhc?site=coinoneeth&type=1h')
    
    dict = json.loads(data.content)
    
    for i in range(199):
        
        realTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(dict['data'][i]['DT'] / 1000)) 
        print(realTime)
        
        print(dict['data'][i]['Close'])
    ```
    
- 과거 가격 수만개 수집하려면 → URL 뒤에 `&last_time=(숫자)` 추가하기

- [자주 쓰는 time & formatting 문법](./COINONE/SYNTAX.md)

<br>

>### **파이썬 멀티쓰레딩 : 수집할 페이지가 많을 때**
> 
- 수집할 페이지가 매우 많을 때 순차적으로 크롤링을 수행하면 시간이 매우 오래 걸림
- multi-processing/multi-threading을 써서 병렬 작업
    - multi-processing : 여러개의 파이썬 실행창 띄우기
    - multi-threading : CPU 병렬 처리
        
        `from multiprocessing.dummy import Pool as ThreadPool`
        
- map 함수 : `map(함수, 리스트)`
    
    ```python
    import requests
    import json
    from multiprocessing.dummy import Pool as ThreadPool
    
    url = [
      'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1609524000000',
      'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608811200000',
      'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608098400000',
      'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1606672800000',
      'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605960000000',
      'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605242700000',
      'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1604534400000',
      'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603821600000',
      'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603108800000',
      'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1602396000000',
    ]
    
    def get_Close(url):
        data = requests.get(url)
        dict = json.loads(data.content)
    
        return dict['data'][0]['Close']
    
    pool = ThreadPool(4)
    result = pool.map(get_Close, url)
    
    pool.close()
    pool.join()
    
    print(result)
    ```

- [인스타그램 봇 만들기](./Instagram/BOT.md)

    
- 페이지 이동과 이미지 수집
    - 과정
        1. Python으로 로그인 후
        2. #강아지 검색 페이지 이동
        3. 첫 번째 사진 클릭
        4. 이미지 저장
        5. 다음 누르고 이미지 저장 (반복)
    - `find_element()` : 맨 처음 등장하는 것만 찾아줌
    - `find_elements()` : 여러 개 등장하는 거 찾아서 list 형태로 반환 → 인덱싱 필요
        
        ```python
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
        ```

- - -
## Part 3. 번역기 만들기

>### **API를 이용한 자동 영-한 번역기 만들기 1 (Papago)**
> 
- [네이버 파파고 API 이용](https://developers.naver.com/apps/#/myapps/T2ChYvTtXKmqJmbenfaJ/overview)
    - 사용 API : `Papago 번역`
    - 웹 서비스 URL : http://localhost
    - [API 사용법](https://developers.naver.com/docs/papago/papago-nmt-api-reference.md)
        
        ```json
        {
        	"message":   {
        			"result":   {
        					"srcLangType":  "ko",
        					"tarLangType":  "en",
        					"translatedText":  "Nice to meet you. I am studying.",
        					"engineType":"N2MT"
        				},
        			"@type":  "response",
        			"@service":  "naverservice.nmt.proxy",
        			"@version":"1.0.0"
        	}
        }
        ```
        
        ```python
        import os
        import sys
        import urllib.request
        import json
        client_id = "(client_id)" # 개발자센터에서 발급받은 Client ID 값
        client_secret = "(client_secret)" # 개발자센터에서 발급받은 Client Secret 값
        encText = urllib.parse.quote("반갑습니다 저는 지금 공부하고 있습니다.") # 번역할 문장
        
        data = "source=ko&target=en&text=" + encText # Ko를 En으로 바꾸기
        url = "https://openapi.naver.com/v1/papago/n2mt"
        
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",client_id)
        request.add_header("X-Naver-Client-Secret",client_secret)
        response = urllib.request.urlopen(request, data=data.encode("utf-8"))
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            dict = json.loads(response_body) # JSON을 딕셔너리로 변환
            print(dict['message']['result']['translatedText']) # 번역된 문장 출력
        else:
            print("Error Code:" + rescode)
        ```
        
<br>

>### **API를 이용한 자동 영-한 번역기 만들기 2 (Papago)**
> 
- 다른 .py에 있는 함수 가져와서 쓰기
    
    `from (파일명) import (함수명)`
    
- 엑셀 파일 읽어서 영-한 번역하기
    - 설치
        
        ```bash
        $ pip3 install pandas
        $ pip3 install openpyxl
        ```
        
        ```python
        from papago import translater
        import pandas as pd
        
        data = pd.read_excel('english.xlsx', engine='openpyxl')
        
        for l, row in data.iterrows(): # l : 행번호, row : 행 안의 내용
            data.loc[l, 'korean'] = translater(row['english'])
        
        print(data) # 영-한 번역된 결과
        
        data.to_excel('output.xlsx') # 결과 파일 생성
        ```
