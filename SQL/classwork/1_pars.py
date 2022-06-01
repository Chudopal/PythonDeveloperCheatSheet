import sqlite3


connection = sqlite3.connect("example.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE users (id, email, name);
""")

connection.commit()

cursor.execute(
    """INSERT INTO users VALUES (1, "edefe", "alex");"""
)
cursor.execute(
    """INSERT INTO users VALUES (2, "edefe1", "alex");"""
)
cursor.execute(
    """INSERT INTO users VALUES (3, "edefe2", "alex");"""
)
cursor.execute(
    """INSERT INTO users VALUES (5, "edefe3", "alex");"""
)


connection.commit()


cursor.execute("""
    SELECT * FROM users;
""")


data = cursor.fetchall()

print(data)


import sqlite3


connection = sqlite3.connect("1.db")
cursor = connection.cursor()

# cursor.execute("""
#     CREATE TABLE users(id, name, age);
# """)
# connection.commit()

name = input(
    """Введите имя: """
)


cursor.execute(
    """
        DELETE FROM users WHERE name="{}";
    """.format(name)
)

connection.commit()


cursor.execute("""
    SELECT * FROM users;
""")

data = cursor.fetchall()

print(data)




import sqlite3

connection = sqlite3.connect("2.db")
cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE users (name, email, age, job, address);"""
)

connection.commit()

data = input().split(" ")

place_holder = """("{}", "{}", {}, "{}", "{}")"""

cursor.execute(
    """INSERT INTO users VALUES{};
    """.format(place_holder).format(
        *["Bob", "dfcfd", 40, "dfd", "dfd,dfd,dfdf,25"])
)
cursor.execute(
    """INSERT INTO users VALUES{};
    """.format(place_holder).format(
        *["Mike", "dfcfd", 23, "dfd", "dfd,dfd,dfdf,23"])
)
cursor.execute(
    """INSERT INTO users VALUES{};
    """.format(place_holder).format(
        *["Alice", "dfcfd", 25, "dfd", "dfd,dfd,dfdf,40"])
)
connection.commit()

cursor.execute(
    """SELECT * FROM users WHERE age > 23;"""
)

data = cursor.fetchall()

print(data)




import sqlite3

connection = sqlite3.connect('3.db')
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE students(name TEXT PRIMARY KEY, group_name);
""")

connection.commit()


cursor.execute("""
    INSERT INTO students VALUES ('A', 'B');
""")

cursor.execute("""
    INSERT INTO students VALUES ('C', 'D');
""")

cursor.execute("""
    INSERT INTO students VALUES ('E', 'F');
""")

cursor.execute("""
    INSERT INTO students VALUES ('K', 'M');
""")

connection.commit()

name = input('Введите имя: ').upper()

group_name = input('Введите имя группы: ')

cursor.execute("""
    UPDATE students SET group_name = '{}' WHERE name = '{}';
""".format(group_name, name))

connection.commit()


cursor.execute("""
    SELECT * FROM students;
""")

data = cursor.fetchall()

print(data)

