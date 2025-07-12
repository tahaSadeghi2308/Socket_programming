import socket

server_ip = input('Enter the ip of server: ')
cli = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
cli.connect((server_ip , 4225))

while True:
    msg = input("message: ")
    if msg == "e": break
    cli.send(msg.encode("UTF-8"))
    res = cli.recv(2048).decode("UTF-8")
    print(f"Response {res}")

cli.close()

