import requests
from parsel import Selector
import time


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui """
    try:
        HEADER = {"user-agent": "Fake user-agent"}
        response = requests.get(url, headers=HEADER, timeout=1)
        time.sleep(1)
        if response.status_code != 200:
            return None
        else:
            return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    news_list = []
    for card in selector.css("article.entry-preview"):
        news = card.css("h2.entry-title > a::attr(href)").get()
        news_list.append(news)
    return news_list


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    next_page = selector.css("a.next::attr(href)").get()
    if not next_page:
        return None
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
