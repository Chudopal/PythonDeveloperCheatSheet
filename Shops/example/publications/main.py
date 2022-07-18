
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



class Article:
    
    def __init__(self, content, article_id: int):
        self.content = content
        self.article_id = article_id


class FileStorage:

    def __init__(self, path: str, name:str, model: type):
        self.path = path
        self.name = name
        self.model = model
    
    def get(self, number: int=None) -> List:
        data = self._read_file().get(self.name)
        if number == None:
            number = len(data)
        return self._adaptate_to_model(data)[0:number]

    def _adaptate_to_model(self, data: List) -> List:
        return [
            self.model(**article) for article in data
        ]

    def _adaptate_to_file(self, model_list: List) -> List:
        return [
            {
                "content": model.content,
                "article_id": model.artice_id
            } for model in model_list
        ]

    def _read_file(self) -> Dict:
        with open(self.path) as file:
            data = json.load(file)
        return data

    def save(self, articles: List[Article]):
        article_list = self._adaptate_to_file(articles) # получаем в виде json
        data = self._read_file()
        data[self.name] = article_list
        with open(self.path, "w") as file:
            json.dump(data, file)


class PublicationsService:

    def __init__(self, articles_storage, liked_articles_storage):
        self._articles_storage = articles_storage
        self._liked_articles_storage = liked_articles_storage

    def add_article(self, content: str):
        articles = self._articles_storage.get()
        articles.append(
            Article(
                content=content,
                article_id=self._create_article_id(articles)
            )
        )
        self._articles_storage.save(articles)
        
    def _create_article_id(self, articles: List) -> int:
        return len(articles) + 1

    def get_articles(self, number: str):
        self._articles_storage.get(number)

    def like_article(self, article_id: int):
        article = self._find_article(article_id)
        articles = self._liked_articles_storage.get()
        articles.append(
            article
        )
        self._liked_articles_storage.save(articles)


    def _find_article(self, article_id: int):
        articles = self._articles_storage.get()
        result = None
        for article in articles:
            if article.article_id == article_id:
                result = article
                break
        return result

    def get_liked_articles(self, number: int):
        self._liked_articles_storage.get(number)
    

class ConsoleView:

    def __init__(self, service):
        self.service = service

    def run(self):
        choice = None
        message = self.get_menu()
        while choice != 5:
            choice = self.get_choice()
            self.make_choice(choice)
    
    def make_choice(self, choice):
        if ...:
            content = input()
            self.service.add_article()
        elif ...:
            self.service.get_articles()

    def print_articles(self, articles) -> None:
        print("\n".join([f"{article.article_id}. {article.content}"  for article in articles]))


    def get_choice(self, message) -> int:
        return int(input(message))


    def get_menu(self) -> None:
        return ""



def run():
    PublicationsService(
        FileStorage("app/storage.json", "articles", Article),
        FileStorage("app/storage.json", "liked_articles", Article),
    )
    ConsoleView(PublicationsService).run()

run()