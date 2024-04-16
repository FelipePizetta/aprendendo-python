nome = str(input("Qual seu nome? "))
idade = int(input("Qual sua idade? "))
conhecimento = str(input("Qual seu nível conhecimento? "))

mensagem = f'''
    Me chamo {nome}, 
    tenho apenas {idade} anos de idade, 
    e meu nivel de conhecimento é {conhecimento}.
'''

print(mensagem)