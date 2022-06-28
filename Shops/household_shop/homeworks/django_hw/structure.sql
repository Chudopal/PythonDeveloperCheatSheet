-- Сделайте пользователя manager в PostgreSQL следующей командой:
CREATE USER manager WITH ENCRYPTED PASSWORD 'manager';

-- Дайте новому пользователю права в новой базе данных командой:
GRANT ALL PRIVILEGES ON DATABASE bank_system TO manager;

-- PORT может оказаться у вас другим, его можно посмотреть в БД командой:
SELECT setting FROM pg_settings WHERE name = 'port';