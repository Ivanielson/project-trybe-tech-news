from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    data = search_news({"title": {"$regex": title, "$options": "i"}})
    report_list = []
    for news in data:
        report_list.append((news["title"], news["url"]))
    return report_list


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""
    find_tag = f"{tag[0].upper()}{tag[1:].lower()}"
    data = search_news({"tags": find_tag})
    report_list = []
    for news in data:
        report_list.append((news["title"], news["url"]))
    return report_list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    data = search_news({"category": {"$regex": category, "$options": "i"}})
    report_list = []
    for news in data:
        report_list.append((news["title"], news["url"]))
    return report_list
