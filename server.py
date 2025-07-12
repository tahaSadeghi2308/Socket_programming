import socket 
import threading
import os


server = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server.bind(('0.0.0.0' , 4225))
server.listen(5)

os.system("clear")
print("Start Listening ......")


def user_handler(cli , addr) -> None:
    print(f"connection for {addr} is comming !!!")
    while True:
        try:
            data = cli.recv(2048).decode('UTF-8')
            if not data: break
        
            print(f"recived data is {data}")
            res = f"Seyyed Recived {data}"
            cli.send(res.encode("UTF-8"))
        except Exception as e:
            break
    cli.close()

while True:
    cli , addr = server.accept()
    t = threading.Thread(target=user_handler , args=(cli , addr))
    t.start()

