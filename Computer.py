import socket
import os

so = socket.socket()
port = 8080
host = "DESKTOP-MOA9M48"

so.connect((host, port))

print("Finished loading!")

while 1:
    command = so.recv(1024)
    command = command.decode()
    print("Recieved!")
    if command == "download_file":
        filepath = so.recv(5000)
        filepath = filepath.decode()
        file = open(filepath, "rb")
        data = file.read()
        so.send(data)
        print("Sent")

    elif command == "delete_file":
        file = so.recv(6000)
        file = file.decode()
        os.remove(file)
        print("Sent")

    else:
        print("Not a command.")