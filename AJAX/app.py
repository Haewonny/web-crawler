import requests
from bs4 import BeautifulSoup

titles = []
def find_Top100(query):
    for i in range(1, 101, 30):
        data = requests.get(f'https://s.search.naver.com/p/review/search.naver?rev=44&where=view&api_type=11&start={i}&query={query}&nso=&nqx_theme=%7B%22theme%22%3A%7B%22main%22%3A%7B%22name%22%3A%22food_ingredient%22%7D%7D%7D&main_q=&mode=normal&q_material=&ac=0&aq=0&spq=0&st_coll=&topic_r_cat=&nx_search_query=&nx_and_query=&nx_sub_query=&prank=32&sm=tab_sug.top&ssc=tab.view.view&ngn_country=KR&lgl_rcode=02590127&fgn_region=&fgn_city=&lgl_lat=37.1974492&lgl_long=127.0715009&abt=&_callback=viewMoreContents')
        soup = BeautifulSoup(data.text.replace('\\', ''), 'html.parser') 

        for j in range(30):
            titles.append(soup.select('a.api_txt_lines')[j].text)
    return titles

result = find_Top100('사과')

file = open('titles.txt', 'w') # write mode

for i in range(100):
    file.write('\n' + str(i + 1)+ '. ' + result[i])

file.close()