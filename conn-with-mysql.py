import mysql.connector

connection = mysql.connector.connect(user='root', password='root', host='127.0.0.1', port='8889', database='pybase',
                                     auth_plugin='mysql_native_password')

cursor = connection.cursor()


insertQuery = "INSERT INTO users(username, city) VALUES(%(username)s, %(city)s)"
insertData = {
    'username': 'Testuser',
    'city': 'Katowice'
}
cursor.execute(insertQuery, insertData)
connection.commit()

query = 'SELECT id, username, city FROM users'
cursor.execute(query)

for (id, username, city) in cursor:
    print(f'[{id}] {username} from {city}')

connection.close()
