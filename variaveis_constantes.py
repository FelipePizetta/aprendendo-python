# Variáveis:
nome = 'Felipe Pizetta'
idade = 21
print(f'Variáveis Separadas: {nome}, {idade}')

nome, idade = ('Felipe Pizetta', 21)
print(f'Variáveis Juntas: {nome}, {idade}')

saldo_conta = 2000 # ?> Snake Case
print("Saldo da conta: " + saldo_conta)

# Constantes:
# Não existem constantes em Python (Apenas construa uma variável em letra maiúscula e não mude o valor)
ESTADOS = ["SP", "RJ", "RS", "MG", "SC"]
print(ESTADOS)

PI = 3.14
print(PI)

# Boas Práticas:
# 1. O padrão de nomes deve ser snake case;
# 2. Escolher nomes sugestivos;
# 3. Nome de constantes todo em maiúsculo.