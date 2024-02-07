# PasswordValidator

README: Validação de Senha
Descrição:

Este projeto fornece uma API para validação de senhas. A API verifica se a senha fornecida atende aos seguintes critérios:

Tamanho mínimo de 9 caracteres
Ausência de caracteres repetidos
Presença de pelo menos um dígito, uma letra minúscula, uma letra secreta e um caractere especial
Ausência de espaços em branco
Funcionalidades:

Validação de senha via API
Verificação de caracteres inválidos
Geração de hash de senha (opcional)
Verificação de hash de senha (opcional)
Tecnologias:

Frasco
Pitão
Passlib
Uso da API:

Ponto final:

/validar-senha(método POST)
Entrada:

senha: string contendo uma senha a ser validada
Saída:

JSON com os seguintes campos:
válido: boolean diminuir se a senha é válida
motivo: string contendo a razão da invalidade da senha (se aplicável)
Exemplo de requisição:

curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"senha": "MinhaSenhaForte123!"}' \
  http://localhost:5000/validar-senha
Exemplo de resposta:

{
  "válido": true,
  "motivo": "Senha valida"
}
Instalação:

pip install -r requirements.txt
Execução:

python app.py
Documentação:

Detalhes da implementação das funções de validação de senha podem ser encontrados no código fonte.
As funções de geração e verificação de hash de senha são específicas e não são utilizadas na API de validação.
Observações:

Este projeto é um exemplo básico de validação de senha.

Contribuições:

Sugestões e melhorias são bem-vindas.