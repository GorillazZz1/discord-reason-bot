from datetime import datetime
from bs4 import BeautifulSoup
import random, requests


def help(*args):
    return 'Хуй тебе!'


def google_search(*args):
    if len(args) == 0:
        return 'Введите **непустой** поисковой запрос!'

    q = ' '.join(args)
    return 'https://google.com/search?q=' + str(q.encode('utf-8')).replace('\\x', '%').replace(' ', '+')[2:-1]


def get_local_time(*args):
    return datetime.now().strftime('%X')


def get_random_anek(*arg):
    # TODO: add long texts reading!
    anekURL = 'https://baneks.ru/' + str(random.randint(1, 1142))
    r = requests.get(anekURL)
    if not (r.status_code == 200):
        return 'Для тебя нет анекдота :с'
    else:
        r.encoding = 'utf-8'
        return BeautifulSoup(r.text, 'html.parser').find('article').get_text()
