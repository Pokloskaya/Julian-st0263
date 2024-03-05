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
    dataBase[request.credentials] = ''
    print("Peer " + request.credentials + " connected.")

    return Service_pb2.OperationResponse(serverResponse="Conection is established!")
    #HAY QUE PONER LOS FILES DEL PEER EN EL SERVIDOR CENTRAL
  
  def logout(self, request, context):
    if request in dataBase:
      del dataBase[request]
      print("Peer (TENGO QUE PONER EL NOMBRE) disconnected.")

  def search(self, request, context):
    pass

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