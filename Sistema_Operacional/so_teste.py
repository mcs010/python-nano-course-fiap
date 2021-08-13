import platform
import getpass
from datetime import datetime

print("Nome máquina:........", platform.node())
print("Arquitetura:........", platform.architecture())
print("Sistema Operacional:........", platform.system())
print("Versão do SO:........", platform.release())
print("Processador:........", platform.processor())
print("Versão do Python:........", platform.python_version())

print(datetime.now)
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)
print(datetime.now().hour)

usuario = getpass.getuser()
senha = getpass.getpass("Digite sua senha:....")

if usuario == 'usertricaster' and senha == 'Hello':
    print('Bem vinda Adele')
else:
    print('Voce nao tem acesso')