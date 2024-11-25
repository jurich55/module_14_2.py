import sqlite3

connection = sqlite3.connect('not_telegram2.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER)
''')
# Создание индекса по email
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

 # INSERT INTO Users - Создание  таблицы БД "Users" в цикле
# с началом счета от 1 и с шагом 10 для возраста
for i in range(1, 11):
     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?,?,?,?)",
                    (f"user{i}", f"example{i}@gmail.com",  10 * i, 1000))

#   UPDATE  -  Обновление balance у каждой второй записи, начиная с первой
cursor.execute('''
    UPDATE Users    SET balance = 500    WHERE (id % 2) = 1
''')

# DELETE  - Удаление каждой третьей записи, начиная с первой
for id in range(1, 11, 3):
    cursor.execute('''DELETE FROM Users WHERE id = ?''', (id,))

#  SELECT - Выборка всех записей, где возраст не равен 60
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
t_ext = cursor.fetchall()        # применение  fetchall()

# Вывод результатов в консоль в формате:
# Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>
# for t_ext in t_ext:
#     username, email, age, balance = t_ext
#     print(f"Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}")

# Удаление пользователя с id = 6
cursor.execute('''DELETE FROM Users WHERE id = ?''', (6,))

# Подсчет общего количества пользователей
cursor.execute('''SELECT COUNT (*) FROM Users''')
total_users = cursor.fetchone()[0]
# print(total_users)

# Подсчёт суммы всех балансов
cursor.execute('''SELECT SUM(balance) FROM Users''' )
all_balances = cursor.fetchone()[0]
# print(all_balances)

# средний баланс всех пользователей
print(all_balances / total_users)

# Сохранение изменений и закрытие соединения
connection.commit()
connection.close()