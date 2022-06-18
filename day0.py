from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
@aap.route('/users')
def get_user_details():
    return 'there is no db'
app.run()