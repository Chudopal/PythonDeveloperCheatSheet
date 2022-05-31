-- так помечаются комменты в sql

-- создаем таблицу users
CREATE TABLE users(
    name CHARACTER VARYING(256),
    uuid uuid UNIQUE DEFAULT uuid_generate_v4()
);

-- создаем таблицу accounts
CREATE TABLE accounts(
    iban CHARACTER VARYING(32) NOT NULL UNIQUE,
    amount INTEGER NOT NULL CHECK (amount > 0),
    currency CHARACTER VARYING(3) DEFAULT 'usd'
);

-- создаем таблицу cards
CREATE TABLE cards(
    user_uuid uuid NOT NULL REFERENCES users(uuid),
    iban CHARACTER VARYING(32) NOT NULL REFERENCES accounts(iban),
    number CHARACTER VARYING(16) NOT NULL UNIQUE,
    cvv INTEGER NOT NULL CHECK(cvv > 0 AND cvv < 1000), -- проверка чтобы cvv был больше 0 и меньше 1000
    exp_date timestamp NOT NULL -- храним дату
);

-- заполняем таблицы данными
-- заполнем таблицу пользователей
INSERT INTO users(name) VALUES
('Bob'),
('Alice'),
('Alex');

-- заполняем таблицу счетов
INSERT INTO accounts VALUES
('qwerty1', 100, 'usd'),
('qwerty2', 200, 'byn');

-- заполняем таблицу карт, с данными из users 
INSERT INTO cards(user_uuid, iban, number, cvv, exp_date)
SELECT uuid, 'qwerty1', '4242424242424242', 777, '2024-12-01'
FROM users WHERE name='Alex';

INSERT INTO cards(user_uuid, iban, number, cvv, exp_date)
SELECT uuid, 'qwerty1', '4343434343434343', 666, '2026-12-01'
FROM users WHERE name='Alex';

INSERT INTO cards(user_uuid, iban, number, cvv, exp_date)
SELECT uuid, 'qwerty1', '4444444444444444', 888, '2023-12-01'
FROM users WHERE name='Alex';

INSERT INTO cards(user_uuid, iban, number, cvv, exp_date)
SELECT uuid, 'qwerty2', '4545454545454545', 999, '2024-12-01'
FROM users WHERE name='Bob';

INSERT INTO cards(user_uuid, iban, number, cvv, exp_date)
SELECT uuid, 'qwerty2', '4646464646464646', 101, '2027-12-01'
FROM users WHERE name='Alice';

INSERT INTO cards(user_uuid, iban, number, cvv, exp_date)
SELECT uuid, 'qwerty2', '4747474747474747', 121, '2028-12-01'
FROM users WHERE name='Alice';


-- запросы на получение данных

-- 1.получение данных всех пользователей
SELECT * FROM users;

-- 2.получение данных всех карт
SELECT * FROM cards;

-- 3.получение количества всех карт
SELECT COUNT(*) as card_number FROM cards;

-- 4.получение количества всех пользователей
SELECT COUNT(*) as user_number FROM users;

-- 5.получение карт, привязанных к определенному счету
SELECT * FROM cards WHERE iban = 'qwerty2';

-- 6.получение всех карт определенного пользователя
SELECT name, users.uuid, number, cvv, exp_date
FROM cards JOIN users
ON cards.user_uuid = users.uuid
WHERE name = 'Alex';

-- 7.получение количества карт определенного пользователя
SELECT COUNT(*) as card_number
FROM cards JOIN users
ON cards.user_uuid = users.uuid
WHERE name = 'Alex';

-- 8.получение карты с наибольшим exp_date для определенного пользователя
SELECT name, users.uuid, number, cvv, exp_date
FROM cards JOIN users
ON cards.user_uuid = users.uuid
WHERE exp_date = (
    SELECT MAX(exp_date) FROM cards JOIN users
    ON cards.user_uuid = users.uuid
    WHERE name = 'Alex'
);

-- 9.получаем количество карт для каждого пользователя
SELECT name, COUNT(number) as cards_number
FROM users JOIN cards
ON users.uuid = cards.user_uuid
GROUP BY name;

-- 10.Делаем представление (VIEW) для получения name, number, iban
CREATE VIEW get_name_number_iban AS
SELECT name, number, accounts.iban
FROM users JOIN cards
ON users.uuid = cards.user_uuid
JOIN accounts
ON cards.iban = accounts.iban;

-- получаем данные из представления
SELECT * FROM get_name_number_iban;
