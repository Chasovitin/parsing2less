from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint

main_link = ('https://irkutsk.hh.ru/search/vacancy?clusters=true&enable_snippets=true&text=python&L_save_area=true&area=1124&from=cluster_area&showClusters=false')
params = {'search':'vacancy',
          'tab':'all'} # взял по аналогии с кинопоиском
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/85.0.4183.102 Safari/537.36'}

html = requests.get(main_link + '/search/vacancy',params=params,headers=headers)

soup = bs(html.text,'html.parser')

vacancy_block = soup.find('div',{'class':'vacancy-serp'})
vacancy_list = vacancy_block.find_all('div',{'class':'bloko-header-3_lite, bloko-section-header-3_lite'})


vacancies = []
for vacancy in vacancy_list:
    vacancy_data = {}
    vacancy_info = vacancy.find('div')
    vacancy_link = main_link + vacancy_info.parent['href']
    vacancy_name = vacancy_info.getText()
    vacancy_compensation = vacancy.find('span',{'class':'.bloko-section-header-3'}).nextSibling.getText()
    # vacancy_rating = vacancy.find('span',{'class':'rating__value'})  # тут у меня произошел сбой )) что делать?
    # if vacancy_rating:
    #     vacancy_rating = vacancy_rating.getText()
    #     try:
    #         vacancy_rating = float(vacancy_rating)
    #     except:
    #         pass

    vacancy_data['name'] = vacancy_name
    vacancy_data['link'] = vacancy_link
    vacancy_data['compensation'] = vacancy_compensation
    # vacancy_data['rating'] = vacancy_rating

    vacancies.append(vacancy_data)

pprint(vacancies)