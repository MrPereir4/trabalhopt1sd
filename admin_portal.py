
import random
from paho.mqtt import client as mqtt_client
import socket

from ast import literal_eval

customerHashTable = {}
productsHashTable = {}
print("Digite a porta do broker mqtt: (Padrao : 1883)")
portaBrokerMqtt = input()

print("Digite a porta da conexao tcp: ")
portaTcp = input()

broker = 'broker.emqx.io'
port = int(portaBrokerMqtt)
topic = "python/trbsd"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client










def admin_client_connect_socket():
    global portaTcp
    print("entrou")
    s = socket.socket()                         # Create a socket object
    host = "127.0.0.1"                          # Get local machine name
    port = int(portaTcp)                        # Reserve a port for your service.
    s.bind((host, port))                        # Bind to the port
    s.listen(5)                                 # Now wait for client connections.
    


    while True:
        c, addr = s.accept()                     # Establish connection with client.
        print('Got connection from', addr)
        newCustomer = c.recv(2048).decode()
        flag = newCustomer[0]
        newCustomer = newCustomer[1:]

        if flag == "1":          
            newCustomer = newCustomer.split("|")
            if int(newCustomer[3]) in customerHashTable:
                print("Cliente", newCustomerJSON["cpf"], "ja existe.")
                sendBack = "Cliente com esse cpf ja existe."
                c.send(sendBack.encode())
            else:
                newCustomerJSON = {"name": newCustomer[0], "age": newCustomer[1], "cpf": newCustomer[2]}
                hashForCustomer = int(newCustomer[3])
                customerHashTable[hashForCustomer] = newCustomerJSON
                print("Novo cliente", newCustomerJSON["name"], "inserido.")
                sendBack = "Novo cliente inserido com cid: " + str(hashForCustomer)
                c.send(sendBack.encode())

        elif flag == "2":
            
            newCustomer = newCustomer.split("|")
            print(newCustomer[3])
            if int(newCustomer[3]) in customerHashTable:
                customerHashTable.pop(int(newCustomer[3]))
                newCustomerJSON = {"name": newCustomer[0], "age": newCustomer[1], "cpf": newCustomer[2]}
                customerHashTable[int(newCustomer[3])] = newCustomerJSON
                print("Cliente ", newCustomerJSON['name'], " foi modificado.")
                c.send("Cliente foi modificado.".encode())
            else:
                print("CID não existe.")
                c.send("CID não existe.".encode())

        elif flag == "3":
            if int(newCustomer) in customerHashTable:
                
                newCustomerJSON = customerHashTable[int(newCustomer)]
                print("Cliente retornado")
                sendBack = "Cliente retornado: Nome: " + newCustomerJSON["name"] + "\nIdade: " + newCustomerJSON["age"] + "\nCPF: " + newCustomerJSON["cpf"]
                c.send(sendBack.encode())
            else:
                print("CID não existe.")
                c.send("CID não existe.".encode())
        

        elif flag == "4":
            print(newCustomer)

            if int(newCustomer) in customerHashTable:
                
                newCustomerJSON = customerHashTable[int(newCustomer)]
                customerHashTable.pop(int(newCustomer))
                print("Cliente removido")
                sendBack = "Cliente: " + newCustomerJSON["name"] + " removido."
                c.send(sendBack.encode())
            else:
                print("CID não existe.")
                c.send("CID não existe.".encode())

        if flag == "5":
            newCustomer = newCustomer.split("|")

            if int(newCustomer[3]) in productsHashTable:
                print("Produto ja existe.")
                sendBack = "Produto ja existe."
                c.send(sendBack.encode())
            else:

                newProductJSON = {"name": newCustomer[0], "price": newCustomer[1], "quantity": newCustomer[2]}
                hashForProduct = int(newCustomer[3])
                productsHashTable[hashForProduct] = newProductJSON
                print("Novo produto", newProductJSON["name"], "inserido.")
                sendBack = "Novo produto inserido com cid: " + str(hashForProduct)
                c.send(sendBack.encode())


        elif flag == "6":
            newCustomer = newCustomer.split("|")
            if int(newCustomer[3]) in productsHashTable:
                productsHashTable.pop(int(newCustomer[3]))
                newProductJSON = {"name": newCustomer[0], "price": newCustomer[1], "quantity": newCustomer[2]}
                productsHashTable[int(newCustomer[3])] = newProductJSON
                print("Produto ", newProductJSON['name'], " foi modificado.")
                c.send("Produto foi modificado.".encode())
            else:
                print("PID não existe.")
                c.send("PID não existe.".encode())

        elif flag == "7":
            if int(newCustomer) in productsHashTable:
                
                newProductJSON = productsHashTable[int(newCustomer)]
                print("Produto retornado")
                sendBack = "Produto retornado: Nome: " + newProductJSON["name"] + "\nPreco: " + newProductJSON["price"] + "\nEstoque: " + newProductJSON["quantity"]
                c.send(sendBack.encode())
            else:
                print("PID não existe.")
                c.send("PID não existe.".encode())

        elif flag == "8":
            print(newCustomer)

            if int(newCustomer) in productsHashTable:
                
                newProductJSON = productsHashTable[int(newCustomer)]
                productsHashTable.pop(int(newCustomer))
                print("Produto removido")
                sendBack = "Produto: " + newProductJSON["name"] + " removido."
                c.send(sendBack.encode())
            else:
                print("PID não existe.")
                c.send("PID não existe.".encode())

        else:
            print("")
        

        print("Tabela de cliente", customerHashTable)
        print("Tabela de produtos", productsHashTable)
        
        publish(client, "1" + str(customerHashTable))
        publish(client, "2" + str(productsHashTable))

def teste():
    admin_client_connect_socket()


def publish(client, mensagem):
    print(mensagem)
    msg_count = 0
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


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        global customerHashTable
        global productsHashTable
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        message = msg.payload.decode()
        

        if message[0] == "1":
            message = message[1:]
            customerHashTable = literal_eval(message)
        if message[0] == "2":
            message = message[1:]
            productsHashTable = literal_eval(message)
        
        print("AQUI!")
        print(customerHashTable)


    client.subscribe(topic)
    client.on_message = on_message

def run():
    teste()


if __name__ == '__main__':
    client = connect_mqtt()
    subscribe(client)
    client.loop_start()

    run()
    

