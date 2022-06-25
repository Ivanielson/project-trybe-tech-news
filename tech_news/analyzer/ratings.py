from tech_news.database import find_news


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    data = find_news()
    report = sorted(
        data,
        key=lambda comment: comment["comments_count"],
        reverse=True
    )
    order_list = sorted(
        report,
        key=lambda row: row["comments_count"],
        reverse=True
    )
    news_list = []
    for news in order_list[:5]:
        news_list.append((news["title"], news["url"]))
    return news_list


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
