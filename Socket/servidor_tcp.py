from socket import *

servidor = "127.0.0.1" #localhost
porta = 43210

obj_socket = socket(AF_INET, SOCK_STREAM) #AF_INET => identificaçao do servidor, SOCK_STREAM => trabalha 
                                                                                 # com o protocolo TCP
obj_socket.bind((servidor, porta))
obj_socket.listen(2) # Qtd max de clientes que a aplicação irá escutar/receber conexão

print("Aguardando cliente...")

while True:
    con, cliente = obj_socket.accept()
    print("Conectado com: ", cliente)
    while True:
        msg_reccebida = str(con.recv(1024))
        print("Recebemos: ", msg_reccebida)
        msg_enviada = b'Olah cliente'
        con.send(msg_enviada)
        break
    con.close()