
-- подгружаем uuid
CREATE EXTENSION "uuid-ossp";

-- создаем таблицу doctors(uuid, name, category, position)
CREATE TABLE doctors(
    uuid uuid UNIQUE DEFAULT uuid_generate_v4(),
    name CHARACTER VARYING(256), category VARCHAR(256), position TEXT);

-- cоздаем таблицу patients(uuid, name, birth_date, weight, height, sex)
CREATE TABLE patients(
    uuid uuid UNIQUE DEFAULT uuid_generate_v4(),
    name CHARACTER VARYING(256), 
    birth_date DATE, 
    weight INT NOT NULL CHECK (weight > 10 AND weight < 300),
    height INT NOT NULL CHECK (height > 50 AND height < 220),
    sex VARCHAR(7)
);

-- создаем таблицу anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
CREATE TABLE anamnesis(
    patient_uuid uuid NOT NULL REFERENCES patients (uuid),
    doctor_uuid uuid NOT NULL REFERENCES doctors (uuid),
    diagnosis TEXT,
    treatment TEXT
);

-- заполняем таблицу doctors
INSERT INTO doctors (name, category, position) 
VALUES ('Bob', 'первая', 'дежурный врач'), ('Alice', 'вторая', 'глава отделения' ), ('Alex', 'высшая', 'главврач');

-- заполняем таблицу patients
INSERT INTO patients (name, birth_date, weight, height, sex) 
VALUES ('Robert', '1996-07-01', 85, 177, 'мужской' ), 
('Den', '1988-10-15', 76, 180, 'мужской' ), 
('Anna', '1969-12-26', 70, 164, 'женский'),
('Katerina', '1999-06-18', 56, 175, 'женский');

-- заполняем таблицу anamnesis
INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, '4f14e356-7412-400f-bfaa-ed49954e06d5', 'ОРВИ', 'Теплое питьё'
FROM patients WHERE name='Robert';

INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, '4f14e356-7412-400f-bfaa-ed49954e06d5', 'Радикулит', 'гимнастика для спины, умеренные физические нагрузки'
FROM patients WHERE name='Robert';

INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, '54ff4ce0-0091-4b25-901c-ddad87495a60', 'Межпозвоночная грыжа', 'медикаментозные блокады, лечебная физкультура, физиотерапия'
FROM patients WHERE name='Robert';

INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, '54ff4ce0-0091-4b25-901c-ddad87495a60', 'Перелом ноги', 'пункция, блокада места перелома'
FROM patients WHERE name='Den';

INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, '54ff4ce0-0091-4b25-901c-ddad87495a60', 'Язва', 'снижение кислотности желудка, защита слизистой оболочки, коррекция состояния нервной системы и психической сферы.'
FROM patients WHERE name='Den';

INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, '81aa9fe1-0edb-4dee-88ac-70b920818a43', 'Бронхит', 'антибиотики, муколитики, противокашлевые препараты'
FROM patients WHERE name='Anna';

INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, '81aa9fe1-0edb-4dee-88ac-70b920818a43', 'Гастрит', 'Н2-гистаминоблокаторы, ингибиторы протонной помпы, антациды'
FROM patients WHERE name='Anna';

INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, '81aa9fe1-0edb-4dee-88ac-70b920818a43', 'Гастрит', 'Н2-гистаминоблокаторы, ингибиторы протонной помпы, антациды'
FROM patients WHERE name='Katerina';

INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, '4f14e356-7412-400f-bfaa-ed49954e06d5', 'ОРВИ', 'Теплое питьё'
FROM patients WHERE name='Katerina';

INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, '4f14e356-7412-400f-bfaa-ed49954e06d5', 'ОРВИ', 'Теплое питьё'
FROM patients WHERE name='Den';

-- 1. name, category всех докторов
select name, category from doctors

-- 2. количество всех пациентов
SELECT COUNT(*) as patient FROM patients

-- 3. кол-во пациентов женского пола
SELECT COUNT(*) as patient FROM patients WHERE sex = 'женский'

-- 4. отсортировать всех пользователей по birth_date
SELECT name, birth_date, weight, height, sex  FROM patients  ORDER BY birth_date

-- 5. name пациента и name лечащего доктора
SELECT patients.name AS name_patients, doctors.name AS name_doctors FROM anamnesis
JOIN patients 
ON patients.uuid = anamnesis.patient_uuid     
JOIN doctors 
ON doctors.uuid = anamnesis.doctor_uuid
ORDER BY name_patients

-- 6. name, диагноз пациентов с максимальным ростом (доп: сделать VIEW)
CREATE VIEW patients_diagnosis AS
SELECT name, diagnosis, height, weight, treatment
FROM anamnesis JOIN patients
ON anamnesis.patient_uuid = patients.uuid;

-- запрос к VIEW
SELECT name, diagnosis
  FROM patients_diagnosis
 WHERE height = (SELECT MAX(height) FROM patients_diagnosis)

 -- 7. вывести treatment, имт пользователя, 
 --    среднее имт по больнице для всех пользователей, 
 --     у которых имт выше среднего в больнице

Select ROUND (weight / (height * 0.01 * height * 0.01),2) AS IMT, treatment,
(SELECT SUM(weight / (height * 0.01 * height * 0.01))FROM patients_diagnosis) / 
(SELECT COUNT(treatment)
 FROM patients_diagnosis) AS Среднее_IMT 
 FROM patients_diagnosis 
 WHERE (Select ROUND (weight / (height * 0.01 * height * 0.01),2)) > 
 (SELECT SUM(weight / (height * 0.01 * height * 0.01))FROM patients_diagnosis) / 
(SELECT COUNT(treatment)
 FROM patients_diagnosis)

 -- 8. сделайте представление, которое возвращает name пациента, name доктора, diagnosis, treatment
CREATE VIEW honey_card AS
SELECT patients.name AS name_patient, doctors.name AS name_doctors, diagnosis, treatment
FROM anamnesis 
JOIN patients 
ON anamnesis.patient_uuid = patients.uuid 
JOIN doctors 
ON anamnesis.doctor_uuid = doctors.uuid 

SELECT * FROM honey_card

-- 9. количество пациентов, name для каждого доктора
SELECT name, COUNT(DISTINCT patient_uuid) FROM doctors 
JOIN anamnesis ON anamnesis.doctor_uuid = doctors.uuid
GROUP BY name