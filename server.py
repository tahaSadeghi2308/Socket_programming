import socket

server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

server.bind(("localhost" , 4225))

server.listen(1)


