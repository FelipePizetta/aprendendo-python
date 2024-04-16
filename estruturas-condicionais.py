# Saque
saldo = 1750.00
saque = float(input("Informe o valor do saque: "))
if saldo >= saque:
    saldo -= saque
    print(f"Saque realizado! \n Saldo Atual: R${saldo}")
else:
    print("Saldo Insuficiente!")

# Idade
IDADE_ADULTO = 18
IDADE_VELHO = 65

idade = int(input("Qual sua idade? "))
if idade >= IDADE_ADULTO:
    print("CNH vence depois de 10 anos.")
elif idade >= IDADE_VELHO:
    print("CNH vence depois de 5 anos.")
else:
    print("Proibido tirar a CNH...")