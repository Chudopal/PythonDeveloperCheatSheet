CREATE EXTENSION "uuid-ossp";
-- создание трёх таблиц
CREATE TABLE doctors(
	uuid uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
	name CHARACTER VARYING(256),
	category CHARACTER VARYING(256),
	positiON CHARACTER VARYING(256)
);


CREATE TABLE patients(
	uuid uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
	name CHARACTER VARYING(256),
	birth_date DATE,
	weight SMALLINT CHECK (weight>10 AND weight<300),
	height SMALLINT CHECK (height>50 AND height<220),
	sex CHARACTER VARYING(256) CHECK (sex='F' OR sex='M')
);

CREATE TABLE anamnesis(
	patient_uuid uuid not null references patients(uuid),
	doctor_uuid uuid not null references doctors(uuid),
	diagnosis character varying(256),
	treatment character varying(256)
);


-- заполняем таблицы данными
INSERT INTO doctors(name, category, positiON)
VALUES
('Bob', 'therapist', 'head physician'),
('Nik', 'surgeON', 'department head'),
('Mike', 'dentist', 'doctor');


INSERT INTO patients (name, birth_date, weight, height, sex)
VALUES
('German', '1/8/1999', 70, 170, 'M'),
('Alex', '8/6/1996', 83, 188, 'M'),
('Ann', '17/3/2002', 51, 164, 'F'),
('Helen', '9/5/1990', 62, 168, 'F');


INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, '3b678e97-9ed1-43c8-aea0-3c1f2bdbbf1b', 'stroke', 'pills and drip'
FROM patients WHERE name='German';

INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, '3b678e97-9ed1-43c8-aea0-3c1f2bdbbf1b', 'small stroke', 'pills'
FROM patients WHERE name='Alex'

INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, '3b678e97-9ed1-43c8-aea0-3c1f2bdbbf1b', 'cirrhosis of the liver', 'surgery and pills'
FROM patients WHERE name='Helen'

INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, '7ba2b756-dd7c-45f1-b43c-05b3b3cb8e9c', 'swelling in the leg', 'surgery and pills'
FROM patients WHERE name='Ann'

INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, '7ba2b756-dd7c-45f1-b43c-05b3b3cb8e9c', 'swelling in the leg', 'surgery and pills'
FROM patients WHERE name='German'

INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, '9cf21af7-0570-4c74-87d8-170e8178102c', 'hole in the tooth', 'fill a tooth'
FROM patients WHERE name='German'

INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, '9cf21af7-0570-4c74-87d8-170e8178102c', 'hole in the tooth', 'fill a tooth'
FROM patients WHERE name='Alex'

INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, '9cf21af7-0570-4c74-87d8-170e8178102c', 'periodONtal diseASe', 'remove the tooth'
FROM patients WHERE name='Helen'

INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, '7ba2b756-dd7c-45f1-b43c-05b3b3cb8e9c', 'retrieval of an object', 'operatiON and drip'
FROM patients WHERE name='Ann'

INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
SELECT uuid, '7ba2b756-dd7c-45f1-b43c-05b3b3cb8e9c', 'retrieval of an object', 'operatiON'
FROM patients WHERE name='Alex'

-- 1.name, category всех докторов
SELECT name, category FROM doctors;

-- 2.количество всех пациентов
SELECT count(*) AS patient FROM patients;

-- 3.пациентов женского пола
SELECT * FROM patients WHERE sex='F'

-- 4.отсортировать всех пользователей по birth_date
SELECT name, birth_date FROM patients ORDER BY birth_date;

-- 5.name пациента и name лечащего доктора
SELECT doctors.name, patients.name
FROM doctors
JOIN anamnesis ON doctor_uuid=doctors.uuid
JOIN patients ON patients.uuid=patient_uuid;

-- 6.name, диагноз пациентов с максимальным ростом (доп: сделать VIEW)
CREATE VIEW patients_height AS
SELECT name, diagnosis, height
FROM anamnesis
JOIN patients
ON patients.uuid=anamnesis.patient_uuid;

SELECT name, diagnosis, height
FROM patients_height
WHERE height = (SELECT max(height) FROM patients_height);

-- 7.вывести treatment, имт пользователя, среднее имт по больнице для всех пользователей,
-- у которых имт выше среднего в больнице
CREATE VIEW BMI_VIEW AS
SELECT weight/(height *0.01 * height * 0.01) AS BMI,
anamnesis.treatment, patients.name
FROM patients
JOIN anamnesis ON anamnesis.patient_uuid=patients.uuid;

SELECT BMI, treatment, name
FROM BMI_VIEW
WHERE BMI> (SELECT avg(BMI) FROM BMI_VIEW)

-- 8.сделайте представление, которое возвращает name пациента, name доктора, diagnosis, treatment
CREATE VIEW registr_VIEW AS
SELECT patients.name AS patient, doctors.name AS doctor, anamnesis.diagnosis, anamnesis.treatment
FROM anamnesis
JOIN patients
ON patients.uuid=anamnesis.patient_uuid
JOIN doctors
ON doctors.uuid=anamnesis.doctor_uuid


-- 9.количество пациентов, name для каждого доктора
SELECT count(DISTINCT anamnesis.patient_uuid), doctors.name
FROM doctors
JOIN anamnesis ON anamnesis.doctor_uuid=doctors.uuid
GROUP BY doctors.name;

