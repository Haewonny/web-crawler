### **인스타그램 자동 접속 봇 만들기**
 
- 설치
    
    ```bash
    $ pip3 install selenium # 최신 ver. 4.10.0 설치
    
    $ pip3 install webdriver-manager # 크롬 드라이버 버전 맞춰주는 라이브러리
    ```
    
- 인스타그램 접속해서 원하는 글자 수집하기
    
    ```python
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    import time
    
    driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))
    
    url = "https://instagram.com/"
    driver.get(url)
    
    time.sleep(2) # 로딩 시간 오류 방지
    
    e = driver.find_element_by_css_selector('._ab25').text
    print(e)
    ```
    
- 인스타그램 자동 로그인
    
    ```python
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
    
    id = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    pw = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
    login = driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3) > button")
    
    id.send_keys("instagramID")
    pw.send_keys("12345678910")
    login.click()
    ```