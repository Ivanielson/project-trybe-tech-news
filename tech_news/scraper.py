import requests
from parsel import Selector
import time


HEADER = {"user-agent": "Fake user-agent"}


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
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
    selector = Selector(html_content)
    news_url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    news_date = selector.css("li.meta-date::text").get()
    author = selector.css("span.author > a::text").get()
    list_summary = selector.css(
        "div.entry-content p:nth-child(2) *::text"
    ).getall()
    summary = ""
    for text in list_summary:
        summary += text
    comments_count = selector.css("comment-content::text").getall()
    tags = selector.css("section.post-tags ul li > a::text").getall()
    category = selector.css("a > span.label::text").get()
    report = {
        "url": news_url,
        "title": title,
        "timestamp": news_date,
        "writer": author,
        "comments_count": len(comments_count),
        "summary": summary,
        "tags": tags,
        "category": category,
    }
    return report


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""


# REF: https://www.journaldev.com/23625/python-trim-string-rstrip-lstrip-strip


if __name__ == "__main__":
    content = fetch("https://blog.betrybe.com/tecnologia/arquivo-bin/")
    scrape_noticia(content)
