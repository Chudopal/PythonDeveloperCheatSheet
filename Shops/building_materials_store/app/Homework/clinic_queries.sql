create EXTENSION "uuid-ossp";
-- создание трёх таблиц
create table doctors(
	uuid uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
	name CHARACTER VARYING(256),
	category CHARACTER VARYING(256),
	position CHARACTER VARYING(256)
);


create table patients(
	uuid uuid DEFAULT uuid_generate_v4() PRIMARY KEY,
	name CHARACTER VARYING(256),
	birth_date DATE,
	weight SMALLINT CHECK (weight>10 AND weight<300),
	height SMALLINT CHECK (height>50 AND height<220),
	sex CHARACTER VARYING(256)
);

create table anamnesis(
	patient_uuid uuid not null references patients(uuid),
	doctor_uuid uuid not null references doctors(uuid),
	diagnosis character varying(256),
	treatment character varying(256)
);


-- заполняем таблицы данными
insert into doctors(name, category, position)
values
('Bob', 'therapist', 'head physician'),
('Nik', 'surgeon', 'department head'),
('Mike', 'dentist', 'doctor');


insert into patients (name, birth_date, weight, height, sex)
values
('German', '1/8/1999', 70, 170, 'men'),
('Alex', '8/6/1996', 83, 188, 'men'),
('Ann', '17/3/2002', 51, 164, 'woman'),
('Helen', '9/5/1990', 62, 168, 'woman');


insert into anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
select uuid, '3b678e97-9ed1-43c8-aea0-3c1f2bdbbf1b', 'stroke', 'pills and drip'
from patients where name='German';

insert into anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
select uuid, '3b678e97-9ed1-43c8-aea0-3c1f2bdbbf1b', 'small stroke', 'pills'
from patients where name='Alex'

insert into anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
select uuid, '3b678e97-9ed1-43c8-aea0-3c1f2bdbbf1b', 'cirrhosis of the liver', 'surgery and pills'
from patients where name='Helen'

insert into anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
select uuid, '7ba2b756-dd7c-45f1-b43c-05b3b3cb8e9c', 'swelling in the leg', 'surgery and pills'
from patients where name='Ann'

insert into anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
select uuid, '7ba2b756-dd7c-45f1-b43c-05b3b3cb8e9c', 'swelling in the leg', 'surgery and pills'
from patients where name='German'

insert into anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
select uuid, '9cf21af7-0570-4c74-87d8-170e8178102c', 'hole in the tooth', 'fill a tooth'
from patients where name='German'

insert into anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
select uuid, '9cf21af7-0570-4c74-87d8-170e8178102c', 'hole in the tooth', 'fill a tooth'
from patients where name='Alex'

insert into anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
select uuid, '9cf21af7-0570-4c74-87d8-170e8178102c', 'periodontal disease', 'remove the tooth'
from patients where name='Helen'

insert into anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
select uuid, '7ba2b756-dd7c-45f1-b43c-05b3b3cb8e9c', 'retrieval of an object', 'operation and drip'
from patients where name='Ann'

insert into anamnesis(patient_uuid, doctor_uuid, diagnosis, treatment)
select uuid, '7ba2b756-dd7c-45f1-b43c-05b3b3cb8e9c', 'retrieval of an object', 'operation'
from patients where name='Alex'

-- 1.name, category всех докторов
select name, category from doctors;

-- 2.количество всех пациентов
select count(*) as patient from patients;

-- 3.пациентов женского пола
select * from patients where sex='woman'

-- 4.отсортировать всех пользователей по birth_date
select name, birth_date from patients order by birth_date;

-- 5.name пациента и name лечащего доктора
select doctors.name, patients.name
from doctors
join anamnesis on doctor_uuid=doctors.uuid
join patients on patients.uuid=patient_uuid;

-- 6.name, диагноз пациентов с максимальным ростом (доп: сделать VIEW)
create view patients_height as
select name, diagnosis, height
from anamnesis
join patients
on patients.uuid=anamnesis.patient_uuid;

select name, diagnosis, height
from patients_height
where height = (select max(height) from patients_height);

-- 7.вывести treatment, имт пользователя, среднее имт по больнице для всех пользователей,
-- у которых имт выше среднего в больнице
create view BMI_view as
select weight/(height *0.01 * height * 0.01) as BMI,
anamnesis.treatment, patients.name
from patients
join anamnesis on anamnesis.patient_uuid=patients.uuid;

select BMI, treatment, name
from BMI_view
where BMI> (select avg(BMI) from BMI_view)

-- 8.сделайте представление, которое возвращает name пациента, name доктора, diagnosis, treatment
select patients.name, doctors.name, anamnesis.diagnosis, anamnesis.treatment
from anamnesis
join patients
on patients.uuid=anamnesis.patient_uuid
join doctors
on doctors.uuid=anamnesis.doctor_uuid


-- 9.количество пациентов, name для каждого доктора
select count(anamnesis.patient_uuid) from anamnesis
join doctors on anamnesis.doctor_uuid=doctors.uuid
where doctors.name = 'Bob';

select count(anamnesis.patient_uuid) from anamnesis
join doctors on anamnesis.doctor_uuid=doctors.uuid
where doctors.name = 'Nik';


select count(anamnesis.patient_uuid) from anamnesis
join doctors on anamnesis.doctor_uuid=doctors.uuid
where doctors.name = 'Mike';

