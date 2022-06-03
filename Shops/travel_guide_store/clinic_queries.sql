CREATE EXTENSION "uuid-ossp";

-- создаем таблицу doctors

CREATE TABLE doctors(
    uuid uuid UNIQUE DEFAULT uuid_generate_v4() PRIMARY KEY, 
    name CHARACTER VARYING(100),   
    category CHARACTER VARYING(30), 
    position CHARACTER VARYING(15));

-- создаем таблицу patients
CREATE TABLE patients(
    uuid uuid DEFAULT uuid_generate_v4() PRIMARY KEY, 
    name CHARACTER VARYING(100), 
    birth_date DATE, 
    weight SMALLINT CHECK(weight>10 AND weight <300), 
    height SMALLINT CHECK (height >50 AND height<220), 
    sex CHARACTER VARYING(3));

-- создаем таблицу anamnesis
CREATE TABLE anamnesis(
    patient_uuid uuid NOT NULL REFERENCES patients (uuid),
    doctor_uuid uuid NOT NULL REFERENCES doctors (uuid),
    diagnosis TEXT,
    treatment TEXT);

-- заполняем таблицы данными
-- заполнем таблицу докторов
INSERT INTO doctors (name, category, position)
VALUES ('Владимир', 'первая', 'хирург'), ('Елена', 'первая', 'терапевт'), ('Степан', 'высшая', 'травматолог');

-- заполняем таблицу patients
INSERT INTO patients (name, birth_date, weight, height, sex) 
VALUES ('Катя', '1986-12-01', 65, 177, 'жен' ), 
('Артем', '1988-10-15', 76, 180, 'муж' ), 
('Таня', '1999-12-06', 51, 174, 'жен'),
('Оля', '2001-06-18', 50, 178, 'жен');

--заполняем таблицу анамнезов
INSERT INTO anamnesis (patient_uuid, doctor_uuid, diagnosis, treatment)
VALUES
(
  (SELECT uuid FROM patients WHERE name='Катя'),
  (SELECT uuid FROM doctors WHERE name='Елена'),
  'повышенная температура',
  'принимать Ибупрофен'
);
INSERT INTO anamnesis (patient_uuid, doctor_uuid, diagnosis, treatment)
VALUES
(
  (SELECT uuid FROM patients WHERE name='Оля'),
  (SELECT uuid FROM doctors WHERE name='Владимир'),
  'Боль при сгибании руки',
  'Сделать снимок и применять мазь'
);
INSERT INTO anamnesis (patient_uuid, doctor_uuid, diagnosis, treatment)
VALUES
(
  (SELECT uuid FROM patients WHERE name='Катя'),
  (SELECT uuid FROM doctors WHERE name='Владимир'),
  'Ожог',
  'Мазать мазью и носить повязку'
);
INSERT INTO anamnesis (patient_uuid, doctor_uuid, diagnosis, treatment)
VALUES
(
  (SELECT uuid FROM patients WHERE name='Таня'),
  (SELECT uuid FROM doctors WHERE name='Владимир'),
  'Ожог',
  'Мазать мазью и носить повязку'
);
INSERT INTO anamnesis (patient_uuid, doctor_uuid, diagnosis, treatment)
VALUES
(
  (SELECT uuid FROM patients WHERE name='Катя'),
  (SELECT uuid FROM doctors WHERE name='Степан'),
  'Перелом руки',
  'Оперативное вмешательство'
);
INSERT INTO anamnesis (patient_uuid, doctor_uuid, diagnosis, treatment)
VALUES
(
  (SELECT uuid FROM patients WHERE name='Артем'),
  (SELECT uuid FROM doctors WHERE name='Елена'),
  'Кашель и насморк',
  'Пропить курс антибиотиков'
);
INSERT INTO anamnesis (patient_uuid, doctor_uuid, diagnosis, treatment)
VALUES
(
  (SELECT uuid FROM patients WHERE name='Таня'),
  (SELECT uuid FROM doctors WHERE name='Степан'),
  'Боль при сгибании ноги',
  'Сделать снимок'
);
INSERT INTO anamnesis (patient_uuid, doctor_uuid, diagnosis, treatment)
VALUES
(
  (SELECT uuid FROM patients WHERE name='Артем'),
  (SELECT uuid FROM doctors WHERE name='Владимир'),
  'Абсцесс на правой щеке',
  'Хирургическое вмешательство'
);
INSERT INTO anamnesis (patient_uuid, doctor_uuid, diagnosis, treatment)
VALUES
(
  (SELECT uuid FROM patients WHERE name='Оля'),
  (SELECT uuid FROM doctors WHERE name='Елена'),
  'Мед.комиссия',
  'Стандартный осмотр и анализы'
);
INSERT INTO anamnesis (patient_uuid, doctor_uuid, diagnosis, treatment)
VALUES
(
  (SELECT uuid FROM patients WHERE name='Катя'),
  (SELECT uuid FROM doctors WHERE name='Владимир'),
  'Вросший ноготь',
  'Хирургическое вмешательство'
);

-- запросы
-- 1. получение name, category всех докторов
SELECT name, category FROM doctors;


-- 2. получение количества всех пациентов
SELECT * FROM patients;


-- 3. получение пациентов женского пола
SELECT * FROM patients
WHERE sex='жен';

--4. отсортировать всех пользователей по birth_date
SELECT * FROM patients ORDER BY birth_date;

--5. получение name пациента и name лечащего доктора
SELECT 	patients.name, 	doctors.name FROM patients
INNER JOIN anamnesis ON patients.uuid = anamnesis.patient_uuid
INNER JOIN doctors ON anamnesis.doctor_uuid = doctors.uuid
ORDER BY patients.name;

--6. получение name, диагноз пациентов с максимальным ростом (доп: сделать VIEW)
CREATE VIEW list_diagnosis AS SELECT 	patients.name, 	anamnesis.diagnosis, 	patients.height FROM 	patients 
INNER JOIN anamnesis ON patients.uuid = anamnesis.patient_uuid
SELECT name, diagnosis, height FROM list_diagnosis WHERE height=(SELECT MAX(height) FROM list_diagnosis);
--7. вывести treatment, имт пользователя, среднее имт по больнице для всех пользователей, у которых имт выше среднего в больнице

-- 8. сделайте представление, которое возвращает name пациента, name доктора, diagnosis, treatment
--9. количество пациентов, name для каждого доктора