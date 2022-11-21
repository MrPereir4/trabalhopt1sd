import socket


def main_customer_opts():
    while True:

        print("________________________________")
        print("|Selecione uma opção           |")
        print("|1 - Inserir pedido            |")
        print("|2 - Modificar pedido          |")
        print("|3 - Enumerar pedido           |")
        print("|4 - Enumerar pedidos          |")
        print("|5 - Cancelar pedido           |")
        print("|6 - Sair                      |")
        print("--------------------------------")


        mainOptSelected = input()
            
        if int(mainOptSelected) == 1:
            print("Inserir pedido")
            print("Insira o CID do cliente: ")
            customerCID = input()
            newOrder = [customerCID]
            criar_pedido(newOrder)
        elif int(mainOptSelected) == 2:
            print("Modificar o pedido")
            print("Insira o OID do Pedido: ")
            orderOID = input()
            print("Insira o CID do cliente: ")
            customerCID = input()

            print("Quantos produtos devem ser adicionados?")
            productsQuantity = input()
            num = 0
            productToInsert = []
            while num != int(productsQuantity):
                print("Inserindo o produto numero: " + str(num + 1))
                print("Insira o pid do produto a ser comprado: ")
                productPID = input()
                print("Insira a quantidade")
                productQnt = input()
                productToInsert.append([productPID, productQnt])
                num += 1

            newOrder = [orderOID, customerCID, productToInsert]
            modificar_pedido(newOrder)
        elif int(mainOptSelected) == 3:
            print("Enumerar pedido")
            print("Insira o OID do Pedido: ")
            orderOID = input()
            print("Insira o CID do cliente: ")
            customerCID = input()
            order = [orderOID, customerCID]
            enumerar_pedido(order)
        elif int(mainOptSelected) == 4:
            print("Enumerar pedidos")
            print("Insira o CID do cliente: ")
            customerCID = input()
            enumerar_pedidos(customerCID)
        elif int(mainOptSelected) == 5:
            print("Cancelar pedido")
            print("Insira o OID do Pedido: ")
            orderOID = input()
            print("Insira o CID do cliente: ")
            customerCID = input()
            order = [orderOID, customerCID]
            cancelar_pedido(order)

        elif int(mainOptSelected) == 6:
            break
        else:
            continue


def criar_pedido(order):
    global porta
    s = socket.socket()                    # Create a socket object
    host = "127.0.0.1"                     # Get local machine name
    port = int(porta)                           # Reserve a port for your service.

    s.connect((host, port))
    while True:
        customerCID = str(order[0])
        s.send("1".encode())
        s.send(customerCID.encode())
        

        response = s.recv(1024).decode()
        if response != '':
            print(response)
            s.close()
            break



def modificar_pedido(order):
    global porta
    s = socket.socket()                    # Create a socket object
    host = "127.0.0.1"                     # Get local machine name
    port = int(porta)                           # Reserve a port for your service.

    s.connect((host, port))
    while True:
        orderOID = str(order[0]) + "|"
        customerCID = str(order[1]) + "|"
        products = str(order[2])


        s.send("2".encode())
        s.send(orderOID.encode())
        s.send(customerCID.encode())
        s.send(products.encode())
        

        response = s.recv(1024).decode()
        if response != '':
            print(response)
            s.close()
            break


def enumerar_pedido(order):
    global porta
    s = socket.socket()                    # Create a socket object
    host = "127.0.0.1"                     # Get local machine name
    port = int(porta)                           # Reserve a port for your service.

    s.connect((host, port))
    while True:
        orderOID = str(order[0]) + "|"
        customerCID = str(order[1])


        s.send("3".encode())
        s.send(orderOID.encode())
        s.send(customerCID.encode())
        

        response = s.recv(1024).decode()
        if response != '':
            print(response)
            s.close()
            break


def enumerar_pedidos(cid):
    global porta
    s = socket.socket()                    # Create a socket object
    host = "127.0.0.1"                     # Get local machine name
    port = int(porta)                           # Reserve a port for your service.

    s.connect((host, port))
    while True:
        customerCID = str(cid)


        s.send("4".encode())
        s.send(customerCID.encode())
        

        response = s.recv(1024).decode()
        if response != '':
            print(response)
            s.close()
            break

def cancelar_pedido(order):
    global porta
    s = socket.socket()                    # Create a socket object
    host = "127.0.0.1"                     # Get local machine name
    port = int(porta)                           # Reserve a port for your service.

    s.connect((host, port))
    while True:
        orderOID = str(order[0]) + "|"
        customerCID = str(order[1])


        s.send("5".encode())
        s.send(orderOID.encode())
        s.send(customerCID.encode())
        

        response = s.recv(1024).decode()
        if response != '':
            print(response)
            s.close()
            break

def startCustomer():
    global porta
    print("Digite a porta para a conexao tcp: ")
    porta = input()

    main_customer_opts()
    

porta = ""
startCustomer()