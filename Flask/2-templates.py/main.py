from flask import Flask, request, render_template 
from flask.helpers import make_response
from werkzeug.utils import redirect

app = Flask(__name__)

todos = ['Comprar café',
        'Solicitud de compra',
        'Entregar el producto']

@app.route('/')
def index():
    user_ip = request.remote_addr
    response = make_response(redirect('/hello'))
    response.set_cookie('user_ip', user_ip)
    return response
    
@app.route('/hello')
def hello():
    user_ip = request.cookies.get('user_ip')
    context = {
        'user_ip' : user_ip,
        'todos' : todos
    }
    return render_template('hello.html',
            **context)
 
