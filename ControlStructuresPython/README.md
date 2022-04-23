# Управляющие структуры Python
1. [Операторы сравнения](#comparison)
2. [Операторы ветвления](#statements)
3. [Цикл while](#while)
4. Цикл for
5. [Homework](./homework.py)

### <a name='comparison'>Операторы сравнения</a>
- Операторы сравнения возвращают булевое значение. Оператор - это знак операции, например `==`, `>`, `!=`. Операнды - сравниваемые значения, в случае выражение `5 == 5` оператор - `==`, операнды - `5` и `5`.

- Оператор равенства `==`, возвращает `True` если операнды равны:
    ```python
    print(5 == 5) # True
    print(5 == 6) # False

    print([1,2,3] == [1,2,3]) # True
    ```

- Оператор неравенства `!=`, возвращает `True`, если операнды не равны:
    ```python
    print(5 != 6) # True
    print(5 != 5) # False
    ```

- Оператор тождественности `is`, на простых структурах данных работает так же как и `==`, но на самом деле этот оператор сравнивает адреса в памяти, например:
    ```python
    print(5 is 5) #True
    ```
    но
    ```python
    [1,2,3] == [1,2,3] # True
    [1,2,3] is [1,2,3] # False
    a = b = [1,2,3]
    a is b # True
    ```
    В последнем выражении `True` потому что оба операнда(`a`, `b`) указывают на одну структуру данных.

- Группа операторов: больше `>`, больше или равно `>=`, меньше `<`, меньше или равно `<=`:
    ```python
    print(5 < 6) # True
    print(5 < 4) # False
    print(4 <= 4) # True

    print(5 > 4) # True
    print(5 > 6) # False
    print(5 >= 5) # True
    ```
    Кроме того данные операторы можно комбинировать, можно писать следующие структуры:
    ```python
    a = 5
    print(5 <= a <= 10) # True
    print(5 < a < 10) # False
    print(10 <= a <= 5) # Всегда False, при любых значениях a, нет такого числа, которое больше десяти и меньше 5
    ```

- Оператор принадлежности `in`, возвращает `True`, если элемент есть в какой-либо коллекции:
    ```python
    print(1 in [1,2,3]) # True
    print(4 in [1,2,3]) # False

    print(2 in {"Alex": 2}.values()) # True
    print('Alex' in {"Alex": 2}.keys()) # True

    print("a" in "abc") # True, символ в строке тоже можно так искать
    ```

- Так как результатом операций сравнения является булевое значение, к результату можно примерять логические операнды `and`, `or`, `not`:
    ```python
    a = 5
    b = 7
    d_list = [1,2,3,4,5,6]
    print((0 <= a <= 10) and (not (b in d_list))) # True
    ```


### <a name='statements'> Операторы ветвления </a>
- Операторы ветвления - самые базовые логические составляющие вашей программы, они говорят, как программа должна реагировать на данные, которые она принимает.
- Операторы ветвления в Python представлены командой `if`, она еще называется **условным оператором**. После нее пишется условие и исполняемый код. Если условие правдиво `True`, то код исполняется. Условие пишется сразу после `if`, потом ставится двоеточие `:` и на следующей строке, с отступом в один tab, пишется исполняемый код. Чтобы писать код, который не входит в `if`, нужно сместить убрать отступ. Например, программа которая спрашивает желает ли пользователь вывести приветственное сообщение:
    ```python
    name = input("Enter your name: ")
    answer = input("Do you want to see greeting message?(yes/no): ")

    if answer == "yes":
        print("Hello", name, sep=', ', end='!')

    if answer == "no":
        print("OK.")
    ```
    Если запустить данную программу, ввести свое имя, а потом ответить `yes`, то программы выведет `"Hello, name!"` - исполнится первое условие. Если ответить `no`, то программа не выведет `"Hello, name!"`, а просто напишет `"OK."` - первое условие не исполнится, а второе исполнится.
    Также можно переписать программу, чтобы она понимала больше ответов, используя коллекции верных и неверных ответов:
    ```python
    name = input("Enter your name: ")
    answer = input("Do you want to see greeting message?(yes/no): ")

    positive_answers = ('yes', 'y', 'yep', 'yeah') # кортеж положительных ответов
    negative_answers = ('no', 'n', 'nope') # кортеж отрицательных ответов

    if answer in positive_answers:
        print("Hello", name, sep=', ', end='!')

    if answer is negative_answers:
        print("OK.")
    ```

- Так же можно сделать так, чтобы при неисполнении какого-либо условия, исполнялся другой код. Для этого есть специальное слово `else`. В нем отсутствует условие, и этот оператор срабатывает, когда условие в конструкции `if` ложно. Он ставится после исполняемого когда в `if`, и после него ставится просто двоеточие `:`. Например, можно переписать нашу программу и сделать ее более читаемой:
    ```python
    name = input("Enter your name: ")
    answer = input("Do you want to see greeting message?(yes/no): ")

    positive_answers = ('yes', 'y', 'yep', 'yeah')
    #negative_answers = ('no', 'n', 'nope')

    if answer in positive_answers:
        print("Hello", name, sep=', ', end='!')
    else:
        print("OK.")
    ```
    Работать она будет так же, если вводить значения `yes`, 'no'.

- Условия могут быть вложены друг в друга. Например наша программа приветствия будет работать не совсем очевидно, если мы ответим на вопрос не `yes`/`no`, а `maybe`. Для исправления этой проблемы можно написать еще одну условную конструкцию:
    ```python
    name = input("Enter your name: ")
    answer = input("Do you want to see greeting message?(yes/no): ")

    positive_answers = ('yes', 'y', 'yep', 'yeah')
    negative_answers = ('no', 'n', 'nope')

    if answer in positive_answers:
        print("Hello", name, sep=', ', end='!')
    else:
        if answer in negative_answers: # вложенная условная конструкция
            print("OK.")
        else:
            print("I don't understand you.")
    ```
    Условия можно улаживать до бесконечности, главное не забывать ставить отступ.

- Если очень вложенных много условий, то код очень быстр может уйти за пределы экрана, для этого в Python введена специальная конструкция `elif` - это совмещение команды `else` и `if`. После нее так же требуется указывать условие исполнение кода. Перепишем наш пример более правильно:
    ```python
    name = input("Enter your name: ")
    answer = input("Do you want to see greeting message?(yes/no): ")

    positive_answers = ('yes', 'y', 'yep', 'yeah')
    negative_answers = ('no', 'n', 'nope')

    if answer in positive_answers:
        print("Hello", name, sep=', ', end='!')
    elif answer in negative_answers: # использование оператора elif
        print("OK.")
    else: # и в этом же коде можно использовать сразу else
        print("I don't understand you.")
    ```
    В нашем примере сразу используются команды `if`, `elif` и `else`. Так делать можно.

### <a name='while'>Цикл while</a>
- Цикл это повторение одного и того же участка кода несколько раз. Количество повторений зависит от какого-то условия.
- Цикл `while` - это простой цикл повторения, сначала пишется ключевое слово `while`, потом условие - пока оно истинно код будет повторяться снова и снова, на следующей строке с отступом 1 `tab` пишется исполняемый код, чтобы убрать код из цикла, нужно сместиться на 1 `tab` из цикла. Пример цикла:
    ```python
    max_number = int(input("Enter the number of 'Hello': "))
    counter = 1

    while counter <= max_number:
        print("Hello №", counter, sep=0)
        counter += 1 # каждый раз увеличиваем счетчик

    print("Thank you!")
    ```
    Данная программа просит ввести пользователя количество слов `Hello`, которое он хочет увидеть, выводит их, а потом пишет `"Thank you!"`. При каждом проходе через исполняемый код переменная `counter` увеличивается на 1. Это делается для того, чтобы цикл завершился ровно на 10 исполнениях. Цикл перед каждым исполнением кода проверяет условие, которое в нем записано `counter <= max_number`, если условие станет ложным, цикл завершится.
- Давайте вспомним программу из прошлого раздела, которая выводит приветствие, вот ее финальный вариант:
    ```python
    name = input("Enter your name: ")
    answer = input("Do you want to see greeting message?(yes/no): ")

    positive_answers = ('yes', 'y', 'yep', 'yeah')
    negative_answers = ('no', 'n', 'nope')

    if answer in positive_answers:
        print("Hello", name, sep=', ', end='!')
    elif answer in negative_answers:
        print("OK.")
    else:
        print("I don't understand you.")
    ```
    Можно переписать ее так, чтобы она на непредусмотренном ответе не завершалась, а просила ввести данные опять и опять и так, пока не будет введен корректный ответ:
    ```python
    # просим ввести имя
    name = input("Enter your name: ")

    # объявили все корректные ответы
    positive_answers = ('yes', 'y', 'yep', 'yeah')
    negative_answers = ('no', 'n', 'nope')
    # для удобства занесем все ответы в один кортеж
    correct_answers = positive_answers + negative_answers

    # объявим пустую переменную ответа, чтобы на условии не было ошибки 
    answer = None

    # построим цикл, который будет повторяться, пока не будет введен корректный ответ
    while answer not in correct_answers:
        # просим ввести ответ
        answer = input("Do you want to see greeting message?(yes/no): ")

        if answer in positive_answers:
            print("Hello", name, sep=', ', end='!')
        elif answer in negative_answers:
            print("OK.")
        else:
            print("I don't understand you.")
            print("Try again...")
    ```
- Так как в цикле `while` есть условная составляющая, не удивительно, что так же есть конструкция `else`. Перепишем нашу программу, чтобы она в конце говорила `Thank you`:
    ```python
    # просим ввести имя
    name = input("Enter your name: ")

    # объявили все корректные ответы
    positive_answers = ('yes', 'y', 'yep', 'yeah')
    negative_answers = ('no', 'n', 'nope')
    # для удобства занесем все ответы в один кортеж
    correct_answers = positive_answers + negative_answers

    # объявим пустую переменную ответа, чтобы на условии не было ошибки 
    answer = None

    # построим цикл, который будет повторяться, пока не будет введен корректный ответ
    while answer not in correct_answers:
        # просим ввести ответ
        answer = input("Do you want to see greeting message?(yes/no): ")

        if answer in positive_answers:
            print("Hello", name, sep=', ', end='!')
        elif answer in negative_answers:
            print("OK.")
        else:
            print("I don't understand you.")
            print("Try again...")
    else:
        print("\nThank you!")
    ```
    Однако ее существование сомнительно, так как можно просто написать эти дефствия после самого цикла.
- Иногда циклы получаются бесконечными, иногда это нужно, но чаще всего это из-за какой-то ошибки программиста в условии. Чтобы остановить программу, которая зависла, или программу, в которой нечаянно появился бесконечный цикл, нужно нажать сочетание клавиш [`ctrl + c`]. Ошибки - это не страшно, главное знать как их починить =)

- С помощью цикла `while` также можно обойти все элементы какой-то коллекции:
    ```python
    users = ["Alex", "Alice", "Bob", "Nikita"]
    i = 0

    while i < len(users):
        print(users[i], "has number", i, "in list")
        i += 1
    ```

### <a name='for'> </a> Цикл for
- Коллекции можно обойти с помошью цикла `while`, однако намного удобнее работать с коллекцями при помощи цикла `for`. Этот инструмент позво