### Создайте шаблон для магазина, в который можно добавлять продукты через телеграм-бота.
1. Создайте проект джанго
2. Установите `pytelegrambotapi` командой:
  ```
  pip install pytelegrambotapi
  ```
3. Сделайте приложение `products`
4. Сделайте модель продукта, производителя и тега, которые будут включать:
  - Продукт
    - название продукта - непустое поле
    - описание - может быть пустым
    - грамовку/количество штук - может быть не задано пользователем, по умолчанию 1
    - цену - непустое поле
    - производителя - непустое поле
    - уникальный идентификатор(uuid или id) - выдается самой системой по умолчанию
    - тег - ненулевое значение
  - производитель:
    - только название
  - тег:
    - название
    - (extra) количество - количество товаров данного тега, с которого будет происходить скидка
    - (extra) скидка - скидка, которая будет применена, в случае выбора определенного количества товаров данного тега 
5. Сделайте шаблоны для просмотра всех продуктов по url `\products`, по этому url должна отображаться информация формата "название_продукта - цена"
6. Сделайте фильтра для url `\products` по цене, например:
    - `\products?price_gt=20&price_lt=50` - вывод всех товаров, стоимость которых больше 20 и меньше 50, не включая продукты, стоимость которых 20 и 50
    - `\products?price_gte=20&price_lte=50` - вывод всех товаров, стоимость которых больше 20 и меньше 50, включая продукты, стоимость которых 20 и 50
    - `\products?tags=computers,health,sport` - вывод всех товаров, у которых есть теги health, computers, sport
    Должна быть возможность комбинировать теги, т.е. получить, например, продукты, которые принадлежат тегам health, computers, sport и имеют стоимость больше 20 и меньше 50, включая стоимость 50
7. Сделайте url `\products\<str: product_id>`, по которому можно посмотреть подробную информацию о продукту
8. Создайте файл `admin_bot.py` в приложении products
9. Получите токен для телеграм-бота (ссылка как сделать и как использовать: https://xakep.ru/2021/11/28/python-telegram-bots/)
10. Напишите бота, через который "админ" сможет добавлять продукты в магазин. Бот должен принимать информацию о продукте и заносить ее в БД. Причем если админ не вводит обязательные параметры, бот просит его ввести это поле заново.
11. Выбор тега и производителя сделать через types.InlineKeyboardButton (почитать можно тут, но у автора беды с бошкой потому там все будет работать плохо, но суть ясна: https://habr.com/ru/post/442800/)
12. Взаимодействие с БД сделать через Django ORM и в приложении, и в Боте
13. TELEGRAM_TOKEN брать из settings.py, НО В КОММИТЫ НИ В КОЕМ СЛУЧАЕ НЕ ДОБАВЛЯТЬ ЕГО!
### Удачи =)
