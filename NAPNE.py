from flask import Flask, abort, request, render_template
import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/cadastrar')
def mostrar_oi_aleky():
    x = '<form action="/gravar">'
    x += 'Nome: <input type="text" name="nome"><br>'
    x += 'sobrenome: <input type="text" name="sobrenome"><br>'
    x += '<input type="submit" value="Gravar"><br>'
    x += '</form>'
    return x


@app.route('/gravar', methods=['GET', 'POST'])
def parse_arg_from_requests():
    global lista
    lista.append(request.args.get('nome'))
    return 'Voce digitou: ' + request.args.get('nome') + ' ' + request.args.get('sobrenome')


@app.route('/listar')
def listar():
    x = ''
    for item in lista:
        x += item
    return x


if __name__ == '__main__':
    lista = []
    app.run()
