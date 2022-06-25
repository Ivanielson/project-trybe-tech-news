from tech_news.database import search_news
import datetime


months = {
    "01": "janeiro de",
    "02": "fevereiro de",
    "03": "março de",
    "04": "abril de",
    "05": "maio de",
    "06": "junho de",
    "07": "julho de",
    "08": "agosto de",
    "09": "setembro de",
    "10": "outubro de",
    "11": "novembro de",
    "12": "dezembro de",
}


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    data = search_news({"title": {"$regex": title, "$options": "i"}})
    report_list = []
    for news in data:
        report_list.append((news["title"], news["url"]))
    return report_list


def convert_date_to_long_format(date):
    split_date = str(date).split('-')
    if int(split_date[2]) < 10:
        new = f"{split_date[2]} de {months[split_date[1]]} {split_date[0]}"
        return new[1:]
    else:
        return f"{split_date[2]} de {months[split_date[1]]} {split_date[0]}"


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        format_date = datetime.date.fromisoformat(date)
        news_date = convert_date_to_long_format(format_date)
        data = search_news({"timestamp": news_date})
        report_list = []
        for news in data:
            report_list.append((news["title"], news["url"]))
        return report_list
    except ValueError:
        raise ValueError("Data inválida")


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
