from papago import translater
import pandas as pd

data = pd.read_excel('english.xlsx', engine='openpyxl')

for l, row in data.iterrows(): # l : 행번호, row : 행 안의 내용
    data.loc[l, 'korean'] = translater(row['english'])

print(data) # 영-한 번역된 결과

data.to_excel('output.xlsx') # 결과 파일 생성