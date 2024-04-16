# FOR
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print()

print("Executado no final")

# RANGE
for numero in range(0, 10):
    print(numero, end=" ")
else:
    print()

for tabuada in range(0, 51, 5):
    print(tabuada, end=" ")
else:
    print()

# WHILE
saldo = 1000
opcao = -1

while opcao != 0:
    opcao = int(input("\n[1] Sacar \n[2] Extrato \n[0]Sair \n"))

    if opcao == 1:
        saque = float(input("Informe o valor que gostaria de sacar: "))
        if saque > saldo:
            print("Saque maior que o limite...")
        else:
            saldo -= saque
            print("Sacando... \n")
    elif opcao == 2:
        print(f"\nExibindo o extrato...\n Saldo Atual: R${saldo}")