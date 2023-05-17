from flask import request
from flask_socketio import emit

from .extensions import socketio

users = {}

# Function that will be called when the "connect" event is received from the client side
@socketio.on("connect")
def handle_connect():
    print("Client connected!")

# Function that will be called when the "user_join" event is received from the client side
@socketio.on("user_join")
def handle_user_join(username):
    print(f"User {username} joined!")
    users[username] = request.sid

# Function that will be called when the "new_message" event is received from the client side
@socketio.on("new_message")
def handle_new_message(message):
    print(f"New message: {message}")
    username = None
    for user in users:
        if users[user] == request.sid:
            username = user
    emit("chat", {"message": message, "username": username}, broadcast=True)

# Function that will be called when the "image" event is received from the client side
@socketio.on("image")
def handle_image(image_data):
    print(f"Received Image data: {image_data}")
    emit("image", image_data, broadcast=True)
