-- Создание таблиц

-- Создаем таблицу doctors

CREATE TABLE doctors(
    uuid uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
    name CHARACTER VARYING(256),
    category INTEGER NOT NULL CHECK (0 < category and category < 4),
    position CHARACTER VARYING(256)
);

-- Создаем таблицу patients
CREATE TABLE patients(
    uuid uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
    name CHARACTER VARYING(256),
    birth_date DATE,
    weight FLOAT NOT NULL CHECK (10 < weight and weight < 300),
    height FLOAT NOT NULL CHECK (50 < height and height < 220),
    sex CHARACTER VARYING(6)
);


-- Создаем таблицу anmnesis
CREATE TABLE anamnesis(
    patient_uuid uuid REFERENCES patients(uuid),
    doctor_uuid uuid REFERENCES doctors(uuid),
    diagnosis TEXT,
    treatment TEXT
);

-- Заполняем таблицы данными
-- Заполняем таблицу doctors
INSERT INTO doctors(name, category, position) 
VALUES ('Bob', 1, 'Surgeon'),
    ('Gordon', 2, 'Pediatrician'),
    ('Alice', 1, 'Ophthalmologist');

-- Заполняем таблицу patients
INSERT INTO patients(name, birth_date, weight, height, sex)
VALUES ('Dima', '1996-08-06', 65, 170, 'Male'),
    ('Den', '1995-05-15', 70, 175, 'Male'),
    ('Vika', '1998-01-18', 50, 168, 'Female'),
    ('Alina', '1995-04-04', 60, 180, 'Female');

-- Заполняем таблицу anamnesis

INSERT INTO anamnesis
VALUES('d3d7e985-6199-47ce-8acc-1c7455fa6170', '0b7bed13-a62a-4616-98ad-45187a0b612b',
       'broken arm', 'Plaster, bandage, rest');

INSERT INTO anamnesis
VALUES('df0d959b-cbbd-4a18-a977-94dcece92b76', '0b7bed13-a62a-4616-98ad-45187a0b612b',
    'Ankle ligament injury', 'Peace, do not create stress');

INSERT INTO anamnesis
VALUES('9fb13b72-32aa-45ec-b51e-44e07836109c', 'a1b940d2-8707-4dc5-a626-88bb9799f160',
    'Inflammation of the mucous membrane of the eye', 'Take anti-inflammatory drops');

INSERT INTO anamnesis
VALUES('0e003c39-045b-4277-bc73-b25fd85953c6', '61ba1d2d-cab0-4ca7-bb2d-2bd2f473b608',
    'SARS', 'Antiviral agents');

INSERT INTO anamnesis
VALUES('0e003c39-045b-4277-bc73-b25fd85953c6', '0b7bed13-a62a-4616-98ad-45187a0b612b',
    'Ankle ligament injury', 'Peace, do not create stress');

INSERT INTO anamnesis
VALUES('9fb13b72-32aa-45ec-b51e-44e07836109c', '61ba1d2d-cab0-4ca7-bb2d-2bd2f473b608',
       'SARS', 'Antiviral agents');

INSERT INTO anamnesis
VALUES('df0d959b-cbbd-4a18-a977-94dcece92b76', '61ba1d2d-cab0-4ca7-bb2d-2bd2f473b608',
       'SARS', 'Antiviral agents');

INSERT INTO anamnesis
VALUES('d3d7e985-6199-47ce-8acc-1c7455fa6170', '61ba1d2d-cab0-4ca7-bb2d-2bd2f473b608',
       'SARS', 'Antiviral agents');

INSERT INTO anamnesis
VALUES('df0d959b-cbbd-4a18-a977-94dcece92b76', '0b7bed13-a62a-4616-98ad-45187a0b612b', 'Shoulder injury',
      'Peace, do not create stress');

INSERT INTO anamnesis
VALUES('d3d7e985-6199-47ce-8acc-1c7455fa6170', 'a1b940d2-8707-4dc5-a626-88bb9799f160',
       'Inflammation of the eyelids', 'Eyelid massage, ointment');

-- Запросы на получение данных

-- 1. name, category всех докторов
SELECT name, category FROM doctors;

-- 2. Количество всех пациентов
SELECT * FROM patients;

-- 3. Пациенты женского пола
SELECT * FROM patients WHERE sex = 'Female';

-- 4. Отсортировать всех пользователей по birth_date
SELECT name, birth_date FROM patients ORDER BY birth_date;

-- 5. name пациента и name лечащего доктора
SELECT name(patients), name(doctors)
FROM patients JOIN anamnesis
ON patients.uuid = anamnesis.patient_uuid
JOIN doctors
ON doctors.uuid = anamnesis.doctor_uuid;

-- 6. name, диагноз пациентов с максимальным ростом (доп: сделать VIEW)
CREATE VIEW get_name_diagnosis AS
SELECT name, diagnosis, height
FROM patients JOIN anamnesis
ON patients.uuid = anamnesis.patient_uuid
WHERE height = (
   SELECT MAX(height) FROM patients
);

SELECT * FROM get_name_diagnosis;

-- 7. Вывести treatment, имт пользователя, среднее имт по больнице для всех пользователей,
-- у которых имт выше среднего в больнице
SELECT name, (weight / ((height * 0.01) * (height * 0.01))), (SELECT AVG((weight / ((height * 0.01) * (height * 0.01)))) FROM patients)
FROM patients  
WHERE (weight / ((height * 0.01) * (height * 0.01))) >= (
  SELECT AVG((weight / ((height * 0.01) * (height * 0.01)))) FROM patients
)


-- 8. Сделайте представление, которое возвращает name пациента, name доктора, diagnosis, treatment
CREATE VIEW clinic_card AS  
  SELECT patients.name, doctors.name, anamnesis.diagnosis, anamnesis.treatment FROM doctors
  JOIN anamnesis ON doctors.uuid = anamnesis.doctor_uuid
  JOIN patients ON anamnesis.patient_uuid = patients.uuid


-- 9. Количество пациентов, name для каждого доктора
SELECT name, COUNT(DISTINCT anamnesis.patient_uuid) FROM doctors
JOIN anamnesis ON anamnesis.doctor_uuid = doctors.uuid
GROUP BY name
