import requests
from bs4 import BeautifulSoup


def get_html(url):
    response = requests.get(url)
    return response.text


def get_dates(html):
    soup = BeautifulSoup(html, 'lxml')
    get_data_div = soup.find('div', class_='aubl_cont')
    return get_data_div


def get_every_date(html):
    get_list = html.find_all('div', class_='aubl_item')
    list_ = []
    for list in get_list:
        try:
            photo = list.find('a', class_='aubli_img').find('img').get('src')
        except:
            photo = ""

        try:
            description = list.find('div', class_='aubli_desc').text
        except:
            description = ''

        try:
            title = list.find('div', class_='aubli_data').find('a').text
        except:
            title = ''


        data = {'title': title.replace('\n', ''), 'description': description.replace('\n', '').strip(),
                'photo': photo, }
        list_.append(data)
    return list_


def pars():
    akg_url = 'https://www.igromania.ru/news/game/'
    html = get_html(akg_url)
    html = get_dates(html)
    list_ = get_every_date(html)
    return list_