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


-- Заполняем таблицу doctors
INSERT INTO doctors (name, category, position) 
VALUES ('Bob', 'Дантист', 'Дежурный врач'), ('Alex', 'Лор', 'Зав.отделения'), ('Alice', 'Хирург', 'Глав.врач');


-- Запоняем табоицу patients
INSERT INTO patients(name, birth_date, weight, height, sex) 
VALUES ('Sasha','1997-12-03', 65, 180, 'MEN'), ('Dima', '1993-11-05', 87, 186, 'MEN'), ('Olya', '1993-10-25', 56, 174, 'WOMEN'), ('Anna', '2005-05-20', 48, 156, 'WOMEN');


-- Заполняем таблицу anamnes
INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, 'd3488dd4-c2d4-4a37-8862-22ca229e55ba', 'ОРВИ', 'Теплое питьё'
FROM patients WHERE name='Sasha';

INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, 'd3488dd4-c2d4-4a37-8862-22ca229e55ba', 'Радикулит', 'гимнастика для спины, умеренные физические нагрузки'
FROM patients WHERE name='Sasha';

INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, 'd3488dd4-c2d4-4a37-8862-22ca229e55ba', 'Межпозвоночная грыжа', 'медикаментозные блокады, лечебная физкультура, физиотерапия'
FROM patients WHERE name='Sasha';


INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, '2906b866-4d86-471e-b936-326801e369a5', 'Перелом ноги', 'пункция, блокада места перелома'
FROM patients WHERE name='Dima';


INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, '2906b866-4d86-471e-b936-326801e369a5', 'Язва', 'снижение кислотности желудка, защита слизистой оболочки, коррекция состояния нервной системы и психической сферы.'
FROM patients WHERE name='Dima';


INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, '2906b866-4d86-471e-b936-326801e369a5', 'Бронхит', 'антибиотики, муколитики, противокашлевые препараты'
FROM patients WHERE name='Dima';


INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, 'a49f6ca2-229f-421d-b087-8d04c359e529', 'Гастрит', 'Н2-гистаминоблокаторы, ингибиторы протонной помпы, антациды'
FROM patients WHERE name='Olya';


INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, 'a49f6ca2-229f-421d-b087-8d04c359e529', 'Гастрит', 'Н2-гистаминоблокаторы, ингибиторы протонной помпы, антациды'
FROM patients WHERE name='Olya';


INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, 'a49f6ca2-229f-421d-b087-8d04c359e529', 'ОРВИ', 'Теплое питьё'
FROM patients WHERE name='Anna';


INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, 'a49f6ca2-229f-421d-b087-8d04c359e529', 'ОРВИ', 'Теплое питьё'
FROM patients WHERE name='Anna';


--1 Task
SELECT name, category FROM doctors;


--2 Task
SELECT COUNT(*) FROM patients;


--3 Task
SELECT * FROM patients WHERE sex = 'WOMEN'


--4 Task
SELECT * FROM patients ORDER BY birth_date;


--5 Task
SELECT patients.name 
AS new_patients_name, doctors.name FROM anamnesis
JOIN patients ON patients.uuid = anamnesis.patient_uuid
JOIN doctors ON doctors.uuid = anamnesis.doctor_uuid;


--6 Task
CREATE VIEW patients_diagnosis AS
SELECT name, diagnosis, height, weight, treatment 
FROM anamnesis JOIN patients
ON anamnesis.patient_uuid = patients.uuid;


SELECT name, diagnosis
  FROM patients_diagnosis
 WHERE height = (SELECT MAX(height) FROM patients_diagnosis);


--7 Task
Select ROUND (weight / (height * 0.01 * height * 0.01),2) AS IMT, treatment,
(SELECT SUM(weight / (height * 0.01 * height * 0.01))FROM patients_diagnosis) / 
(SELECT COUNT(treatment)
 FROM patients_diagnosis) AS Среднее_IMT 
 FROM patients_diagnosis 
 WHERE (Select ROUND (weight / (height * 0.01 * height * 0.01),2)) > 
 (SELECT SUM(weight / (height * 0.01 * height * 0.01))FROM patients_diagnosis) / 
(SELECT COUNT(treatment)
 FROM patients_diagnosis)


 --8 Task
CREATE VIEW med_card AS SELECT patients.name 
AS patients_name, doctors.name 
AS doctors_name, diagnosis, treatment 
FROM anamnesis JOIN patients 
ON anamnesis.patient_uuid = patients.uuid
JOIN doctors ON anamnesis.doctor_uuid = doctors.uuid;


--9 Task
SELECT name, COUNT(DISTINCT patient_uuid) FROM doctors 
JOIN anamnesis ON anamnesis.doctor_uuid = doctors.uuid
GROUP BY name