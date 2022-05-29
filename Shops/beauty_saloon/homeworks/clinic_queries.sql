
-- подгружаем uuid
CREATE EXTENSION "uuid-ossp";

-- создаем таблицу doctors(uuid, name, category, position)
CREATE TABLE doctors(
    uuid uuid UNIQUE DEFAULT uuid_generate_v4(),
    name CHARACTER VARYING(256), category VARCHAR(256), position INT);

-- cоздаем таблицу patients(uuid, name, birth_date, weight, height, sex)
