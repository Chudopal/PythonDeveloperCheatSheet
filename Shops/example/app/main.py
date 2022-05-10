
"""Программа для просмотра пабликаций.

Возможности:

- просмотреть все публикации
- добавить публикацию
- отметить публикацию как понравившуюся
- посмотреть список понравившихся публикаций

Приверы публикаций:
- Сегодня солнечная погода!
- Функция - это исполняемый фрагмент кода, который можно переиспользовать множество раз.
- Название переменной - это то, как вы можете обращаться к значению в данной переменной.
"""

import json
from typing import List, Dict


def read_file(path, name) -> List:
    with open(path) as file:
        data = json.load(file)
    return data.get(name)


def write_file(path, data) -> None:
    with open(path, "w") as file:
        json.dump(data, file)


def adaptor(data: List) -> Dict:
    result = {}
    for article in data:
        result[article.get("id")] = article.get("content")
    return result


def file_adaptor(data: Dict, name: str) -> Dict:
    result = {
        "arctiles": get_all_articles(),
        "liked_articles": get_all_like_articles()
    }
    articles = []
    for article_id, article_content in data.items():
        articles.append(
            {"id": article_id,
            "content": article_content}
        )
    result[name] = articles
    return result


def get_all_articles() -> List:
    data = read_file("app/storage.json", "articles")
    return adaptor(data)


def get_all_like_articles() -> List:
    data = read_file("app/storage.json", "liked_articles")
    return adaptor(data)


def calculate_id(article: str, articles):
    article_id = len(articles) + 1
    articles[article_id] = article


def add_article(article: str, articles) -> None:
    calculate_id(article, articles)
    data = file_adaptor(articles, "articles")
    write_file("app/storage.json", data)


def like_article(article_id) -> None:
    article_content = get_all_articles().get(article_id)
    liked_articles = get_all_like_articles()
    calculate_id(article_content, liked_articles)
    data = file_adaptor(liked_articles, "liked_articles")
    write_file("app/storage.json", data)


def format_article(article_list: Dict) -> str:
    return "\n".join([
        f"{article_id}. {article}"
        for article_id, article in article_list.items()
    ])


def menu() -> str:
    return (
        "*"*80 + "\n" +
        "1. Посмотреть все публикации\n" +
        "2. Добавить публикацию\n" + 
        "3. Лайкнуть публикацию\n" +
        "4. Посмотреть понравившиеся."
    )


def make_choice(choice: int):
    result = ""
    if choice == 1:
        articles = get_all_articles()
        message = format_article(articles)
        result = message
    elif choice == 2:
        article = input("Напишите публикацию: ")
        add_article(article, get_all_articles())
    elif choice == 3:
        article_id = int(input("Введите номер понравившейся публикации: "))
        like_article(article_id)
    elif choice == 4:
        articles = get_all_like_articles()
        message = format_article(articles)
        result = message
    return result


def run() -> None:
    choice = None
    while choice != 5:
        print(menu())
        choice = int(input("Введите пункт меню: "))
        message = make_choice(choice)
        print(message)


run()