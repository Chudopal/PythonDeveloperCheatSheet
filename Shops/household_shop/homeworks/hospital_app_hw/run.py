import psycopg2
from hospital import Hospital
from config import connection, cursor


hospital = Hospital()
print(*hospital.get_all_doctors(), sep='\n')