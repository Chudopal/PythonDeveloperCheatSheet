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
