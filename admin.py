import socket

def main_admin_opts():
    while True:
        print("________________________________")
        print("|Selecione uma opção           |")
        print("|1 - Manipular produto         |")
        print("|2 - Manipular Cliente         |")
        print("--------------------------------")

        mainOptSelected = input()

        if mainOptSelected == "1":
            print("________________________________")
            print("|Selecione uma opção           |")
            print("|1 - Inserir produto           |")
            print("|2 - Modificar produto         |")
            print("|3 - Recuperar produto         |")
            print("|4 - Remover produto           |")
            print("|5 - Finalizar                 |")
            print("--------------------------------")



            inputSelectedPrd = input()
            
            if int(inputSelectedPrd) == 1:
                print("inserir produto")
                print("Insira o nome do produto: ")
                productName = input()
                print("Insira o valor do produto: ")
                productPrice = input()
                print("Insira a quantidade em estoque do produto: ")
                productStorage = input()
                productPid = hash(productName)
                newProduct = [productName, productPrice, productStorage, productPid]
                inserir_produto(newProduct)
            elif int(inputSelectedPrd) == 2:
                print("Editar produto")
                print("Insira o PID do produto a ser modificado")
                productPid = input()
                print("Insira o nome do produto: ")
                productName = input()
                print("Insira o valor do produto: ")
                productPrice = input()
                print("Insira a quantidade em estoque do produto: ")
                productStorage = input()
                newProduct = [productName, productPrice, productStorage, productPid]
                editar_product(newProduct)
            elif int(inputSelectedPrd) == 3:
                print("Recuperar produto")
                print("Insira o pid do produto a ser retornado:")
                productPid = input()
                retornar_produto(productPid)
            elif int(inputSelectedPrd) == 4:
                print("Remove produto")
                print("Insira o PID do produto a ser removido")
                productToRemovePID = input()
                remover_produto(productToRemovePID)
            elif int(inputSelectedPrd) == 5:
                break
            else:
                continue



        else:
            print("________________________________")
            print("|Selecione uma opção           |")
            print("|1 - Inserir novo cliente      |")
            print("|2 - Editar cliente            |")
            print("|3 - Recuperar cliente         |")
            print("|4 - Remover cliente           |")
            print("|5 - Finalizar                 |")
            print("--------------------------------")
            inputSelected = input()
            
            if int(inputSelected) == 1:
                print("Inserir cliente")
                print("Insira o nome do cliente: ")
                customerName = input()
                print("Insira a idade do cliente: ")
                customerAge = input()
                print("Insira o cpf do cliente: ")
                customerCPF = input()
                customerCid = hash(customerCPF)
                newCustomer = [customerName, customerAge, customerCPF, customerCid]
                inserir_cliente(newCustomer)
            elif int(inputSelected) == 2:
                print("Editar cliente")
                print("Insira o CID do cliente a ser modificado")
                customerCid = input()
                print("Insira o nome do cliente: ")
                customerName = input()
                print("Insira a idade do cliente: ")
                customerAge = input()
                print("Insira o cpf do cliente: ")
                customerCPF = input()
                customerToEdit = [customerName, customerAge, customerCPF, customerCid]
                editar_cliente(customerToEdit)

            elif int(inputSelected) == 3:
                print("Recuperar cliente")
                print("Insira o cid do cliente a ser retornado:")
                customerCid = input()
                retornar_cliente(customerCid)
            elif int(inputSelected) == 4:
                print("Remove cliente")
                print("Insira o cliente a ser removido")
                customerToRemoveCID = input()
                remover_cliente(customerToRemoveCID)
            elif int(inputSelected) == 5:
                break
            else:
                continue



