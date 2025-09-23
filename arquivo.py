import csv

caminho: str = "/home/prod/env/dev/bootcamp_python/aula_04/exemplo.csv"

arquivo_csv: list = []

with open(file=caminho, mode="r", encoding='utf-8') as arquivo:
        leitor_csv = csv.DictReader(arquivo)

        for linha in leitor_csv:
                arquivo_csv.append(linha)

print(arquivo_csv)
