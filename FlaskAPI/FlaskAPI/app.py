from flask import Flask, jsonify, request
from flask_cors import CORS
from validate_docbr import CPF
app = Flask(__name__)
CORS(app)

@app.route('/api/validate_cpf', methods=['POST'])
def api():
    data = request.get_json()
    cpf = data.get('cpf')

    try:
        cpf_validator = CPF()
        if cpf_validator.validate(cpf):
            return jsonify({'status': 'CPF válido'}), 200
        else:
            return jsonify({'status': 'CPF inválido'}), 400

    except Exception as e:
        return jsonify({'status': 'Erro na validação do CPF', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
