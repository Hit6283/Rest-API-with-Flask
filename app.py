from flask import Flask, request, jsonify

app = Flask(__name__)

#In-memory user data
users = [
    {"id": 1, "name": "Keshav", "email": "keshav@example.com"},
    {"id": 2, "name": "Hit", "email": "hit@example.com"}
]

#GET - List all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

#GET - Single user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

#POST - Create a new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    new_user = {
        "id": users[-1]["id"] + 1 if users else 1,
        "name": data["name"],
        "email": data["email"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

#PUT - Update a user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    user["name"] = data.get("name", user["name"])
    user["email"] = data.get("email", user["email"])
    return jsonify(user)

#DELETE - Remove a user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted"})


if __name__ == "__main__":
    app.run(debug=True)
