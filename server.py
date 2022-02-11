from concurrent import futures

import grpc
import sample_pb2, sample_pb2_grpc

store = {}

class Servicer(sample_pb2_grpc.SampleRPCServicer):
    def Save(self, request, context):
        store[request.id] = request.message
        return sample_pb2.SaveRes(
            success=True,
            id=request.id,
            message=store[request.id],
        )

    def Get(self, request, context):
        if request.id not in store:
            context.abort(grpc.StatusCode.NOT_FOUND, "Not found")
        return sample_pb2.GetRes(
            id=request.id,
            message=store[request.id],
        )


server = grpc.server(futures.ThreadPoolExecutor(1))
sample_pb2_grpc.add_SampleRPCServicer_to_server(Servicer(), server)
server.add_insecure_port("[::]:50051")
server.start()
server.wait_for_termination()

