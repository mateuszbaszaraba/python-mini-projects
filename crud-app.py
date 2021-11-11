import mysql.connector
from flask import Flask
from flask import jsonify
from flask import request
from flask import Response
import jsonpickle


def get_connection_db():
    connection = mysql.connector.connect(
        user='root',
        password='password',
        host='127.0.0.1',
        database='pythondatabase',
        auth_plugin='mysql_native_password')
    return connection


#################################################################################

class User:
    def __init__(self, user_id: int, username: str, city: str):
        self.user_id = user_id
        self.username = username
        self.city = city

#################################################################################


app = Flask(__name__)


@app.route('/users', methods=['GET'])
def get_users():
    users = []
    connection = get_connection_db()
    cursor = connection.cursor(dictionary=True)
    query = 'SELECT id, username, city FROM users'
    cursor.execute(query)

    for row in cursor:
        users.append(User(row['id'], row['username'], row['city']))

    connection.close()

    response = Response(jsonpickle.encode(users, unpicklable=False), mimetype='application/json')
    response.headers['new_header'] = 'new header'

    return response


@app.route('/users', methods=['POST'])
def add_user():
    request_data = request.get_json()

    try:
        connection = get_connection_db()
        cursor = connection.cursor()

        query = 'INSERT INTO users(username, city) VALUES(%(username)s, %(city)s)'
        cursor.execute(query, request_data)
        connection.commit()
    except mysql.connector.Error as err:
        return jsonify(details=err.msg), 400
    finally:
        connection.close()

    return request_data, 201


@app.route('/users/<user_id>', methods=['PUT'])
def edit_user(user_id):
    request_data = request.get_json()
    request_data['user_id'] = user_id

    try:
        connection = get_connection_db()
        cursor = connection.cursor()

        query = 'UPDATE users SET username=%(username)s, city=%(city)s WHERE id=%(user_id)s'
        cursor.execute(query, request_data)
        connection.commit()
    except mysql.connector.Error as err:
        return jsonify(details=err.msg), 400
    finally:
        connection.close()

    return request_data


@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    request_data = {}
    request_data['user_id'] = user_id

    try:
        connection = get_connection_db()
        cursor = connection.cursor()

        query = 'DELETE FROM users WHERE id=%(user_id)s'
        cursor.execute(query, request_data)
        connection.commit()
    except mysql.connector.Error as err:
        return jsonify(details=err.msg), 400
    finally:
        connection.close()

    return jsonify()

app.run()
