-- Создание таблиц

CREATE EXTENSION "uuid-ossp";

CREATE TABLE doctors(
  uuid uuid PRIMARY KEY DEFAULT uuid_generate_v4 (),
  name CHARACTER VARYING(255) NOT NULL,
  category CHARACTER VARYING(255) NOT NULL,
  position CHARACTER VARYING(255) NOT NULL
);

CREATE TABLE patients(
	uuid UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
	name CHARACTER VARYING(255),
	birth_date timestamp,
	weight INTEGER CHECK (weight > 10 AND weight < 300),
	height NUMERIC(3, 2) CHECK (height > 0.5 AND height < 2.20),
	sex CHARACTER CHECK (sex LIKE 'F' OR sex LIKE 'M')
);

CREATE TABLE anamnesis(
	patient_uuid UUID NOT NULL REFERENCES patients(uuid) ON DELETE RESTRICT,
	doctor_uuid UUID NOT NULL REFERENCES doctors(uuid) ON DELETE RESTRICT,
	diagnosis TEXT,
	treatment TEXT,
	PRIMARY KEY (patient_uuid, doctor_uuid)
);

-- Заполнение данными

INSERT INTO doctors (name, category, position) VALUES
('Gregory', 'General Pathology', 'Clinical Director'),
('Bob', 'Cardiology', 'Head Physician'),
('John', 'Surgery', 'Head of Surgery Department');

INSERT INTO patients (name, birth_date, weight, height, sex) VALUES
('Liam', '1952-06-07', 85, 1.93, 'M'),
('Chuck', '1940-03-10', 82, 1.78, 'M'),
('Carrie', '1956-12-27', 65, 1.55, 'F'),
('Margot', '1990-07-02', 60, 1.68, 'F');

INSERT INTO anamnesis (patient_uuid, doctor_uuid, diagnosis, treatment)
VALUES
(
	(SELECT uuid FROM patients WHERE name='Liam'),
	(SELECT uuid FROM doctors WHERE name='John'),
	'Open chest wound',
	'sew up and bandage'
),
(
	(SELECT uuid FROM patients WHERE name='Carrie'),
	(SELECT uuid FROM doctors WHERE name='John'),
	'Broken leg',
	'Bandage and rest'
),
(
	(SELECT uuid FROM patients WHERE name='Chuck'),
	(SELECT uuid FROM doctors WHERE name='John'),
	'Head injury',
	'Cold and rest'
),
(
	(SELECT uuid FROM patients WHERE name='Margot'),
	(SELECT uuid FROM doctors WHERE name='John'),
	'Broken arm',
	'Fix and bandage'
),
(
	(SELECT uuid FROM patients WHERE name='Carrie'),
	(SELECT uuid FROM doctors WHERE name='Gregory'),
	'Сough',
	'Drink hot tea and eat pillows'
),
(
	(SELECT uuid FROM patients WHERE name='Margot'),
	(SELECT uuid FROM doctors WHERE name='Gregory'),
	'Сough',
	'Drink hot tea and eat pillows'
),
(
	(SELECT uuid FROM patients WHERE name='Liam'),
	(SELECT uuid FROM doctors WHERE name='Gregory'),
	'Runny nose',
	'Drink hot tea, use nose spray'
),
(
	(SELECT uuid FROM patients WHERE name='Chuck'),
	(SELECT uuid FROM doctors WHERE name='Gregory'),
	'Runny nose',
	'Drink hot tea, use nose spray'
),
(
	(SELECT uuid FROM patients WHERE name='Carrie'),
	(SELECT uuid FROM doctors WHERE name='Bob'),
	'Arrhythmia',
	'Eat pills'
),
(
	(SELECT uuid FROM patients WHERE name='Liam'),
	(SELECT uuid FROM doctors WHERE name='Bob'),
	'Coronary Artery Disease',
	'Eat pills and drink water'
);

-- Запросы

-- 1. name, category всех докторов
SELECT name, category FROM doctors;

-- 2. количество всех пациентов
SELECT COUNT(*) FROM patients;

-- 3. пациентов женского пола
SELECT * FROM patients WHERE sex='F';

-- 4. отсортировать всех пользователей по birth_date
SELECT * FROM patients ORDER BY birth_date;

-- 5. name пациента и name лечащего доктора
SELECT patients.name, doctors.name 
FROM patients 
JOIN anamnesis ON patients.uuid = anamnesis.patient_uuid
JOIN doctors ON anamnesis.doctor_uuid = doctors.uuid

-- 6 name, диагноз пациентов с максимальным ростом (доп: сделать VIEW)
CREATE VIEW higest_patients_diagnosis AS
SELECT name, anamnesis.diagnosis
FROM patients JOIN anamnesis ON patients.uuid = anamnesis.patient_uuid
WHERE patients.height=(
	SELECT MAX(height) FROM patients
);

-- 7 вывести treatment, имт пользователя, 
-- среднее имт по больнице для всех пользователей, 
-- у которых имт выше среднего в больнице

WITH patients_bmi AS (
	SELECT patients.name as name, ROUND((weight / (height * height)), 2) as bmi, anamnesis.treatment as treatment
	FROM patients JOIN anamnesis ON patients.uuid = anamnesis.patient_uuid
)

SELECT name, bmi, treatment
FROM patients_bmi
WHERE bmi > (SELECT AVG(bmi) FROM patients_bmi)

-- 8 сделайте представление, которое возвращает name пациента, name доктора, diagnosis, treatment
CREATE VIEW patient_doctor AS (
	SELECT patients.name AS patient, doctors.name AS doctor, anamnesis.diagnosis, anamnesis.treatment
	FROM patients JOIN anamnesis ON patients.uuid = anamnesis.patient_uuid
	JOIN doctors ON anamnesis.doctor_uuid = doctors.uuid
);

-- 9 количество пациентов, name для каждого доктора
SELECT doctors.name , COUNT(anamnesis.doctor_uuid)
FROM doctors JOIN anamnesis ON doctors.uuid = anamnesis.doctor_uuid
GROUP BY doctors.name
