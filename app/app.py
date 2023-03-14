import uuid
import redis

from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    r = redis.StrictRedis(host='redis', port=6379, decode_responses=True)
    response = r.keys('*')
    return response

@app.route('/user', methods=['POST'])
def user():
    r = redis.StrictRedis(host='redis', port=6379, decode_responses=True)
    username = request.args.get('username', type = str)
    r.set(username, "user")
    return 'agregando usuario: ' + username

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)