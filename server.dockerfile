FROM python:3
RUN pip3 install grpcio grpcio-tools protobuf grpclib googleapis-common-protos
COPY ./sample_pb2.py sample_pb2.py
COPY ./sample_pb2_grpc.py sample_pb2_grpc.py
COPY ./server.py server.py
RUN chmod +x server.py
EXPOSE 50051
CMD [ "python3", "./server.py" ]

