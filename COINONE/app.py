import requests
import json
import time

data = requests.get('https://tb.coinone.co.kr/api/v1/chart/olhc?site=coinoneeth&type=1h')

dict = json.loads(data.content)

for i in range(199):
    
    realTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(dict['data'][i]['DT'] / 1000)) 
    print(realTime)
    
    print(dict['data'][i]['Close'])