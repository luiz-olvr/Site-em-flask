from flask import Blueprint, render_template, request
from database.cliente import CLIENTES
cliente_route = Blueprint("Cliente", __name__)

@cliente_route.route("/")
def lista_cliente():
    return render_template('lista_clientes.html', clientes = CLIENTES)

@cliente_route.route('/', methods=["POST"])
def inserir_cliente():
    
    data = request.json
    novo_usuario ={
        "Id": len(CLIENTES) + 1,
        "Nome": data['nome'],
        "Email": data['email'],
    }
    return render_template('item_cliente.html', cliente= novo_usuario)

@cliente_route.route('/new')
def form_cliente():
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhes_cliente(cliente_id):
    return render_template('detalhe_cliente.html')


@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    return render_template('form_edit_cliente.html')


@cliente_route.route('/<int:cliente_id>/uptade', methods=["PUT"])
def atualizar_cliente(cliente_id):
    pass

@cliente_route.route('/<int:cliente_id>/deleta')
def deletar_cliente(cliente_id):
    pass






