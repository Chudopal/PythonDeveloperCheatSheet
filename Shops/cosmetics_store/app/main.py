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

from typing import List, Dict
import json

# ARTICLES = {
#     1: "Сегодня солнечная погода!",
#     2: "Функция - это исполняемый фрагмент кода, который можно переиспользовать множество раз."
# }

# LIKED_ARTICLES = {}



def get_all_articles() -> List:
    with open("app\storage.json") as file:
        data = json.load(file)
    return data.get("articles")

def adaptor(data: List) -> Dict:
    result = {}
    for article in data:
        result[article.get("id")]=article.get("content")
    return result
print(adaptor(get_all_articles()))



def add_article(article: str, articles) -> None:
    article_id = len(articles) + 1

    articles[article_id] = article


def like_article(article_id) -> None:
    article_content = ARTICLES.get(article_id)
    add_article(article_content, LIKED_ARTICLES)


def get_all_like_articles() -> List:
    return LIKED_ARTICLES


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
        add_article(article, ARTICLES)
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