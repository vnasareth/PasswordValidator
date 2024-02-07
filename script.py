from flask import Flask, request, jsonify
from validacao import validar_senha, possui_caracteres_invalidos

# Criando a API
app = Flask(__name__)

# Rota para página inicial
@app.route("/")
def index():
    return "Bem-vindo! Use a rota /validar-senha para validar uma senha."

# Rota para validação de senha
@app.route("/validar-senha", methods=["POST"])
def validar():
    
    # Obtendo a entrada da requisição
    json_data = request.get_json()

    # Verificando se a entrada contém a chave "senha"
    if "senha" not in json_data:
        return jsonify({"válido": False, "motivo": "A senha não foi fornecida"})

    # Obtendo a senha
    senha = json_data["senha"]

    # Verificando se a senha contém caracteres inválidos
    if possui_caracteres_invalidos(senha):
        return jsonify({"válido": False, "motivo": "A senha contém caracteres inválidos"})

    # Validando a senha
    resultado_validacao = validar_senha(senha)

    return jsonify(resultado_validacao)

if __name__ == "__main__":
    app.run(debug=True)
