#Rewrites the file
with open ("primeiro_arquivo.txt", "w") as arquivo:
    arquivo.write("\n Hakuna Matata!!")

#Prints the file content
with open ("primeiro_arquivo.txt", "r") as arquivo:
    print(conteudo)


#Prints line by line of the file
with open ("primeiro_arquivo.txt", "r") as arquivo:
    for linha in arquivo.readlines():
        print(conteudo)