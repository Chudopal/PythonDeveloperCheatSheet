import psycopg2

connection = psycopg2.connect(
    dbname="hospital_system",
    user="postgres",
    password='Vl987654321',
    host='localhost'
)

cursor = connection.cursor()