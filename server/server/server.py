from concurrent import futures

import grpc
import Service_pb2 
import Service_pb2_grpc

import bootstrap

HOST = bootstrap.localhost


#Base de datos de los peers
dataBase = {}

class functions(Service_pb2_grpc.MainFunctionsServicer):
   
  def login(self, request, context):
    #print("Request is received: " + str(request))
    dataBase[request.peerName] = request.fileName
    print("Peer with name: " + request.peerName + " connected.")
    print("Data base: " + str(dataBase))

    return Service_pb2.OperationResponse(serverResponse="Conection is established!")
  
  def logout(self, request, context):
    print("Request is received: " + str(request))
    if request.peerName in dataBase:
      del dataBase[request.peerName]
      print("Peer " + request.peerName + " disconnected.")

    return Service_pb2.OperationResponse(serverResponse="Peer disconnected!")

  def search(self, request, context):
    print("Searching for file:", request.peerName)
    
    # Iterate through each peer in the database
    for peer, files in dataBase.items():
        # Check if the requested file is in the list of files for the current peer
        if request.peerName in files:
            # File found, return the peer's credentials
            return Service_pb2.OperationResponse(serverResponse=f"File '{request.peerName}' found. Owner: {peer}")
    
    # File not found for any peer
    return Service_pb2.OperationResponse(serverResponse=f"File '{request.peerName}' not found.")


  def index(self, request, context):
    print("Request is received: " + str(request))
 
def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  Service_pb2_grpc.add_MainFunctionsServicer_to_server(functions(), server)
  server.add_insecure_port(HOST)
  print("Service is running... ")
  server.start()

  server.wait_for_termination()


if __name__ == "__main__":
  serve()