nome = str(input("Qual seu nome? "))
idade = int(input("Qual sua idade? "))
formacao = str(input("Qual sua formação acadêmica? "))
conhecimento = str(input("Qual seu conhecimento? "))
print("\nOld Style: Meu nome é %s, tenho %s anos e sou formado em %s. Tenho conhecimento em: %s." % (nome, idade, formacao, conhecimento)) # %s
print("\n.format: Meu nome é {}, tenho {} anos e sou formado em {}. Tenho conhecimento em: {}.".format(nome, idade, formacao, conhecimento)) # Método .format
print(f"\n.f-String: Meu nome é {nome}, tenho {idade} anos e sou formado em {formacao}. Tenho conhecimento em: {conhecimento}.") # Método f-String

PI = 3.14159
print(f"Valor de PI: {PI: .2f}")
print(f"Valor de PI: {PI: 10.2f}")