-- создаем таблицу "Доктора"
CREATE TABLE doctors (
	uuid uuid UNIQUE DEFAULT uuid_generate_v4() PRIMARY KEY,
	name CHARACTER VARYING(40),
	category CHARACTER VARYING(10),
	position CHARACTER VARYING(20)
);


-- создаем таблицу "Пациенты"
CREATE TABLE patients (
	uuid uuid UNIQUE DEFAULT uuid_generate_v4() PRIMARY KEY,
	name CHARACTER VARYING(40),
	birth_date datestyle,
	weight,kg INTEGER CHECK (weight > 10 AND weight < 300)
	height,cm INTEGER CHECK (height > 50 AND height < 220) 
	sex CHARACTER VARYING(1)
);


-- создаем таблицу "Анамнез"
CREATE TABLE anamnesis (
	patient_uuid uuid NOT NULL REFERENCES patients(uuid),
	doctor_uuid uuid NOT NULL REFERENCES doctors(uuid),
	diagnosis CHARACTER VARYING(30),
	treatment CHARACTER VARYING(50)
);


-- заполнение таблицы "Доктора"
INSERT INTO doctors (name, category, position) VALUES
('Павлов В.М.', 'первая', 'травматолог'),
('Иванова С.М.','первая', 'педиатр'),
('Петров Г.C.', 'вторая', 'хирург');


-- заполнение таблицы "Пациенты"
INSERT INTO patients(name, birth_date, weight_kg, height_cm, sex) VALUES
('Иванов И.И.', '1975-08-24', 79, 180, 'м'),
('Семенов Г.И.', '1980-09-24', 89, 182, 'м'),
('Петрова Г.И.', '1990-07-09', 55, 164, 'ж'),
('Сидорова Г.И.', '1990-08-24', 56, 168, 'ж');


-- заполнение таблицы "Анамнез"
INSERT INTO anamnesis (patient_uuid, doctor_uuid, diagnosis, treatment)
VALUES
(
  (SELECT uuid FROM patients WHERE name='Иванов И.И.'),
  (SELECT uuid FROM doctors WHERE name='Иванова С.М.'),
  'близорукость',
  'препарат'
);

INSERT INTO anamnesis (patient_uuid, doctor_uuid, diagnosis, treatment)
VALUES
(
  (SELECT uuid FROM patients WHERE name='Семенов Г.И.'),
  (SELECT uuid FROM doctors WHERE name='Иванова С.М.'),
  'близорукость',
  'препарат'
);

INSERT INTO anamnesis (patient_uuid, doctor_uuid, diagnosis, treatment)
VALUES
(
  (SELECT uuid FROM patients WHERE name='Петрова Г.И.'),
  (SELECT uuid FROM doctors WHERE name='Иванова С.М.'),
  'близорукость',
  'препарат'
);

INSERT INTO anamnesis (patient_uuid, doctor_uuid, diagnosis, treatment)
VALUES
(
  (SELECT uuid FROM patients WHERE name='Сидорова Г.И.'),
  (SELECT uuid FROM doctors WHERE name='Иванова С.М.'),
  'близорукость',
  'препарат'
);

INSERT INTO anamnesis (patient_uuid, doctor_uuid, diagnosis, treatment)
VALUES
(
  (SELECT uuid FROM patients WHERE name='Иванов И.И.'),
  (SELECT uuid FROM doctors WHERE name='Павлов В.М.'),
  'перелом руки',
  'фиксация с помощью гипса'
);

INSERT INTO anamnesis (patient_uuid, doctor_uuid, diagnosis, treatment)
VALUES
(
  (SELECT uuid FROM patients WHERE name='Семенов Г.И.'),
  (SELECT uuid FROM doctors WHERE name='Павлов В.М.'),
  'перелом руки',
  'фиксация с помощью гипса'
);

INSERT INTO anamnesis (patient_uuid, doctor_uuid, diagnosis, treatment)
VALUES
(
  (SELECT uuid FROM patients WHERE name='Петрова Г.И.'),
  (SELECT uuid FROM doctors WHERE name='Павлов В.М.'),
  'перелом руки',
  'фиксация с помощью гипса'
);

INSERT INTO anamnesis (patient_uuid, doctor_uuid, diagnosis, treatment)
VALUES
(
  (SELECT uuid FROM patients WHERE name='Сидорова Г.И.'),
  (SELECT uuid FROM doctors WHERE name='Павлов В.М.'),
  'перелом руки',
  'фиксация с помощью гипса'
);

INSERT INTO anamnesis (patient_uuid, doctor_uuid, diagnosis, treatment)
VALUES
(
  (SELECT uuid FROM patients WHERE name='Иванов И.И.'),
  (SELECT uuid FROM doctors WHERE name='Петров Г.С.'),
  'аппендицит',
  'оперативное вмешательство'
);

INSERT INTO anamnesis (patient_uuid, doctor_uuid, diagnosis, treatment)
VALUES
(
  (SELECT uuid FROM patients WHERE name='Семенов Г.И.'),
  (SELECT uuid FROM doctors WHERE name='Петров Г.С.'),
  'аппендицит',
  'оперативное вмешательство'
);



-- Запросы
-- name, category всех докторов
SELECT name, category FROM doctors


-- количество всех пациентов
SELECT * FROM patients


-- пациентов женского пола
SELECT * FROM patients
WHERE sex='ж'


-- отсортировать всех пользователей по birth_date
SELECT uuid, name, birth_date, weight_kg, height_cm, sex
FROM patients ORDER BY birth_date


-- name пациента и name лечащего доктора
SELECT
	patients.name,
	doctors.name
FROM
	patients
INNER JOIN anamnesis 
    ON patients.uuid = anamnesis.patient_uuid
INNER JOIN doctors 
    ON anamnesis.doctor_uuid = doctors.uuid
ORDER BY patients.name;


-- name, диагноз пациентов с максимальным ростом (доп: сделать VIEW)
CREATE VIEW diagnosis_height AS
SELECT
	patients.name,
	anamnesis.diagnosis,
	patients.height_cm
FROM
	patients
INNER JOIN anamnesis 
    ON patients.uuid = anamnesis.patient_uuid

SELECT name, diagnosis, height_cm FROM diagnosis_height
WHERE height_cm=(SELECT MAX(height_cm) FROM diagnosis_height)


-- вывести treatment, имт пользователя, среднее имт по больнице для всех пользователей, у которых имт выше среднего в больнице
CREATE VIEW BMI_COUNT AS
SELECT weight_kg / (height_cm * 0.01 * height_cm * 0.01) AS BMI,
	patients.name,
	anamnesis.treatment
FROM
	patients
INNER JOIN anamnesis 
    ON patients.uuid = anamnesis.patient_uuid
ORDER BY patients.name;

SELECT name, BMI, treatment
FROM BMI_COUNT
WHERE BMI > (SELECT AVG(BMI) FROM BMI_COUNT)


-- сделайте представление, которое возвращает name пациента, name доктора, diagnosis, treatment
SELECT
	patients.name,
	doctors.name,
	anamnesis.diagnosis,
	anamnesis.treatment
FROM
	patients
INNER JOIN anamnesis 
    ON patients.uuid = anamnesis.patient_uuid
INNER JOIN doctors 
    ON anamnesis.doctor_uuid = doctors.uuid
ORDER BY patients.name;

-- количество пациентов, name для каждого доктора
SELECT doctors.name, COUNT(DISTINCT anamnesis.patient_uuid)
FROM
	doctors
INNER JOIN anamnesis 
    ON doctors.uuid = anamnesis.doctor_uuid
GROUP BY doctors.name;