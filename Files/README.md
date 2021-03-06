# Работа с файлами
1. [Виды файлов](#files)
2. [Работа с файлами](#work_files)

### <a name='files'> Виды файлов </a>
- Текстовые файлы - файлы с расширением `.txt`. Содержат просто какой-то текст внутри, который можно считать или записать. Пример:
    ```
    Чтобы приготовить простой хлеб нужно 3 стакана муки, 0.25 грамм дрожжей, 1.5 стакана теплой воды. Смешать все ингридиенты и тщательно замесить, закрыть тканью и оставить на один час в тёплом помещении, замесить ещё раз, положить на противень и поставить в духовку. Готовить 180 минут.
    ```
- XML файлы - файлы для хранения данных с расширением `.xml`, можно хранить списки элементов или словари в специальной фаорме, пример xml-файла для рецепта:
    ```xml
    <recipe name="хлеб" cooktime="180min">
        <title>
            Простой хлеб
        </title>
        <composition>
            <ingredient amount="3" unit="стакан">Мука</ingredient>
            <ingredient amount="0.25" unit="грамм">Дрожжи</ingredient>
            <ingredient amount="1.5" unit="стакан">Тёплая вода</ingredient>
        </composition>
        <instructions>
            <step>
                Смешать все ингредиенты и тщательно замесить. 
            </step>
            <step>
                Закрыть тканью и оставить на один час в тёплом помещении. 
            </step>
            <step>
                Замесить ещё раз, положить на противень и поставить в духовку.
            </step>
        </instructions>
    </recipe>

    ```
    Здесь все разбивается на теги(специальные структуры, заключенные в `<>`), по ним и достаются данные. В данный момент такой формат данных считается устаревшим, однако кое-где его все еще можно встретить.
- JSON-файлы - более современный способ хранения данных, имеет расширение `.json`. Словар в Python - это по сути JSON, список - это тоже JSON. Однако множества и кортежи - не являются частью JSON. Пример:
    ```JSON
    {
        "title": "Простой хлеб",
        "composition": [
            {
                "amount": 3,
                "unit": "стакан",
                "ingredient": "Мука"
            },
            {
                "amount": 0.25,
                "unit": "грамм",
                "ingredient": "Дрожжи"
            },
            {
                "amount": 1.5,
                "unit": "стакан",
                "ingredient": "Тёплая вода"
            }

        ],
        "instructions" : [
            "Смешать все ингредиенты и тщательно замесить.",
            "Закрыть тканью и оставить на один час в тёплом помещении.",
            "Замесить ещё раз, положить на противень и поставить в духовку."
        ]

    }
    ```
    JSON - это не только файлы, но и формат данных, у которого есть свои особенности:
    1. Строки берутся в двойные ковычки("_");
    2. Ключами могут быть только строки, цыфры или другие структуры - не могут;
    3. Начинаться и заканчиваться JSON файл должен открываютщей фигурной скобкой{ и закрывающейся};
    4. Он чем-то похож на словарь, однако там можно использовать только списки и словари из доступных в Python коллекций, множества и кортежи - нельзя.


### <a name='work_files'> Работа с файлами </a>
- Работа с текстовыми файлами происходит при помощи встроенной функции `open(path, mode)`, path - это путь к файлу, а mode - это режим доступа: чтение("r") или запись("w"), по умолчанию режим доступа - чтение. Считывать файл можно так:
    ```python
    file = open("1.txt") # открываем файл
    content = file.read() # читаем все содержимое файла

    print(content) # HERE IS JOHNNY - вывели содержимое файла

    file.close() # закрыли файл
    ```
    Очень важно после работы с файлами - закрыть их. Если этого не сделать, то множество открытых файлов будет висеть в памяти компьютера, пока она не закончится. Потому всегда нужно указывать команду `file.close()`, после получения данных. Это настолько распространено, что в Python сделали даже отдельную структуру для таких случаем, которая называется **менеджером контекста** - ключевое слово `with`. Предыдущий код можно переписать следующим образом:
    ```python
    with open("1.txt") as file: # открыли файл через менеджер контекста 
        content = file.read() # здесь соединение с файлом еще есть, читаем оттуда данные
    # здесь соединение с файлом уже закрыто, все данные в памяти    

    print(content) # HERE IS JOHNNY - вывели содержимое файла
    ```
    Менеджер контекста закроет за нас этот файл, как только мы получим оттуда все нужные данные. Чтобы записать данные в файл нужно указать режим доступа: "w" и воспользоваться специальным методом `write(content)` файла:
    ```python
    with open("1.txt", "w") as file: 
        file.write("HERE IS JOHNNY\n"*10) # запишет фразу "HERE IS JOHNNY" в файл 1.txt
    ```
    файл `1.txt`:
    ```txt
    HERE IS JOHNNY
    HERE IS JOHNNY
    HERE IS JOHNNY
    HERE IS JOHNNY
    HERE IS JOHNNY
    HERE IS JOHNNY
    HERE IS JOHNNY
    HERE IS JOHNNY
    HERE IS JOHNNY
    HERE IS JOHNNY

    ```
    Кроме стандартного режима записи "w", который перезаписывает файл, есть режим доступа "a", который не перезаписывает файл, а добавляет в него информацию:
    ```python
    with open("1.txt") as file:
    content = file.read()

    print(content) # This is base information

    with open("1.txt", "a") as file:
        file.write("\nAdditional information")

    with open("1.txt") as file:
        content = file.read()

    print(content) # This is base information\nAdditional information
    ```
- Работа с JSON выполняется через специальный модуль json. Этот модуль позволяет сохранять, получать, декодировать json-файлы и структуры. Открытие json-файла происходит при помощи менеджера контекста как и в случае простых текстовых файлов, однако получение данных происходит через метод `json.load(file)`, где file - это файл, в котором хранится json, например:
    ```python
    import json

    with open("1.json") as file: # открываем файл json
        content = json.load(file) # с помощью json.load загружаем содержимое файла

    print(content) # {'people': [{'name': 'Alex', 'age': 22}, {'name': 'Bob', 'age': 10}, {'name': 'Alice', 'age': 27}]} - вывели информацию из файла
    ```
    Запись в json так же происходит через модуль json, при помощи метода `json.dump(data, file)`, data - информацию, которую надо сохранить, file - файл, в который надо сохранить:
    ```python
    import json

    data = {
        "people": [
            {"name": "Alex", "age": 22},
            {"name": "Bob", "age": 10},
            {"name": "Alice", "age": 27}
        ]
    }

    with open("1.json", "w") as file: # поменяли режим доступа на "w"
        json.dump(data, file) # записали в файл информацию
    ```
    Файл 1.json:
    ```json
    {"people": [{"name": "Alex", "age": 22}, {"name": "Bob", "age": 10}, {"name": "Alice", "age": 27}]}
    ```
    При записи все старые данные из файла удаляются, и записываются новые. Если нам нужно именно дополнить иформацию в json, нужно сначала считать старую информацию из файла, изменить ее, как нам нужно и записать ее:
    ```python
    import json

    with open("1.json") as file: # получаем старые данные
        content = json.load(file)

    print(content) # {'people': [{'name': 'Alex', 'age': 22}, {'name': 'Bob', 'age': 10}, {'name': 'Alice', 'age': 27}]} - вывели информацию из файла

    content.get("people").append({"name": "Andry", "age": 40}) # добавили новую информацию к существующей

    with open("1.json", "w") as file: # записали в файл
        json.dump(content, file, indent=4) # indent = 4 поможет нам форматировать файл, чтобы его было проще читать. Он установит отступы равные 4 пробела
    ```
    Файл 1.json теперь выглядит так:
    ```json
    {
        "people": [
            {
                "name": "Alex",
                "age": 22
            },
            {
                "name": "Bob",
                "age": 10
            },
            {
                "name": "Alice",
                "age": 27
            },
            {
                "name": "Andry",
                "age": 40
            },
            {
                "name": "Andry",
                "age": 40
            }
        ]
    }
    ```
    Добавился новый человек.
