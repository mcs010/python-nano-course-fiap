import json
'''
with open("bd.json", "r") as arq_json:
    dic = json.load(arq_json)
    for chave, dados in dic.items():
        print(chave + " " + str(dados))

'''

dicionario = {
    "CHAVES": ["CHAVES DO 8", "14/07/2020", "RECEP_01"],
    "QUICO": ["QUICO FLORES", "24/07/2020", "RAIOX_01"],
    "FLORINDA": ["DONA FLORINDA", "18/07/2020", "RECEP_03"]
}

with open("bd1.json", "w") as json_file:
    json.dump(dicionario, json_file)