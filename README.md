# Projeto de Redes: Servidor e Cliente TCP/UDP

Este projeto consiste em um simples servidor e cliente TCP/UDP implementado em Python.

## Requisitos

- Python 3.6 ou superior

## Como executar

1. Baixe o código do projeto para a sua máquina local.
2. Abra o terminal (ou prompt de comando) e navegue até a pasta onde você salvou os arquivos do projeto.

### Inicie o servidor

Em seu terminal, execute o seguinte comando:

```bash
python server.py

### Inicie o cliente TCP
Abra um novo terminal e execute o seguinte comando:

```bash
python clientTCP.py

### Inicie o cliente UDP
Abra um novo terminal e execute o seguinte comando:

```bash
python clientUDP.py

### Funcionamento
O servidor TCP/UDP escuta nas portas 5000 e 5001 respectivamente. 
Quando um cliente se conecta e envia uma mensagem, 
o servidor irá responder com uma mensagem de reconhecimento (ACK).
