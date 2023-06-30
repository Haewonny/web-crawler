import os
import sys
import urllib.request
import json

def translater(s):
    client_id = "T2ChYvTtXKmqJmbenfaJ" # 개발자센터에서 발급받은 Client ID 값
    client_secret = "HfYoqZUpk4" # 개발자센터에서 발급받은 Client Secret 값
    encText = urllib.parse.quote(s) # 번역할 문장

    data = "source=en&target=ko&text=" + encText # en를 ko으로 바꾸기
    url = "https://openapi.naver.com/v1/papago/n2mt"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        dict = json.loads(response_body) # JSON을 딕셔너리로 변환
        return dict['message']['result']['translatedText'] # 번역된 문장 반환
    else:
        print("Error Code:" + rescode)
        
translater('히히')