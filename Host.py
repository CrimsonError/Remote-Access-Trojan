import socket

so = socket.socket()
port = 8080
host = socket.gethostname()
so.bind((host, port))

print("Server running at ", host)

so.listen(1)
connection, address, = so.accept()
print(address, " has been connected")

while 1:
    command = input("Command: ")
    if command == "download_file":
        connection.send(command.encode())
        filepath = input("Please enter the file path including the filename: ")
        connection.send(filepath.encode())
        file = connection.recv(100000)
        filename = input("Please enter the file name for the new file: ")
        newfile = open(filename, "wb")
        newfile.write(file)
        newfile.close()
        print(filename, " Has been downloaded and saved ")

    elif command == "delete_file":
        connection.send(command.encode())
        file = input("Please enter the file and directory: ")
        connection.send(file.encode())
        print("Successfully executed.")

    else:
        print("That command does not exist!")