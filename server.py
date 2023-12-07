import grpc
from concurrent import futures
import hello_pb2
import hello_pb2_grpc

# Define the HelloServicer
class HelloServicer(hello_pb2_grpc.HelloServicer):
    def SayHello(self, request, context):
        return hello_pb2.HelloResponse(message=f"Hello, {request.name}!")

def serve():
    # Create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    # Add the HelloServicer to the server
    hello_pb2_grpc.add_HelloServicer_to_server(HelloServicer(), server)

    # Bind the server to a specific port
    server.add_insecure_port('[::]:50051')

    print("Server started. Listening on port 50051...")
    # Start the server
    server.start()

    # Keep the server alive
    try:
        while True:
            pass
    except KeyboardInterrupt:
        # Stop the server on keyboard interrupt
        server.stop(0)
        print("Server stopped.")

if __name__ == '__main__':
    serve()
