from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def addition(a,b):
    return a+b

print(addition(10,3))