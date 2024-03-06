from flask import Flask, request, jsonify
import requests 

import grpc
import Service_pb2
import Service_pb2_grpc

import threading

import socket
import signal
import sys

import bootstrap

ipAddress = socket.gethostbyname(socket.gethostname())
channel = grpc.insecure_channel(bootstrap.localhost) 
stub = Service_pb2_grpc.MainFunctionsStub(channel)
myFiles = []
myFiles.append(bootstrap.file) 
myFiles.append("exampleGlobal.txt")
print(myFiles)

#------------------ SERVIDOR FLASK ------------------

#iniciialar flask
app = Flask(__name__)

@app.route('/', methods=['POST'])
def receive():
    fileToDownload = request.get_json()
    if fileToDownload in myFiles:
        return jsonify(fileToDownload), 200
    else:
        return jsonify("file not found"), 404
    # data = request.get_json()
    # respuesta = "xd te respondo"
    # print("Mensaje: " + data)
    # return jsonify(respuesta), 200

def send_download():
    url = input("Enter the http direction of the peer you want to download from: ")
    message = input("Enter the file you want to download: ")
    #url = "http://localhost:8082/" #ESTO DESPUES TIENE QUE SER UN PARAMETRO VARIABLE QUE SE RECBE POR EL BOOTSTRAP
    #^^porque eso es el peer que tiene el archivo
    wantedFile = requests.post(url, json=message)
    print("answer: " + wantedFile.text)
    myFiles.append(wantedFile.text)
    print("my files after downloading from other peer: " + str(myFiles))

def iniciar_flask(): #LOCALHOST ES DRECCON IP
    app.run(host='localhost', port=bootstrap.puertoPserver)


def signal_handler(sig, frame):
    print("Ctrl+C detected, cleaning up and exiting...")
    # Perform cleanup actions here, like sending a message to the server

    response = stub.logout(Service_pb2.Credentials(peerName=bootstrap.peerName))  
    print("Response received: " + str(response.serverResponse))
    sys.exit(0)

#------------------ SERVIDOR FLASK ------------------


def run():

    #------------ESTO PUEDE SER DEL ARCHIVO QUE LE VOY A MANDAR----------------
    #ESTO DESPUES TIENE QUE SER UN PARAMETRO DEL CONFIG
    file_path = "image.txt"
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            print("File content: " + file_content)
    except FileNotFoundError:
        print("No images found.")
    #------------ESTO PUEDE SER DEL ARCHIVO QUE LE VOY A MANDAR----------------

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
            messageToServer = bootstrap.peerName #ESTO DESPUES TIENE QUE SER UN PARAMETRO DEL CONFIG
            print("este es el fle name: " + str(myFiles))
            response = stub.login(Service_pb2.Credentials(peerName=messageToServer, fileName=myFiles))  
            print("Response received: " + str(response.serverResponse))
            #enviar mis archivos al servidor central ESTO ME FALTA

        #search files
        if action == "2":
            searchFiles = input("Ented the file you want to search: ")
            response = stub.search(Service_pb2.Credentials(peerName=searchFiles))  
            print(str(response.serverResponse))

        #index files
        if action == "3":
            messageToServer = bootstrap.peerName
            response = stub.login(Service_pb2.Credentials(peerName=messageToServer, fileName=myFiles)) 

        #logout
        if action == "4":
            messageToServer = bootstrap.peerName
            response = stub.search(Service_pb2.Credentials(peerName=messageToServer))  
            print("Response received: " + str(response.serverResponse))

            sys.exit(0)

        if action == "5":
            send_download()


if __name__ == "__main__":
    flask_hilo = threading.Thread(target=iniciar_flask) 
    flask_hilo.daemon = True
    flask_hilo.start()
    run()
    
    