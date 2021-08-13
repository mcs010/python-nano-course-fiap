from Funcoes import *

usuarios ={}

opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
    else if opcao == "P":
        usuario = input("Digite o login do usuário a ser pesquisado: ")
        pesquisar(usuarios, usuario)
    else if opcao == "E":
        usuario = input("Digite o login do usuário a ser excluído: ")
        excluir(usuarios, usuario)
    else if opcao == "L":
        listar(usuarios)
    opcao = perguntar