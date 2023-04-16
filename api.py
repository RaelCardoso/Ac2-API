from flask import Flask, jsonify

app = Flask(__name__)

livros = [
    {'id': 1,'titulo': 'A lei','autor': 'Frédéric Bastiat'},
    {'id': 2,'titulo': 'A arte da geurra','autor': 'Sun Tzu'},
    {'id': 3,'titulo': 'Sapiens: Uma Breve História da Humanidade', 'autor': 'Yuval Noah Harari'}
]

@app.route('/livros', methods=['GET'])
def obter_livros():
    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)