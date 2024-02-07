from passlib.hash import pbkdf2_sha256

# Definindo as variáveis
TAMANHO_MINIMO = 9
CARACTERES_ESPECIAIS = "!@#$%^&*()-+"

# Função para verificar se a senha é válida
def validar_senha(senha):


  # Verificando o tamanho da senha
  if len(senha) < TAMANHO_MINIMO:
    return {"válido": False, "motivo": "Senha muito curta"}

  # Verificando se a senha possui caracteres repetidos
  if len(set(senha)) < len(senha):
    return {"válido": False, "motivo": "Senha possui caracteres repetidos"}

  # Verificando se a senha possui todos os tipos de caracteres
  tem_digito = False
  tem_minuscula = False
  tem_maiuscula = False
  tem_especial = False
  for caractere in senha:
    if caractere.isdigit():
      tem_digito = True
    elif caractere.islower():
      tem_minuscula = True
    elif caractere.isupper():
      tem_maiuscula = True
    elif caractere in CARACTERES_ESPECIAIS:
      tem_especial = True

  if not tem_digito or not tem_minuscula or not tem_maiuscula or not tem_especial:
    return {"válido": False, "motivo": "Senha precisa de dígito, minúscula, maiúscula e caractere especial"}

  # A senha é válida
  return {"válido": True,"motivo": "Senha valida"}

# Função para verificar se a senha contém caracteres inválidos
def possui_caracteres_invalidos(senha):

  for caractere in senha:
    if caractere.isspace():
      return True
  return False

# Função para gerar um hash da senha
def gerar_hash_senha(senha):

  return pbkdf2_sha256.hash(senha)

# Função para verificar se o hash da senha é válido
def verificar_hash_senha(senha, hash_senha):
  
  return pbkdf2_sha256.verify(senha, hash_senha)
