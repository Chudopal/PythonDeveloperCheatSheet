CREATE TABLE doctors(
    uuid uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    category VARCHAR(256) NOT NULL,
    position VARCHAR(256) NOT NULL
);


CREATE TABLE patients(
    uuid uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    birth_date DATE NOT NULL,
    weight SMALLINT NOT NULL CHECK(weight > 10 AND weight < 300),
    height SMALLINT NOT NULL CHECK(height > 50 AND height < 220),
    sex CHAR(1) NOT NULL CHECK(sex IN ('M', 'F'))
);

CREATE TABLE anamnesis(
    patient_uuid uuid REFERENCES patients(uuid),
    doctor_uuid uuid REFERENCES doctors(uuid),
    diagnosis VARCHAR(256) NOT NULL,
    treatment TEXT NOT NULL
);


INSERT INTO doctors(name, category, position)
VALUES ('Sam', 'Surgery', 'Head'),
    ('Robert', 'Otorhinolaryngology', 'Doctor on duty'),
    ('Vincent', 'Dentistry', 'Head');


INSERT INTO patients(name, birth_date, weight, height, sex)
VALUES ('Bob', '1970-04-19', 60, 180, 'M'),
    ('Alice', '1971-05-20', 50, 160, 'F'),
    ('Barbara', '1980-06-21', 140, 160, 'F'),
    ('Mike', '1990-07-22', 200, 160, 'M');


INSERT INTO anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
VALUES (
    (SELECT uuid FROM patients WHERE name='Bob'),
    (SELECT uuid FROM doctors WHERE name='Sam'),
    'broken leg',
    'set a plaster cast'
),
(
    (SELECT uuid FROM patients WHERE name='Alice'),
    (SELECT uuid FROM doctors WHERE name='Sam'),
    'broken hand',
    'set a plaster cast'
),
(
    (SELECT uuid FROM patients WHERE name='Mike'),
    (SELECT uuid FROM doctors WHERE name='Sam'),
    'concussion',
    'take pills, bandage'
),
(
    (SELECT uuid FROM patients WHERE name='Sam'),
    (SELECT uuid FROM doctors WHERE name='Robert'),
    'does not hear',
    'clear ears'
),
(
    (SELECT uuid FROM patients WHERE name='Mike'),
    (SELECT uuid FROM doctors WHERE name='Robert'),
    'hard to breath',
    'clear nose'
),
(
    (SELECT uuid FROM patients WHERE name='Barbars'),
    (SELECT uuid FROM doctors WHERE name='Robert'),
    'deviated septum',
    'rinsing'
),
(
    (SELECT uuid FROM patients WHERE name='Sam'),
    (SELECT uuid FROM doctors WHERE name='Vincent'),
    'caries',
    'sanitation'
),
(
    (SELECT uuid FROM patients WHERE name='Mike'),
    (SELECT uuid FROM doctors WHERE name='Vincent'),
    'caries',
    'sanitation'
),
(
    (SELECT uuid FROM patients WHERE name='Alice'),
    (SELECT uuid FROM doctors WHERE name='Vincent'),
    'toothache',
    'remove the tooth'
),
(
    (SELECT uuid FROM patients WHERE name='Bob'),
    (SELECT uuid FROM doctors WHERE name='Vincent'),
    'wisdom tooth',
    'remove the tooth'
);


-- 1
SELECT name, category FROM doctors;

-- 2
SELECT COUNT(*) as patient_number FROM patients;

-- 3
SELECT * FROM patients WHERE sex='F';

-- 4
SELECT * FROM patients ORDER BY birth_date;

-- 5

SELECT patients.name, doctors.name
FROM doctors JOIN anamnesis
ON doctors.uuid = anamnesis.doctor_uuid
JOIN patients
ON patients.uuid = anamnesis.patient_uuid;

-- 6
SELECT name, height, diagnosis
FROM patients JOIN anamnesis
ON patients.uuid = anamnesis.patient_uuid
WHERE height = (
    SELECT MAX(height) FROM patients
);

-- view
CREATE VIEW max_height_diagnosis AS
SELECT name, height, diagnosis
FROM patients JOIN anamnesis
ON patients.uuid = anamnesis.patient_uuid
WHERE height = (
    SELECT MAX(height) FROM patients
);

-- 7
SELECT treatment,
    (weight / (height * height * 0.0001)) as patient_bmi,
    (SELECT AVG(weight / (height * height * 0.0001))
     FROM patients) as avg_bmi
FROM patients JOIN anamnesis
ON patients.uuid = anamnesis.patient_uuid
WHERE (weight / (height * height * 0.0001)) > (
    SELECT AVG(weight / (height * height * 0.0001))
    FROM patients
);

-- 8
CREATE VIEW full_info AS
    SELECT patients.name as p_name, doctors.name as d_name, diagnosis, treatment
    FROM patients JOIN anamnesis
    ON patients.uuid = anamnesis.patient_uuid
    JOIN doctors
    ON doctors.uuid = anamnesis.doctor_uuid;