from flask import request, jsonify
from src import app
from src.services.bd_connection import BDConnection

connect = BDConnection()

@app.route("/")
def hello():
    return "Hello World! ;)"

@app.route("/pedidos", methods=['GET'])
def listarpedidos():
    try:
        pedidos = connect.getPedidos()
        return jsonify(pedidos)
    except:
        return "Ops! Ocorreu um erro!", 500

@app.route("/addpedido", methods=['POST'])
def adicionarPedido():
    try:
        pedido = request.data();
        connect.addPedido(pedido)
        return "Pedido concluido com sucesso", 200
    except:
        return "Ops! Ocorreu um erro!", 500

@app.route("/delete/<id>", methods=['DELETE'])
def removerPedido(id):
    try:
        connect.deletePedido(id);
        return "Pedido excluido com sucesso!";
    except:
        return "Ops! Ocorreu um erro!", 500
