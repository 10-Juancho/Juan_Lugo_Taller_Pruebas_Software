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
