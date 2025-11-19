# 👤​ GESTIÓN DE USUARIOS - MINI APLICACIÓN WEB (FLASK).
Este documento describe el funcionamiento de una pequeña aplicación web desarrollada con Flask para realizar operaciones CRUD básicas sobre usuarios. También incluye instrucciones para ejecutar el servidor y probar los endpoints.

## 📌 DESCRIPCIÓN DEL PROYECTO.
La aplicación permite gestionar usuarios mediante un API sencilla, implementando las siguientes operaciones:
- Crear usuario (Create)
- Listar usuarios (Read)
- Eliminar usuario (Delete)

> Nota: En este ejmplo no se incluye el update.

## 🧩 LÓGICA DEL SISTEMA (user_manager.py).
El archivo contiene la clase **UserManager**, encargada de manejar las operaciones sobre los usuarios.
```Python
class UserManager:
def __init__(self):
self.users = []


def create_user(self, username, email):
user = {"username": username, "email": email}
self.users.append(user)
return user


def get_users(self):
return self.users


def delete_user(self, username):
self.users = [u for u in self.users if u["username"] != username]
```
## 🚀 APLICACIÓN WEB (app.py)
Este archivo contiene las rutas del API.
| Método   |      Ruta      | Descripccion  |
|----------|:-------------:|------:|
| GET      |  /users | Lista usuarios |
| POST |    /users   |  Crear usuario |
| DELETE | /users/<username> | Eliminar usuario |
```Python
from flask import Flask, request, jsonify
from user_manager import UserManager

app = Flask(__name__)
user_manager = UserManager()

@app.post("/users")
def create_user():
    data = request.json
    user = user_manager.create_user(data["username"], data["email"])
    return jsonify(user), 201

@app.get("/users")
def list_users():
    return jsonify(user_manager.get_users()), 200

@app.delete("/users/<username>")
def delete_user(username):
    user_manager.delete_user(username)
    return jsonify({"message": "Usuario eliminado"}), 200

if __name__ == "__main__":
    app.run(debug=True)

```

##  🧪 PRUEBAS DE HUMO.
Las pruebas de humo validan que las funciones críticas funcionan correctamente.
```python
from user_manager import UserManager

def test_user_manager_smoke():
    user_manager = UserManager()
    
    # Crear usuario
    user = user_manager.create_user("user1", "user1@example.com")
    assert user["username"] == "user1"
    assert len(user_manager.users) == 1

    # Eliminar usuario
    user_manager.delete_user("user1")
    assert len(user_manager.users) == 0
```
Ejecutarlas
```Python
pytest pruebas_funcionales/app_gestion_usuarios/test_smoke.py -v   
```

## ▶ COMO EJECUTAR EL SERVIDOR.
1. Asegurese de tener Flask instalado:
```Python
pip install flask
```
2. Ejecutar la aplicación:
```
Python app.py 
```
3. Veras algo como: 
```
Running on http://127.0.0.1:5000
```
## 🌐 COMPROBAR LOS ENDPOINTS.
- Listar usurios (GET)
Abre en navegador o Postman:
``` url
http://127.0.0.1:5000/users

```
Deberias ver:
> []

- Crear usuario (POST)
Usar postman oThunder client con JSON:
```Json
{
"username": "juan",
"email": "juan@example.com"
}
```

- Elimianr usuario (DELETE)
```Url
http://127.0.0.1:5000/users/juan

```
## 📝 NOTAS IMPORTANTES.
- El servidor corre en HTTP, no HTTPS.

- Si ves [], significa que la API funciona correctamente.

- Un error 404 en / es normal, la ruta correcta es /users.