import requests
from bs4 import BeautifulSoup
from DataBase import SQL

db = SQL('Data.db')


def parser(user_id):
    try:
        info_list = []
        for i in db.list_link(user_id):
            r = requests.get(i)
            soup = BeautifulSoup(r.content, 'html.parser')
            name = soup.find('div', {'class': 'cmc-details-panel-header__name'}).text.strip(' ')
            price = soup.find('span', {'class': 'cmc-details-panel-price__price'}).text.strip(' ')
            grouping = (name + ' → ' + price)
            info_list.append(grouping)
        info_crypt = '\n'.join(map(str, info_list))
        return info_crypt
    except AttributeError:
        return 'Incorrect link entered, enter / dell to remove links'
