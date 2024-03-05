from flask import Flask, request, jsonify
import requests #NO SE PARA QUE ES ESTO

import grpc
import Service_pb2
import Service_pb2_grpc

#esto hay que instalarlo con pip???????????
import threading

import socket
import signal
import sys

import bootstrap

ipAddress = socket.gethostbyname(socket.gethostname())
channel = grpc.insecure_channel(bootstrap.localhost) #ESTO DESPUES TIENE QUE SER UN PARAMETRO DEL CONFIG
stub = Service_pb2_grpc.MainFunctionsStub(channel)

#iniciialar flask
app = Flask(__name__)
@app.route('/', methods=['POST'])



def receive():
    data = request.get_json()
    respuesta = "xd te respondo"
    print(respuesta)
    return jsonify(respuesta), 200

def send_download():
    url = "http://localhost:8081/"
    message = "hola, te mando un mensaje"
    pregunta = requests.post(url, json=message)
    

def iniciar_flask(): #LOCALHOST ES DRECCON IP
    app.run(host='localhost', port=bootstrap.puertoFlask)


def signal_handler(sig, frame):
    print("Ctrl+C detected, cleaning up and exiting...")
    # Perform cleanup actions here, like sending a message to the server

    response = stub.logout(Service_pb2.Credentials(credentials=messageToServer))  
    print("Response received: " + str(response.serverResponse))
    sys.exit(0)

def run():

    #ESTO DESPUES TIENE QUE SER UN PARAMETRO DEL CONFIG
    file_path = "image.txt"
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            print("File content: " + file_content)
    except FileNotFoundError:
        print("No images found.")

    while(True):

        # Register signal handler for Ctrl+C
        signal.signal(signal.SIGINT, signal_handler)

        print("Enter 1 to log in: ")
        print("Enter 2 to search files: ")
        print("Enter 3 to index: ")
        print("Enter 4 to logout: ")

        #decrle al server de un peer que queiro descargar
        print("Enter 5 to download: ")
        

        action = input()

        if action == "1":
        
            print("My IP address is: " + ipAddress)
            messageToServer = "peer1" #ESTO DESPUES TIENE QUE SER UN PARAMETRO DEL CONFIG
            response = stub.login(Service_pb2.Credentials(credentials=messageToServer))  
            print("Response received: " + str(response.serverResponse))
            #enviar mis archivos al servidor central ESTO ME FALTA

        if action == "2":
            pass

        if action == "3":
            pass

        if action == "4":
            pass

        if action == "5":
            send_download()
            


if __name__ == "__main__":
    flask_hilo = threading.Thread(target=iniciar_flask) #YO DEPSUES HAGO EL BOOTSTRAP
    flask_hilo.daemon = True
    flask_hilo.start()
    run()
    
    