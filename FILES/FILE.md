### **파이썬으로 파일 read / write**
 
- 파일 만들기 : `open(파일경로, ‘w’)`
    
    → 이미 그 파일이 있으면 덮어쓰기, 없으면 새로 생성
    
- 파일에 내용 작성하기 : `오픈한 파일.write(’내용’)`
- 파일 닫기 : `오픈한 파일.close()`
    
    ```python
    file = open('a.txt', 'w') # write mode
    file.write('hello')
    
    file.close()
    
    file = open('a.txt', 'r') # read mode
    print(file.read())
    ```
    
- 파일 read 모드로 오픈 :  `open(파일경로, ‘r’)`
- 파일 내용 가져오기 : `오픈한 파일.read()`
    
    ```python
    file = open('a.txt', 'r') # read mode
    print(file.read())
    
    file.close()
    ```
    
- 파일 append 모드로 오픈 : `open(파일 경로, ‘a’)`
    
    ```python
    file = open('a.txt', 'a') # append mode
    file.write('반가워')
    
    file.close()
    ```
    
- 엑셀(.csv) 파일 생성
    
    ```python
    file = open('data.csv', 'w') # write mode
    file.write('1, 2, 3')
    file.write('\n4, 5, 6')
    
    file.close()
    ```
    
- 리스트 내용으로 파일 생성하기
    
    ```python
    list = ['삼성전자', '카카오', '네이버', '신풍제약']
    
    file = open('data.txt', 'w')
    for l in list:
        file.write('\n' + l)
    
    file.close()
    ```