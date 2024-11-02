import sqlite3

connection = sqlite3.connect('L:\\Python\\UU-kurs\\Module17\\taskmanager.db')
cursor = connection.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS Products('
#                'id INTEGER PRIMARY KEY,'
#                'title TEXT NOT NULL,'
#                'description TEXT,'
#                'price INTEGER NOT NULL,'
#                'photo TEXT)')
#
#
# cursor.execute('CREATE INDEX IF NOT EXISTS ind_name ON Buy (first_name)')
# cursor.execute('CREATE INDEX IF NOT EXISTS ind_prod ON Buy (product)')
#
# products = [
#     ['Лот #001', 'Очень бюджетный вариант', 199, 'image/006.JPG'],
#     ['Лот #002', 'Разновидность бюджетного варианта', 299, 'image/003.JPG'],
#     ['Лот #003', 'Инструкция для самостоятельной реализации на базе экранов Nextion', 2_999, 'image/009.JPG'],
#     ['Лот #004', 'Высокоинтеллектуальное решение на базе ИИ', 29_999, 'image/007.JPG'],
#     ['Лот #005', 'Высокоинтеллектуальное решение на базе ИИ с дактилоскопическим анализом состояния здоровья',
#      69_999, 'image/008.JPG'],
#     ['Лот #006', 'Самое эффективное решение по невероятно низкой цене', 9, 'image/010.JPG']
# ]

# for product in products:
#     cursor.execute('INSERT INTO Products (title, description, price, photo) VALUES (?, ?, ?, ?)',
#                    (product[0], product[1], product[2], product[3]))

# cursor.execute("INSERT INTO Users_par (first_name, gender, age, growth, weight) VALUES ('John', 'male', 25, 180, 70)")

cursor.execute('SELECT * FROM Users')
result = cursor.fetchall()
print(result)

connection.commit()
connection.close()
