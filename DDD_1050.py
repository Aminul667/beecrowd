
table = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte"
}

ddd = int(input())
if ddd not in table.keys():
    print("DDD nao cadastrado")
else:
    print(table[ddd])