from random import randint
import rpyc
from constantes_rpyc import *
from rpyc.utils.server import ThreadedServer

servers = {}


class Directory(rpyc.Service):
    @staticmethod
    def exposed_register(self, server_name, ip_adress, port_number):
        addr = (ip_adress, port_number)
        if server_name not in servers:
            token = str(hash(server_name) + hash(randint(0, 50)))
            servers[server_name] = {'ip': addr, 'token': token}
            print(f"Full {servers}")
            print(f"[{server_name}] {ip_adress}:{port_number}\n[{server_name}] {token}\n\n")
            success = (True, token)
            return success
        else:
            failure = (False, "null")
            return failure

    @staticmethod
    def exposed_update_register(self, server_name, ip_adress, port_number, token):
        if servers[server_name]['token'] == token:
            addr = (ip_adress, port_number)
            servers[server_name]['ip'] = addr
            print(f"Atualizado {server_name} = {servers[server_name]}")
            return True
        else:
            return False

    def exposed_unregister(self, server_name, token):
        if servers[server_name]['token'] == token:
            servers.pop(server_name)
            print(f"Removido {server_name}")
            print(f"Completo: {servers}")
            return True
        else:
            return False
    @staticmethod
    def exposed_lookup(self, server_name):
        if server_name in servers:
            return servers[server_name]['ip']
        else:
            notreg = ("error", "Serviço não registrado")
            return notreg


if __name__ == "__main__":
    print(f"Server iniciado na porta {DIR_PORT}. Aguardando requisições")
    server_dir = ThreadedServer(Directory, port=DIR_PORT, protocol_config={"allow_public_attrs": True})
    server_dir.start()
