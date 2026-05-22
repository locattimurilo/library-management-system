from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def saudacoes():
    return "Esta é a API da biblioteca."

ITENS = [
    {'id': uuid.uuid4().hex, 'title': 'Guerra e Paz', 'genre': 'Histórico', 'available': False},
    {'id': uuid.uuid4().hex, 'title': 'Crime e Castigo', 'genre': 'Psicológico', 'available': True},
    {'id': uuid.uuid4().hex, 'title': 'A Menina que Roubava Livros', 'genre': 'Ficção Histórica', 'available': True},
    {'id': uuid.uuid4().hex, 'title': 'Duna', 'genre': 'Ficção Científica', 'available': False},
    {'id': uuid.uuid4().hex, 'title': 'O Guia do Mochileiro das Galáxias', 'genre': 'Ficção Científica', 'available': True},
    {'id': uuid.uuid4().hex, 'title': 'O Iluminado', 'genre': 'Terror', 'available': False},
    {'id': uuid.uuid4().hex, 'title': 'Drácula', 'genre': 'Terror', 'available': True},
    {'id': uuid.uuid4().hex, 'title': 'A Estrada', 'genre': 'Pós-Apocalíptico', 'available': True}
]

@app.route('/itens', methods=['GET', 'POST'])
def todos_os_itens():
    objeto_resposta = {'status': 'sucesso'}
    if request.method == 'POST':
        dados_post = request.get_json()
        ITENS.append({
            'id': uuid.uuid4().hex,
            'title': dados_post.get('title'),
            'genre': dados_post.get('genre'),
            'available': dados_post.get('available')
        })
        objeto_resposta['message'] = 'Item Adicionado!'
    else:
        objeto_resposta['items'] = ITENS
        objeto_resposta['message'] = 'Itens Carregados!'
    return jsonify(objeto_resposta)

@app.route('/itens/<item_id>', methods=['PUT', 'DELETE'])
def item_individual(item_id):
    objeto_resposta = {'status': 'sucesso'}
    if request.method == 'PUT':
        dados_post = request.get_json()
        remover_item(item_id)
        ITENS.append({
            'id': uuid.uuid4().hex,
            'title': dados_post.get('title'),
            'genre': dados_post.get('genre'),
            'available': dados_post.get('available')
        })
        objeto_resposta['message'] = 'Item Atualizado!'
    if request.method == 'DELETE':
        remover_item(item_id)
        objeto_resposta['message'] = 'Item Removido!'
    return jsonify(objeto_resposta)

def remover_item(item_id):
    for item in ITENS:
        if item['id'] == item_id:
            ITENS.remove(item)
            return True
    return False

if __name__ == '__main__':
    app.run(debug=True)
