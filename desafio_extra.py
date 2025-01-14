# Instruções:

CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que insira seu nome.
nome_usuario = input("Digite o seu nome: ")

# 2) Solicita ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
salario_usuario = float(input("Digite o seu salario: "))

# 3) Solicita ao usuário para inserir a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
bonus_usuario = float(input("Digite o seu bonus: "))

# 4) Calcule o valor do bonus final.
valor_bonus =  CONSTANTE_BONUS + salario_usuario * bonus_usuario

# 5) Imprime a mensagem.
print(f"O usuario {nome_usuario} possui o bonus de {valor_bonus} reais.")

