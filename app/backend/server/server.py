from flask import Flask
from flask import Blueprint, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from  Docker!\n'



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)