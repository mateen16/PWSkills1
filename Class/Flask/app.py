from flask import Flask, request

app = Flask(__name__)

# @app.route('/add')
# def addition(a,b):
#     return a+b

@app.route('/home')
def homepage():
    return "Welcome to Flask"



if __name__ == '__main__':
    app.run(host='0.0.0.0')