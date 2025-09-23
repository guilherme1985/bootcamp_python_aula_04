# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
''' 
# SOLUÇAO 01
lista: list = [1,2,3,4,5,6,7,8,9,10]

for n in lista:
    print(n**2)
'''    

# 2. Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
'''
# SOLUCAO 02
lista: list = ["Python", "Java", "C++", "JavaScript"]

lista.remove("C++")
lista.append("Ruby")

print(lista)
'''

# 3. Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
'''
livro: dict = {"nome": "LivroABC", "autor":"Autor do ABC", "publicacao": 2000}
# print(livro["nome"])
# print(livro["autor"])

for chave, valor in livro.items():
    print(f"{chave} - {valor}")
'''

# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
'''
palavra: str = "paralelepipedo amarelo"

def conta_letra(texto: str) -> dict:
    conta = dict.fromkeys(['a', 'p', 'e'], 100)
    for l in texto:
        conta[l] = conta.get(l, 0) + 1
    return conta

contagem = conta_letra(palavra)

print(contagem)
'''

# 5. Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
'''
lista_compras: list = ["maçã", "banana", "cereja"]
precos: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
tt: float = 0

for f in lista_compras:
    vlr: list = precos[f] 
    tt = tt + precos[f]

print(f"Valores = {vlr}")
print(f"\nTotal = {tt}")

# ## SOLUCAO JORNADA
# lista_compras = ["maçã", "banana", "cereja"]
# precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
# 
# total = sum(precos[item] for item in lista_compras)
# 
# print(f"Preço total: {total}")
'''

# 6. Dada uma lista de emails, remova os duplicados e imprima a lista resultante.
##emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]

emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]

for n in emails:
    if emails.count(n) > 1:
        emails.remove(n)

print(emails)

# 7. Crie um programa que solicite ao usuário uma frase e conte o número de palavras na frase.
    # idades = [22, 15, 30, 17, 18]


# 8. Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
    # pessoas = [{"nome": "Ana", "idade": 25}, {"nome": "Carlos", "idade": 30}, {"nome": "Beatriz", "idade": 20}]


# 9.  Dado um conjunto de números, calcular a média.
    # numeros = {10, 20, 30, 40, 50}


# 10. Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
    # valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 11. Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
    # produtos = [{"id": 1, "nome": "Teclado", "preço": 100},    {"id": 2, "nome": "Mouse", "preço": 80}, {"id": 3, "nome": "Monitor", "preço": 300}]
# 12. Dados dois dicionários, fundi-los em um único dicionário.
    # dicionario1 = {"a": 1, "b": 2}
    # dicionario2 = {"b": 3, "c": 4}
# 13. Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
    # estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 5, "CPU": 0}
# 14. Dado um dicionário, criar listas separadas para suas chaves e valores.
    # dicionario = {"a": 1, "b": 2, "c": 3}
# 15. Dada uma string, contar a frequência de cada caractere usando um dicionário.
    # string = "engenharia de dados"
# Leitura. Para ler um arquivo CSV em Python utilizando o módulo nativo, você pode usar a combinação do comando with open... para abrir o arquivo e o método .reader() do módulo csv para ler o arquivo linha por linha. O uso de with assegura que o arquivo será fechado corretamente após sua leitura, mesmo que ocorram erros durante o processo. Abaixo está um exemplo básico de como realizar essa operação:

# 16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
# 17. Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.
# 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
# 19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.
# 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas