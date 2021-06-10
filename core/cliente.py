import rpyc
from constRPYC import *


class Client:
    diretorio_conexao = rpyc.connect(DIR_SERVER, DIR_PORT)
    (address, port) = diretorio_conexao.root.exposed_lookup("ServerCalculadora")
    if address == 'error':
        print(port)
    else:
        print(f"Connection: {address}:{port}")
        num1 = int(input("Primeiro numero: "))
        num2 = int(input("Segundo numero: "))
        servidor_de_conexao = rpyc.connect(address, port)
        soma = servidor_de_conexao.root.exposed_sum(num1, num2)
        sub = servidor_de_conexao.root.exposed_sub(num1, num2)
        multi = servidor_de_conexao.root.exposed_multi(num1, num2)
        divi = servidor_de_conexao.root.exposed_divi(num1, num2)
        print(f"Soma: {soma}")
        print(f"Subtração: {sub}")
        print(f"Multiplicação: {multi}")
        print(f"Divisão: {divi}")
