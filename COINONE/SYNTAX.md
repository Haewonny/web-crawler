### **자주 쓰는 time과 formatting 문법**
> 
- `time()` : 현재 시간을 Epoch 시간으로
    
    ```python
    import time
    
    print(time.time())
    ```
    
- 현재 `ctime` 출력
    
    ```
    import time
    
    T = time.time()
    T = time.ctime(T)
    print(T)
    ```
    
- `localtime()` 으로 세부 항목 출력
    
    ```
    import time
    
    T = time.localtime()
    print(T.tm_year)
    ```
    
    ```python
    import time
    
    T = time.localtime()
    print('현재 시간은 ' + str(T.tm_hour) + '시')
    ```
    
- strftime()으로 시간표시형식 마음대로 바꾸기 `time.strftime('포맷팅 문법', 로컬 타임)`
    - `%Y` 년, `%H` 시, `%m` 월, `%M` 분, `%d` 일, `%S` 초
    
    ```python
    import time
    
    T = time.localtime()
    
    print(time.strftime('%Y년 %m월', T))
    ```
    
- 문자 Formatting → 문자 중간중간에 변수 또는 문자 넣고 싶을 때
    
    ```python
    name = 'Kim'
    
    print(f'안녕하세요 {name}')
    print('안녕하세요 %s' %name) # 예전 문법
    ```