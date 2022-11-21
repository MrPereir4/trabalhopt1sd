# Trabalho Sistemas Distribuidos
## Parte 1 - Vinnicius Pereira da Silva

## Para executa o projeto

- Clone o projeto

```bash
git clone https://github.com/Adlizm/sd_project.git
cd sd_project
```
### Preparando o ambiente

- Instale a dependencia paho-mqtt

```bash
pip3 install paho-mqtt
```
  
## Inicializando projeto
### Iniciando portais e interfaces
- Partindo da pasta do projeto
- Em terminais diferentes execute:


-Inicialize os portais
```bash
python3 client_portal.py
```

```bash
python3 admin_portal.py
```

-Inicialize as interfaces
```bash
python3 client.py
```

```bash
python3 admin.py
```

## Funcionalidades
- [x] Interface do Client com o Portal
- [x] Interface do Administrador com o Portal
- [x] Portal do Administrador
- [x] Portal do Cliente
- [x] Suporte a múltiplos portais

  
### Mecanismos de Comunicação
- Comunicação entre cliente e portal via sockets
- Comunicação entre admin e portal via sockets
- Comunicação entre portais via mqtt
