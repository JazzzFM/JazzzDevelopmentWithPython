from flask import Flask, request
from flask.helpers import make_response
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    return response
    
@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    return "Estado anterior, su ip es {}".format(user_ip)

if __name__ == '__main__': 
    app.run()
    