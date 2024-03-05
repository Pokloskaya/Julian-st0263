from concurrent import futures

import grpc
import Service_pb2 
import Service_pb2_grpc

import bootstrap

HOST = bootstrap.localhost

# FUNCIONES QUE VA A TENER EL SERVIDOR
#login()
#logout()
#buscar()
#indexar()

#Base de datos de los peers
dataBase = {}

class functions(Service_pb2_grpc.MainFunctionsServicer):
   
  def login(self, request, context):
    print("Request is received: " + str(request))
    dataBase[request.credentials] = request.fileName
    print("Peer with name: " + request.credentials + " connected.")
    print("ESTE ES EL NOMBRE DEL FILE: " + request.fileName)
    print("Data base: " + str(dataBase))

    return Service_pb2.OperationResponse(serverResponse="Conection is established!")
    #HAY QUE PONER LOS FILES DEL PEER EN EL SERVIDOR CENTRAL
  
  def logout(self, request, context):
    print("Request is received: " + str(request))
    if request.credentials in dataBase:
      del dataBase[request.credentials]
      print("Peer " + request.credentials + " disconnected.")
      print("Data base afted deleting the peer: " + str(dataBase))

    return Service_pb2.OperationResponse(serverResponse="Peer disconnected!")

  def search(self, request, context):
    print("Searching for file: ", request.credentials)
        
    for peer, file_name in dataBase.items():
      if file_name == request.credentials:
        # File found, return the peer's credentials
        return Service_pb2.OperationResponse(serverResponse=f"File '{request.credentials}' found. Owner: {peer}")
        
      # File not found
      return Service_pb2.OperationResponse(serverResponse=f"File '{request.credentials}' not found.")

  def index(self, request, context):
    pass
 
def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  Service_pb2_grpc.add_MainFunctionsServicer_to_server(functions(), server)
  server.add_insecure_port(HOST)
  print("Service is running... ")
  server.start()

  server.wait_for_termination()


if __name__ == "__main__":
  serve()