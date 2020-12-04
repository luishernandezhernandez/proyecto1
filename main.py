# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Importar dependencias
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL

# Creando la aplicación
app = Flask(__name__)
# Configuración de la conexión con la base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Root.1234'
app.config['MYSQL_DB'] = 'iric'
# Creación de objeto para la conexión a la base de datos
mysql = MySQL(app)
app.secret_key = 'mysecret'


@app.route('/students/get', methods=['GET'])
def get_students():
    # Arreglo
    payload = []
    # Diccionario
    student = {}
    cursor = mysql.connection.cursor()
    cursor.execute("select * from student")
    data = cursor.fetchall()
    # Ciclo
    for row in data:
        student = {
            'id': row[0],
            'nombre': row[1],
            'a_paterno': row[2],
            'a_materno': row[3],
            'e_mail': row[4]
        }
        payload.append(student)
        student = {}
    return jsonify(payload)


@app.route('/students/get/<int:_id>', methods=['GET'])
def get_student_by_id(_id):
    payload = []
    student = {}
    cursor = mysql.connection.cursor()
    cursor.execute('select * from student where id = %s' % _id)
    data = cursor.fetchall()
    # Ciclo
    for row in data:
        student = {
            'id': row[0],
            'nombre': row[1],
            'a_paterno': row[2],
            'a_materno': row[3],
            'e_mail': row[4]
        }
        payload.append(student)
        student = {}
    return jsonify(payload)


@app.route('/students/add', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    a_paterno = request.form['a_paterno']
    a_materno = request.form['a_materno']
    e_mail = request.form['e_mail']
    cursor = mysql.connection.cursor()
    # Codigo para utililizar procedimientos almacenados
    cursor.execute(
        'insert into student(nombre, a_paterno, a_materno, e_mail) values(%s, %s, %s, %s)',
        (nombre, a_paterno, a_materno, e_mail)
    )
    # Confirma la operacion insert
    mysql.connection.commit()
    return jsonify(
        {'message': 'Registro agregado'}
    )


@app.route('/students/edit/<int:_id>', methods=['PUT'])
def editar(_id):
    nombre = request.form['nombre']
    a_paterno = request.form['a_paterno']
    a_materno = request.form['a_materno']
    e_mail = request.form['e_mail']
    cursor = mysql.connection.cursor()
    # Formar la instrucción SQL junto con las variables
    cursor.execute(
        'update student set nombre = %s, a_paterno = %s, a_materno = %s, e_mail = %s where id = %s',
        (nombre, a_paterno, a_materno, e_mail, _id)
    )
    # Ejecutar en firme la instrucción update
    mysql.connection.commit()
    return jsonify({'mensaje': 'Registro editado correctamente'})


@app.route('/students/remove/<int:_id>', methods=['DELETE'])
def remove(_id):
    cursor = mysql.connection.cursor()
    cursor.execute('delete from student where id = %s' % _id)
    mysql.connection.commit()
    return jsonify({'mensaje': 'Registro eliminado correctamente'})


# Ejecución de app
if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
