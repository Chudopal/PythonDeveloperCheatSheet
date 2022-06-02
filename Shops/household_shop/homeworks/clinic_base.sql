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
SELECT name, COUNT(anamnesis.patient_uuid) FROM doctors
JOIN anamnesis ON anamnesis.doctor_uuid = doctors.uuid
GROUP BY name
