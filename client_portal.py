import socket
import random

from ast import literal_eval

from paho.mqtt import client as mqtt_client





def connect_mqtt() -> mqtt_client:
    global customerHashTable2
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connectado ao MQTT Broker!")
        else:
            print("Falha ao se conectar, retorna codigo: %d\n", rc)

    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        global customerHashTable2
        global productsHashTable2
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        message = msg.payload.decode()
        if message[0] == "1":
            message = message[1:]
            customerHashTable2 = literal_eval(message)
        if message[0] == "2":
            message = message[1:]
            productsHashTable2 = literal_eval(message)
        
        print("AQUI!")
        print(customerHashTable2)


    client.subscribe(topic)
    client.on_message = on_message


def publish(client, mensagem):
    while True:
        msg = mensagem
        result = client.publish(topic, msg)
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
            break
        else:
            print(f"Failed to send message to topic {topic}")
            break

def customer_client_connect_socket():
    global portaTcp
    global customerHashTable2
    global productsHashTable2
    print("Conectou tcp cliente")
    s = socket.socket()                         # Create a socket object
    host = "127.0.0.1"                          # Get local machine name
    port = int(portaTcp)                                # Reserve a port for your service.
    s.bind((host, port))   
    ordersHashTable = {}                        # Bind to the port
    s.listen(5)                                 # Now wait for client connections.
    


    while True:
        c, addr = s.accept()                     # Establish connection with client.
        print('Got connection from', addr)
        order = c.recv(2048).decode()
        flag = order[0]
        order = order[1:]
        
        if int(flag) == 1:
            newOrder = order

            if int(newOrder) in customerHashTable2:
                orderJSON = {"customer": newOrder, "products": []}
                hashForOrder = hash(newOrder[0])
                ordersHashTable[hashForOrder] = orderJSON
                print("Novo pedido inserido.")
                sendBack = "Novo pedido inserido com oid: " + str(hashForOrder)
                c.send(sendBack.encode())
            else:
                print("Cliente não existe.")
                sendBack = "Cliente não existe."
                c.send(sendBack.encode())


            

        elif int(flag) == 2:
            modOrder = order.split("|")
            cnt = 0
            if int(modOrder[0]) in ordersHashTable: #Checa se oid existe
                if int(modOrder[1]) in customerHashTable2: #Chega se o cliente existe
                    for prod in literal_eval(modOrder[2]): #Itera pelos produtos
                        for key, value in productsHashTable2.items():
                            if key == int(prod[0]): #Verificar se o produto existe
                                if int(value["quantity"]) > 0: #e se tem em estoque
                                    productsHashTable2[key]["quantity"] = str(int(value["quantity"]) - int(prod[1])) #remover do estoque a quanridade comprada
                                    
                                else:
                                    literal_eval(modOrder[2]).pop(cnt) #se tiver nada de estoque remove produto

                            cnt = cnt + 1

                    print("Ordem modificada: ", modOrder)
                    ordersHashTable.pop(int(modOrder[0]))
                    orderJSON = {"customer": modOrder[1], "products": literal_eval(modOrder[2])}
                    ordersHashTable[int(modOrder[0])] = orderJSON
                    print("Tabela de produtos", productsHashTable2)
                    print("Pedido foi modificado.")
                    publish(client, "2"+str(productsHashTable2))
                    c.send("Pedido foi modificado.".encode())
                else:
                    print("Cliente nao existe.")
                    c.send("Cliente nao existe.".encode())
            else:
                print("OID não existe.")
                c.send("OID não existe".encode())
        

        elif int(flag) == 3:
            modOrder = order.split("|")

            if int(modOrder[1]) in customerHashTable2: #Autenticar cliente
                if int(modOrder[0]) in ordersHashTable: #Chega se existe a ordem
                    thisOrder = ordersHashTable[int(modOrder[0])]

                    products = thisOrder["products"]
                    valorTotal = 0
                    prodNames = ""
                    for prod in products:
                        prodName = productsHashTable2[int(prod[0])]["name"]
                        prodPrice = productsHashTable2[int(prod[0])]["price"]
                        prodNames = prodNames + prodName + " - " + prod[1] + " unidades" + "\n"
                        valorTotal = valorTotal + int(prod[1]) * int(prodPrice)


                    print("Listagem retornada")
                    sendBack = "Produtos: \n" + prodNames + "Valor total: R$" + str(valorTotal)
                    c.send(sendBack.encode()) 

                else:
                    print("OID não existe.")
                    c.send("OID não existe".encode()) 

            else:

                print("Cliente nao existe.")
                c.send("Cliente nao existe.".encode())
            
        elif int(flag) == 4:
            cid = order
            if int(cid) in customerHashTable2: #Checa se existe o cliente
                sendBack = ""
                for orderKey, value in ordersHashTable.items():
                    if value["customer"] == cid:

                        products = value["products"]
                        valorTotal = 0

                        for prod in products:
                            prodPrice = productsHashTable2[int(prod[0])]["price"]
                            valorTotal = valorTotal + int(prod[1]) * int(prodPrice)

                        
                        sendBack = sendBack + "OID: " + str(orderKey) + " - R$" + str(valorTotal) + "\n"
                        
                print("Listagem retornada")        
                c.send(sendBack.encode()) 
            else:         
                print("Cliente nao existe.")
                c.send("Cliente nao existe.".encode()) 

        elif int(flag) == 5:
            modOrder = order.split("|")

            if int(modOrder[1]) in customerHashTable2: #Checa se existe o cliente
                thisOrder = ordersHashTable[int(modOrder[0])]
                productsOfOrder = thisOrder["products"]

                for prod in productsOfOrder:
                    productsHashTable2[int(prod[0])]["quantity"] = str(int(productsHashTable2[int(prod[0])]["quantity"]) + int(prod[1])) #remover do estoque a quanridade comprada
                    print(str(int(value["quantity"]) - int(prod[1])))

                ordersHashTable.pop(int(modOrder[0]))
                print("Tabela de produtos apos remocao", productsHashTable2)
                publish(client, "2"+str(productsHashTable2))
                c.send("Ordem removida.".encode()) 
            else:
                print("Cliente nao existe.")
                c.send("Cliente nao existe.".encode()) 
        else:
            print("dasd")
    
        print("Lista de pedidos: ", ordersHashTable)





if __name__ == '__main__':
    customerHashTable2 = {}
    productsHashTable2 = {}

    global portaBrokerMqtt

    print("Digite a porta do broker mqtt: (Padrao : 1883)")
    portaBrokerMqtt = input()

    print("Digite a porta da conexao tcp: ")
    portaTcp = input()


    broker = 'broker.emqx.io'
    port = int(portaBrokerMqtt)
    topic = "python/trbsd"
    # generate client ID with pub prefix randomly
    client_id = f'python-mqtt-{random.randint(0, 1000)}'

    client = connect_mqtt()
    subscribe(client)
    client.loop_start()

    customer_client_connect_socket()

   

