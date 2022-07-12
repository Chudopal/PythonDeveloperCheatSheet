"""
Перад вамі вэб-старонка беларускай бібліятэкі.
Але ж у ёй нешта не працуе.
Калі хочаш паглядеть чыесьці кнігі, нічога не атрымоўваецца.
Зразумейце, як працуе гэтая праграмма, як захоўвае дадзеныя, ды
як атмалёўваюцца тэмплэйты.
Спраўце памылкі ды зрабіце гэта, змяніўшы як мага менш коду.

Крыху карысных спасылак:
аб тэмплэйтах - https://flask-russian-docs.readthedocs.io/ru/latest/tutorial/templates.html
аб app.route ды <int:author_id> - https://flask-russian-docs.readthedocs.io/ru/latest/quickstart.html#id2
аб render_tamplate - https://flask-russian-docs.readthedocs.io/ru/latest/quickstart.html#id7

Зручней працаваць, калі ўключаны рэжым дэбагу: https://flask-russian-docs.readthedocs.io/ru/latest/quickstart.html#debug-mode

=)
"""

import json
from typing import Dict
from typing import List
from flask import Flask
from flask import request
from flask import render_template


# STORAGES BLOCK

class BaseJsonStorage:

    def __init__(
        self, file_path: str, data_path: List
    ) -> None:
        self.file_path = file_path
        self.data_path = data_path
        self.data = self._get_data()
    
    def _get_data(self) -> Dict:
        base_data = self._read_file()
        return self._extract_data(
            base_data
        )

    def _read_file(self) -> Dict:
        with open(self.file_path) as file:
            data = json.load(file)
        return data
    
    def _extract_data(self, data: Dict) -> Dict:
        result = data
        for step in self.data_path:
            result = result.get(step, {})
        return result


class JsonAuthorsStorage(BaseJsonStorage):

    def get_authors(self, **params) -> Dict:
        result = self.data
        for key, value in params.items():
            if value:
                result = list(filter(
                    lambda item: str(item.get(key)) == str(value),
                    result.values()
                ))
        return result

    def get_author_by_id(self, author_id: int):
        return self.data.get(str(author_id))


class JsonBooksStorage(BaseJsonStorage):

    def get_book_by_id(self, book_id: int) -> Dict:
        return self.data.get(str(book_id))
    
    def get_books(self, **kwargs) -> Dict:
        result = self.data
        for key, value in kwargs.items():
            if value:
                result = dict(filter(
                    lambda item: str(item[1].get(key)) == str(value),
                    result.items()
                ))
        return result


# CONFIGURATION BLOCK

app = Flask(__name__)

authors_storage = JsonAuthorsStorage(
        file_path='storage.json',
        data_path=("4_task", "authors")
)

books_storage = JsonBooksStorage(
        file_path='storage.json',
        data_path=("4_task", "books")
)


# FLASK ROUTES BLOCK

@app.route("/authors")
def get_authors():

    authors = authors_storage.get_authors(
        **request.args
    )

    return render_template(
        "4_task/authors.html",
        authors=authors
    )


@app.route("/authors/<int:author_id>")
def get_author_detail(author_id: int):
    
    author = authors_storage.get_author_by_id(
        author_id=author_id
    )
    
    books = books_storage.get_books(
        author_id=author_id
    )
    
    return render_template(
        "4_task/author_datail.html",
        books=books,
        **author
    )


@app.route("/books/<int:book_id>", )
def get_book_detail(book_id: int):

    book = books_storage.get_book_by_id(
        book_id=book_id
    )

    author = authors_storage.get_author_by_id(
        book.get("author_id")
    )

    return render_template(
        "4_task/book_detail.html",
        author_name=author.get("name"),
        **book
    )


app.run(port=5000)
