from flask import Flask, request

app = Flask(__name__) # main.py

users = [
    {
        "id": 1,
        "name": "Andres",
        "last_name": "Taboada"
    },
    {
        "id": 2,
        "name": "Roberto",
        "last_name": "Quiroga"
    }
]

@app.route('/', methods=['GET'])
def index():
    return {
        'message': 'Hello world !'
    }

@app.route('/users', methods=['GET'])
def usersList():
    return users, 200

# Path Params
# string (por defecto)
# int
# float
# path - es un string, que acepta el signo slash /folder/
# uuid - Identificador unico universal
@app.route('/users/<int:id>', methods=['GET'])
def userGetById(id):
    for user in users:
        if user['id'] == id:
            return user, 200
    
    return {
        'message': 'El usuario ingresado no existe'
    }, 404

@app.route('/users', methods=['POST'])
def userCreate():
    body = request.get_json()
    users.append(body)
    return {
        'message': 'Usuario creado con exito'
    }, 201

@app.route('/users/<int:id>', methods=['PUT'])
def userUpdate(id):
    body = request.get_json()
    
    for user in users:
        if user['id'] == id:
            user['name'] = body['name']
            user['last_name'] = body['last_name']
            return user, 200
    
    return {
        'message': 'El usuario ingresado no existe'
    }, 404

@app.route('/users/<int:id>', methods=['DELETE'])
def userDelete(id):
    for index, value in enumerate(users):
        if value['id'] == id:
            users.pop(index)
            return users, 200
    
    return {
        'message': 'El usuario ingresado no existe'
    }, 404
