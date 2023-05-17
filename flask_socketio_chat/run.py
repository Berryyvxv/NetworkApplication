from chatapp import create_app, socketio

app = create_app()

socketio.run(app)

#app, port=443,8080