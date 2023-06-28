import time
import datetime

T = time.localtime()

print(time.strftime('%Y년 %m월', T))
print(datetime.datetime(2023, 6, 27, 21, 38, 14))