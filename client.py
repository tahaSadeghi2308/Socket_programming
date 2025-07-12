import socket


cli = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
cli.connect(("ip of server" , 4225))

while True:
    msg = input("message: ")
    if msg == "e": break
    cli.send(msg.encode("UTF-8"))
    res = cli.recv(2048).decode("UTF-8")
    print(f"Response {res}")

cli.close()