def inserir_cliente(customer):
    global porta
    s = socket.socket()                    # Create a socket object
    host = "127.0.0.1"                     # Get local machine name
    port = int(porta)                          # Reserve a port for your service.

    s.connect((host, port))
    while True:
        customerName = customer[0] + "|"
        customerAge = customer[1] + "|"
        customerCPF = customer[2] + "|"
        customerCID = customer[3]

        s.send("1".encode())
        s.send(customerName.encode())
        s.send(customerAge.encode())
        s.send(customerCPF.encode())
        s.send(str(customerCID).encode())
        response = s.recv(1024).decode()
        if response != '':
            print(response)
            s.close()
            break
        

def editar_cliente(customer):
    global porta
    s = socket.socket()                    # Create a socket object
    host = "127.0.0.1"                     # Get local machine name
    port = int(porta)

    s.connect((host, port))
    while True:
        customerName = customer[0] + "|"
        customerAge = customer[1] + "|"
        customerCPF = customer[2] + "|"
        customerCID = customer[3]

        s.send("2".encode())
        s.send(customerName.encode())
        s.send(customerAge.encode())
        s.send(customerCPF.encode())
        s.send(customerCID.encode())
        response = s.recv(1024).decode()
        if response != '':
            print(response)
            s.close()
            break


def retornar_cliente(cid):
    global porta
    s = socket.socket()                    # Create a socket object
    host = "127.0.0.1"                     # Get local machine name
    port = int(porta)

    s.connect((host, port))
    while True:

        s.send("3".encode())
        s.send(cid.encode())
        response = s.recv(1024).decode()
        if response != '':
            print(response)
            s.close()
            break

def remover_cliente(cid):
    global porta
    s = socket.socket()                    # Create a socket object
    host = "127.0.0.1"                     # Get local machine name
    port = int(porta)

    s.connect((host, port))
    while True:

        s.send("4".encode())
        s.send(cid.encode())
        response = s.recv(1024).decode()
        if response != '':
            print(response)
            s.close()
            break



def inserir_produto(product):
    global porta
    s = socket.socket()                    # Create a socket object
    host = "127.0.0.1"                     # Get local machine name
    port = int(porta)                           # Reserve a port for your service.

    s.connect((host, port))
    while True:
        productName = product[0] + "|"
        productAge = product[1] + "|"
        productCPF = product[2] + "|"
        productPID = product[3]

        s.send("5".encode())
        s.send(productName.encode())
        s.send(productAge.encode())
        s.send(productCPF.encode())
        s.send(str(productPID).encode())
        response = s.recv(1024).decode()
        if response != '':
            print(response)
            s.close()
            break
        

def editar_product(product):
    global porta
    s = socket.socket()                    # Create a socket object
    host = "127.0.0.1"                     # Get local machine name
    port = int(porta)

    s.connect((host, port))
    while True:
        productName = product[0] + "|"
        productAge = product[1] + "|"
        productCPF = product[2] + "|"
        productPID = product[3]

        s.send("6".encode())
        s.send(productName.encode())
        s.send(productAge.encode())
        s.send(productCPF.encode())
        s.send(productPID.encode())
        response = s.recv(1024).decode()
        if response != '':
            print(response)
            s.close()
            break


def retornar_produto(pid):
    global porta
    s = socket.socket()                    # Create a socket object
    host = "127.0.0.1"                     # Get local machine name
    port = int(porta)

    s.connect((host, port))
    while True:

        s.send("7".encode())
        s.send(pid.encode())
        response = s.recv(1024).decode()
        if response != '':
            print(response)
            s.close()
            break

def remover_produto(pid):
    global porta
    s = socket.socket()                    # Create a socket object
    host = "127.0.0.1"                     # Get local machine name
    port = int(porta)

    s.connect((host, port))
    while True:

        s.send("8".encode())
        s.send(pid.encode())
        response = s.recv(1024).decode()
        if response != '':
            print(response)
            s.close()
            break

def startAdmin():
    global porta
    print("Digite a porta para a conexao tcp: ")
    porta = input()

    main_admin_opts()
    

porta = ""
startAdmin()