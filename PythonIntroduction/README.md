# Введение в Python
1. [О Python в целом](#python_general)
2. [Среда исполнения(virlualenv)](#environment)
3. [Типы данных и операции](#data_types)
4. [Строки и операции над ними](#strigns)
5. [Homework](./homework.py)
6. [Cursed questions](#cursed)

### <a name="python_general">О Python в целом</a>
- **Python** - высокоуровневый(работает с абстракциями, к железу имеет мало отношения) язык программирования общего назначения(не специализируется на какой-то одной задаче, как например регулярные выражения или SQL).
- Python является **интерпретируемым** языком. Это значит, что у программ, написанных на Python, отсутствует стадия **компиляции**(они не переводятся в машинный код или байт-код и не хранятся в бинарном файле). Программы Python выполняются специальной машиной, называемой **интерпретатор**. Самый популярный интерпретатор для Python - это **CPython**(не путать с Cython), отличается от других тем, что во время интерпретирования код на Python считывается и транслируется в язык C. Кроме CPython, есть и другие интерпретаторы:
    - CPython - трансляция в C
    - IronPython - трансляция в C#
    - Jython - трансляция в Java
    - PyPy - трансляция в язык R(самая быстрая реализация Python-интерпретатора на данный момент)
  
  </br>
  Каждый интерпретатор написанный на определенной платформе, позволяет использовать в Python-коде все возможности этой платформы, например CPython позволяет использовать C-библиотека, а Jython позволяет использовать библиотеки платформы JVM(Java, Scala, Kotlin)
- Из-за того, что Python интерпретируемый, его **скорость значительно ниже**, чем у компилируемых языков(например Go и C++) и ниже, чем у компилируемо-интерпретируемых языков(Java, Scala, Kotlin, C#). Однако, Python актуален из-за скорости написания программ на нем.
- Первая программа на Python выглядит следующим образом:
  ```python
  print("Hello World")
  ```
  Данная программа выведет в консоль сообщение `Hello World`.
  Для того, чтобы выводить сообщения используется функция `print()`, а то, что в нее передается(в нашем случае `"Hello World"`), называется аргументом функции.
- Программу `Hello World` можно написать и другим способом:
  ```python
  print("Hello", "World")
  ```
  В данном случае было передано 2 аргумента: `"Hello"`, `"World"`, а Python их сам склеил в одно сообщение и поставил пробел между словами. Если мы захотели бы выводить каждое слово на новой строке, то на пришлось бы поменять "разделитель", который по умолчанию является пробелом. Делается это передачей именованного аргумента `sep` - separator(разделитель):
  ```python
  print("Hello", "World", sep="\n")
  ```
  Данная программа выведет все слова на отдельных строках. В качестве разделителя используется `"\n"` - один из символов [escape-последовательности](https://wiki.dieg.info/escape), обозначающий перевод новой строки.
- Если мы попробуем вывести несколько фраз разными функциями вывода:
  ```python
  print("Hello World")
  print("It's me!")
  ```
  то каждая фраза выведется на новой строке, потому что по умолчанию `print()` ставит символ новой строки `"\n"` в конце каждого сообщения(в сыром виде вывод выглядит как `Hello World\nIt's me!\n`, просто консоль эту фразу делает красивой). Однако можно было бы вывести данную строку по-другому, например `Hello World! It's me!`, в данном случае мы хотим, чтобы вместо символа новой строки, была последовательность символов `"! "`, делается это с помощью именованного аргумента `end`:
  ```python
  print("Hello World", end="! ")
  print("It's me!")
  ```
  теперь вывод будет иметь форму, которую мы хотели: `Hello World! It's me!`. Таким образом можно модифицировать вывод в консоль)
### <a name="environment">Среда исполнения(virtualenv)</a>
- Библиотека - в программировании, это готовое решение, которое можно использовать в своем коде, для использования библиотек есть команда `import`, например довольно часто в коде приходится работать с датами, конечно можно каждый раз писать новый код для дат(код перевода в американскую систему, в европейскую, UTC), однако можно просто воспользоваться готовым решением, которое сразу поставляется с интерпретатором Python:
    ```Python
    import datetime

    current_date = datetime.date.today() # получите нынешнюю дату

    current_date_string = current_date.strftime("%Y-%m-%d") # получите нынешнюю дату в формате строки, например '2022-04-12'
    ```
- Есть библиотеки **предустановленные**, например datetime, они поставляются с интерпретатором Python, а есть библиотеки, которые нужно устанавливать(сторонние), если вы хотите их использовать. Обусловлено это тем, что, например, даты используются в коде часто, и потому они с большой вероятностью понадобятся и их кладут поближе к интерпретатору, однако библиотека для морфологического разбора слов ntlk вряд ли понадобится каждому программисту Python, потому для ее использования, ее нужно **установить**.
- Для установки библиотек используется менеджер зависимостей `pip`, по сути это удобный инструмент с несколькими командами, который контролирует зависимости(установленные библиотеки) в вашем проекте. Его тоже нужно установить, как это сделать, можно посмотреть [тут](https://pythonru.com/baza-znanij/ustanovka-pip-dlja-python-i-bazovye-komandy) или погуглить =)
- Устанавливаются сторонние библиотеки следующей командой:
    ```shell
    $> pip install nltk
    ```

  Данный пример показывает установку последней версии nltk, чтобы проверить установилась ли зависимость, можно в этом же окне терминала зайти в интерпретатор Python и импортировать модуль nltk:
  ```python
    $> python
    >>> import nltk
  ```
  Если зависимость установилась корректно, но ничего не должно появиться, если же возникла ошибка установки и модуль не был установлен, то появится следующее сообщение при импорте:
  ```
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ModuleNotFoundError: No module named 'nltk'
  ```
  Для удаления зависимости используется команда `pip uninstall`, например:
  ```shell
  $> pip uninstall nltk
  ```
- Однако, существует проблема разных версий зависимостей. Например, вы работаете в 2х проектах, 1-й - это чат с виртуальным помощником, 2-й - поисковик. Поисковик начали писать давно, чат-бот с помощником - проект новый, оба приложения базируются на анализе введенной фразы, их алгоритмы построены так, что они получают предложения, разбивают их на слова, находят их исходную форму и дальше каждый анализирует их по-своему. Как мы знаем, за анализ слов, нахождения их исходной формы отвечает модуль nltk, однако в поисковике используется старая версия(например 3.0.0) nltk, у нее совсем другой API(https://ru.wikipedia.org/wiki/API), чем у последней версии, которая используется в чат-боте. И вы устанавливаете в своей системе оба модуля nltk(2.0.2 и последнюю):
  ```shell
  $> pip install nltk==3.0.0 #установит конкретную версию
  $> pip install nltk #установит последнюю версию
  ```
  Однако, интерпретатор Python не разбирается в вашем проекте. Он импортирует всегда только самую последнюю версию версию зависимости, из-за этого ваш проект поисковика сломается, вы его запустить не сможете. Как решать такую проблему, если на уровне интерпретатора нет возможности управлять версиями зависимостей? 
- **Виртуальное окружение** - это интерпретатор, и все библиотеки языка с определенными версиями. Запуская новое виртуальное окружение, вы запускаете новый интерпретатор Python в среде, изолированной от вашей основной системе. Проще говоря, это песочница, в которой вы отделены от внешнего мира. В этой среде вы можете устанавливать любую зависимость, которая вам нужна в этом конкретном проекте. Например, для чат-бота будет окружение с последними версиями библиотек, а в поисковике, будет среда с версиями, которые вам нужны только для этого проекта. Работая над поисковиком, вы активируете среду для этого приложения, захотели поработать над чат-ботом, деактивировали среду для поисковика, и активировали окружение для чат-бота.
- Самое популярное средство виртуализации окружения в Python - это **virtualenv** - это инструмент, который позволяет активировать и деактивировать ваше виртуальное окружение. Установка менеджера окружения делается через pip:
    ```shell
        $> pip install virtualenv
    ```
  Далее в консоле, в папке проекта, пишется:
  ```shell
    $> python -m venv env
  ```
  После этой команды в папке появится директория `env/`, в ней будет отдельный интерпретатор Python и все зависимости, которые вы установите. Однако пока вы не активировали данное окружение, все ваши зависимости будут устанавливаться в систему, для активации, вы должны находиться в директории, в которой находится папка `env/`:
  ```shell
    $> source ./env/bin/activate # MacOs/Linux
    $> .\env\Scripts\activate # Windows
  ```
  После этого в консоли, перед путем в папку появится маркер `(env)`, это будет говорить вам о том, что вы в виртуальном окружении.
  Теперь любая ваши зависимость будет установлена в это окружение, будет независима от системы.
- Для деактивации используется команда `deactivate`, ее просто можно написать в терминале и все:
    ```shell
    $> deactivate
    ```
  Теперь вы снова в окружении системы, а все зависимости упакованы в вашем деактивированном окружении.

### <a name="data_types"> </a> Типы данных и операции
- Объявление переменных происходит следующим образом:
    ```Python
        count = 0 # число
        name = "Bob" # строка
        size = 12.9 # десятичное число
        is_active = True # булевая переменная(с большой буквы)
    ```
- Название переменной - это то, как вы можете обращаться к значению в данной переменной, например:
    ```Python
    students_number = 13
    teachers_number = 1
    people_number = students_number + teachers_number
    ```
- Python - это язык с **динамической сильной** типизацией. Что это значит?
- [Динамическая типизация](https://ru.wikipedia.org/wiki/%D0%94%D0%B8%D0%BD%D0%B0%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B0%D1%8F_%D1%82%D0%B8%D0%BF%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F) - Python не смотрит на типы. Его философия типов называется "утиной": если что-то плавает как утка, квакает как утра, то это утка(противоположность утиной - гусиная типизация, когда важно "видовая" принадлежность). Проще говоря, интерпретатору Python не нужно знать типы переменных, он сам под них подстраивается, единственное, что ему нужно, это чтобы эти типы имели одинаковые названия методов("квакали как утка"). Обычно в статических языках необходимо специфицировать переменную, в которой лежит какое-то значение, например Java:
    ```Java
        int count = 1
    ```
  После такого объявления в переменную нельзя ничего положить, кроме числовых значений, например написать `count = 'one'` уже не получится: это вызовет ошибку компиляции. Однако в Python такое возможно:
  ```Python
  count = 1 # объявили переменную, в которую положили число
  count = 'one' # положили в эту же переменную строку, и все нормально
  ```
+ [Сильная типизация](https://ru.wikipedia.org/wiki/%D0%A1%D0%B8%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F_%D0%B8_%D1%81%D0%BB%D0%B0%D0%B1%D0%B0%D1%8F_%D1%82%D0%B8%D0%BF%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F) - значит, что нельзя проводить операции над значениями разных типов, проще говоря нельзя сложить строку с числом:
    ```Python
    students_number = 13
    teachers_number = '1'
    people_number = students_number + teachers_number
    ```
  Пример выше вызовет ошибку `TypeError: unsupported operand type(s) for +: 'int' and 'str'`, потому что `students_number` - типа **int**, а `teachers_number` - типа **str**, для исправления данной ошибки нужно сказать интерпретатору, что мы хотим иметь дело с int типом, этот прием называется приведением типов:
    ```Python
    students_number = 13
    teachers_number = '1'
    people_number = students_number + int(teachers_number) # привели тип! Получили 14 в ответе
    ```
  Точно так же можно привести int к str:
    ```Python
    students_number = 13
    teachers_number = '1'
    people_number = str(students_number) + teachers_number # привели тип! Получили "131" в ответе
    ```
- Операции над числами:
    ```Python
    5 + 3 # сложение, результат 8
    5 - 3 # разность, результат 2
    5 * 3 # умножение, результат 15
    5 ** 3 # возведение в степень, результат 125
    5 / 3 # деление, результат 1.6666666666666667
    5 // 3 # целочисленное деление, результат 1
    5 % 3 # взятие остатка, результат 2
    ```
- Операции над строками:
    ```Python
    "a" + "b" # конкатенация, результат "ab"
    "a" * 10 # можно делать так, результат "aaaaaaaaaa"
    ```
- Операции над логическими переменными:
    ```Python
    True and False # логическое "и", результат False
    True or False # логическое "или", результат True
    not True # логические "не", результат False
    ```
- (*extra*) Побитовые операции - операции  над представлением значений в битах, можно сдвинуть бит влево(умножить на 2), сдвинуть вправо (отнять один бит), конъюнкция над битами и дизъюнкция над битами:
    ```Python
    4 | 6 # битовое или, результат 6
    4 & 6 # битовое и, результат 4
    4 << 6 # битовый сдвиг влево, результат 256
    4 >> 6 # битовый сдвиг вправо, результат 0
    4 ^ 6 # xor, результат 2
    ```
- Аннотации типов. Иногда удобно проставлять, с каким типом мы имеем дело, это не влияет на работоспособность кода, однако помогает читать код:
    ```Python
        count: int = 8
        name: str = "Bob"
        size: float = 12.5
        is_active: bool = True
    ```

### <a name='strigns'>Строки и операции над ними</a>
- Строки в Python представляют собой набор символов, а значит можно обращаться к символам следующим образом:
  ```python
  name = "Bob"
  o = name[1] # в переменной o будет символ "o"
  ```
  однако строки являются неизменным типом данных:
  ```python
  name = "Bob"
  name[0] = "a" # сделать так нельзя, будет ошибка.
  ```
- Строки это набор символов, а значит их можно приводить ко всем коллекциям:
  ```python
  random_string = "some_string"
  string_list = list(random_string)
  print(string_list) # ['s', 'o', 'm', 'e', '_', 's', 't', 'r', 'i', 'n', 'g']
  ```
- Строки имеют множество особых методов, которые могут помочь с работой с ними:
    - `lower()` - метод для превращения всех букв в слове в маленькие:
      ```python
      name = "alEX"
      lower_name = name.lower()
      print(name) # alEX
      print(lower_name) # alex
      ```
    - `upper()` - переводит все буквы строки в верхний регистр:
      ```python
      name = "alEX"
      lower_name = name.upper()
      print(lower_name) # ALEX
      ```
    - `capitalize()` - делает первую букву строки большой, а остальные маленькими:
      ```python
      name = "alEX"
      lower_name = name.capitalize()
      print(lower_name) # Alex
      ```
    - `join(collection)` - превращает все элементы какой-то коллекции в строку, ставя между ними, как разделитель, строку, к которой применили данный метод:
      ```python
      collection = ["1", "2", "3", "4", "5"]
      some_sep = "! "
      another_sep = "$$$"
      collection_string = some_sep.join(collection)
      another_collection_string = another_sep.join(collection)
      print(collection_string) # 1! 2! 3! 4! 5
      print(another_collection_string) # 1$$$2$$$3$$$4$$$5
      ``` 
    - `replace(old_label, new_label)` - создает новую строку, где заменяет все old_label на new_label:
      ```python
      name = "alexe"
      changed_name = name.replace("e", "OOO")
      print(changed_name) # alOOOxOOO
      ```
- Интерполяция строк - форматирование строк, где форматирование происходит при помощи [плейсхолдеров](https://blog.calltouch.ru/plejsholdery-chto-eto-takoe-i-stoit-li-ispolzovat/). Если упростить, то это процесс форматирования строк, где данные, которые пока неизвестны, заменяются на определенные символы, которые можно подставить позже. В Python представлены 3 вида интерполяции строк:
  - через `%`:
    ```python
    # придумали шаблон, где заменили все неизвестные данные на плейсхолдеры
    template = "%s is %s. He is %s."
    ...
    # спустя какое-то время появились данные
    name = "Alex"
    age = 22
    job = "engineer"

    sentence = template % (name, age, job) # подставили в шаблон все данные и положили в переменную
    # важно помнить, что сам шаблон при этом не меняется
    # так как строки это неизменяемый тип данных.
    # этот шаблон потом можно переиспользовать в другом месте.
    print(sentence) # Alex is 22. He is engineer.
    ```
    Интерполяция через % это довольно старый вид интерполяции, он используется только в тех случаях, где безопасность данных играет малую роль, так как он уязвим к [SQL-инъекциям](https://ru.wikipedia.org/wiki/%D0%92%D0%BD%D0%B5%D0%B4%D1%80%D0%B5%D0%BD%D0%B8%D0%B5_SQL-%D0%BA%D0%BE%D0%B4%D0%B0)
  - через метод `format()`:
    ```python
    # придумали шаблон, где заменили все неизвестные данные на плейсхолдеры
    template = "{} is {}. He is {}."
    ...
    # спустя какое-то время появились данные
    name = "Alex"
    age = 22
    job = "engineer"

    sentance = template.format(name, age, job) # подставили в шаблон все данные и положили в переменную
    print(sentance) # Alex is 22. He is engineer.
    ```
  - f-строки. При данном способе интерполяции необходимо объявлять используемые переменные до шаблона:
    ```python
    # Сначала объявляем переменные
    name = "Alex"
    age = 22
    job = "engineer"
    
    setnance = f"{name} is {age}. He is {job}."
    
    print(setnance) # Alex is 22. He is engineer.
    ```
    Этот способ не создает промежуточного шаблона, а сразу подставляет данные, при объявлении шаблона.
  - (extra) Операции можно выполнять прямо в шаблонах, например данный код является валидным:
    ```python
    name = "Alex"
    weight = 59
    height = 1.78

    sentance_1 = f"{name}'s BMI is {weight/(height**2):.2f}." # вычисляем формулу прямо в строке!

    sentance_2 = "{}'s BMI is {:.2f}.".format(name, weight/(height**2))

    sentance_3 = "%s's BMI is %.2f." % (name, weight/(height**2))

    print(sentance_1)
    print(sentance_2)
    print(sentance_3)
    ```
    Кроме того в данном примере заданы органичения на вывод вещественной части чисел, в случаях format и f-строк, это делается через `:.2f` - вывести 2 знака после запятой, в случе `%`, это просто `%.2f`. Если их убрать(поэксперементируйте), запись вещественной части будет слишком большой. Можно писать любое число вместо двойки, которое будет обозначать количество символов после запятой, которое вам удобно.
  - Это основные виды интерполяции строк, однако каждый из них имеет свои подтипы, которые можно найти в сети Internet =), они не так часто используются, так что я не вижу смысла ими здесь загружать голову.

### <a name='cursed'>Cursed questions</a>
1. Чем Python отличается от остальных языков общего применения?
2. Какие есть интерпретаторы Python? Какой самый популярный?
3. Какие типы данных есть в Python?
4. Что такое виртуальное окружение?
5. Что произойдет при исполнении следующего кода:
  ```python
  a = 5
  b = "6"
  print((a * 3) + (b * 3))
  ```
6. Какие существуют методы интерполяции строк? В чем их разница?
7. Как перевести все буквы в строке в малый регистр?