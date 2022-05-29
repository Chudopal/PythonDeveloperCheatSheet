
-- подгружаем uuid
CREATE EXTENSION "uuid-ossp";

-- создаем таблицу doctors(uuid, name, category, position)
CREATE TABLE doctors(
    uuid uuid UNIQUE DEFAULT uuid_generate_v4(),
    name CHARACTER VARYING(256), category VARCHAR(256), position INT);

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
