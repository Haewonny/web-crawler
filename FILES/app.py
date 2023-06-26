list = ['삼성전자', '카카오', '네이버', '신풍제약']

file = open('data.txt', 'w')
for l in list:
    file.write('\n' + l)

file.close()