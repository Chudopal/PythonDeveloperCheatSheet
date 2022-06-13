CREATE TABLE doctors(
	uuid uuid UNIQUE DEFAULT uuid_generate_v4(),	
	name CHARACTER VARYING (256) NOT NULL,
	category INTEGER CHECK NOT NULL,
	position CHARACTER VARYING (55) NOT NULL
);


CREATE TABLE patients(
	uuid uuid UNIQUE DEFAULT uuid_generate_v4(),
	name CHARACTER VARYING (256) NOT NULL,
	birth_date DATE NOT NULL,
	weight INTEGER NOT NULL CHECK(height >= 10 AND height <= 300),
	height INTEGER NOT NULL CHECK(height >= 50 AND height <= 220),
	sex CHAR(6) NOT NULL CHECK(sex IN ('male', 'female'))
);


CREATE TABLE anamnesis(
	patient_uuid uuid NOT NULL REFERENCES patients(uuid),
	doctor_uuid uuid NOT NULL REFERENCES doctors(uuid),
	diagnosis CHARACTER VARYING (256) NOT NULL,
	treatment CHARACTER VARYING (256) NOT NULL
);


INSERT INTO doctors(name, category, position) VALUES
('Василий Пупкин', 2, 'Врач общей практити'),
('Пупок Пупков', 1, 'Заведующий отделением терапии'),
('Андрей Быков', 1, 'Главный врач');


INSERT INTO patients(name, birth_date, weight, height, sex) VALUES
('Bob', '10.06.1993', 75, 180, 'male'),
('Alice', '10.10.2000', 49, 160, 'female'),
('Alex', '10.09.1990', 98, 190, 'male'),
('Olga', '13.11.1999', 55, 178, 'female');


INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment) VALUES
(
	(SELECT uuid FROM patients WHERE name='Bob'),
	(SELECT uuid FROM doctors WHERE name='Пупок Пупков'),
	'Давление',
	'Приём препаратов'
),
(
	(SELECT uuid FROM patients WHERE name='Alex'),
	(SELECT uuid FROM doctors WHERE name='Андрей Быков'),
	'Давление',
	'Приём препаратов'

),
(
	(SELECT uuid FROM patients WHERE name='Alice'),
	(SELECT uuid FROM doctors WHERE name='Василий Пупкин'),
	'Простуда',
	'Чай з варэннем'
),
(
	(SELECT uuid FROM patients WHERE name='Olga'),
	(SELECT uuid FROM doctors WHERE name='Василий Пупкин'),
	'Боли в спине',
	'Посещение массажа'

),
(
	(SELECT uuid FROM patients WHERE name='Bob'),
	(SELECT uuid FROM doctors WHERE name='Андрей Быков'),
	'Головные боли',
	'Постельный режим'
),
(
	(SELECT uuid FROM patients WHERE name='Alex'),
	(SELECT uuid FROM doctors WHERE name='Пупок Пупков'),
	'Перелом',
	'Гипс'

),
(
	(SELECT uuid FROM patients WHERE name='Alice'),
	(SELECT uuid FROM doctors WHERE name='Василий Пупкин'),
	'Боли в области живота',
	'Диета'
),
(
	(SELECT uuid FROM patients WHERE name='Olga'),
	(SELECT uuid FROM doctors WHERE name='Андрей Быков'),
	'Порез',
	'Повязка'
),
(
	(SELECT uuid FROM patients WHERE name='Bob'),
	(SELECT uuid FROM doctors WHERE name='Василий Пупкин'),
	'Боли в области живота',
	'Диета'
),
(
	(SELECT uuid FROM patients WHERE name='Alex'),
	(SELECT uuid FROM doctors WHERE name='Андрей Быков'),
	'Порез',
	'Повязка'
);


1
SELECT name, category FROM doctors;


2
SELECT COUNT(*) as uuid FROM patients;


3
SELECT COUNT(*) as uuid FROM patients WHERE sex='female';


4
SELECT * FROM patients ORDER BY birth_date;


5
SELECT patients.name, doctors.name FROM patients
JOIN anamnesis ON patients.uuid = anamnesis.patient_uuid
JOIN doctors ON doctors.uuid = anamnesis.doctor_uuid;


6
SELECT name, diagnosis, patients.height FROM anamnesis
JOIN patients ON patients.uuid = anamnesis.patient_uuid
WHERE patients.height = (
	SELECT MAX(patients.height) FROM patients
)

CREATE VIEW max_height AS
SELECT name, diagnosis, patients.height FROM anamnesis
JOIN patients ON patients.uuid = anamnesis.patient_uuid
WHERE patients.height = (
	SELECT MAX(patients.height) FROM patients
)


7
SELECT name, (weight / ((height * 0.01) * (height * 0.01))), (SELECT AVG((weight / ((height * 0.01) * (height * 0.01)))) FROM patients)
FROM patients	
WHERE (weight / ((height * 0.01) * (height * 0.01))) >= (
	SELECT AVG((weight / ((height * 0.01) * (height * 0.01)))) FROM patients
)


8
CREATE VIEW clinic_card AS	
	SELECT patients.name, doctors.name, anamnesis.diagnosis, anamnesis.treatment FROM doctors
	JOIN anamnesis ON doctors.uuid = anamnesis.doctor_uuid
	JOIN patients ON anamnesis.patient_uuid = patients.uuid


9
SELECT name, COUNT(DISTINCT anamnesis.patient_uuid) FROM doctors
JOIN anamnesis ON anamnesis.doctor_uuid = doctors.uuid
GROUP BY name
