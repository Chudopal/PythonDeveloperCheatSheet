from hospital import DBStorage, Hospital

storage = DBStorage(dbname="tms_hospital_homework", host="localhost", user="postgres", password="toor")
app = Hospital(storage)

print(app.get_patient("168a641a-5d16-48c7-bc8d-55a05eb9fc19"))
