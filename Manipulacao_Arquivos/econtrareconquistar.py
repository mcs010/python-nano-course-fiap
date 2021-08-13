texto = "Eu amo python!"
        #012345012345

print(texto.find("o")) # Printa o índice da 1a ocorrencia da letra "o"

print(text[texto.find("o")+1:].find("o")) # Printa 5 -> índice da 2a ocorrencia da letra "o" após slice

print(texto.split(" ")) # Printa ['Eu', 'amo', 'python!']