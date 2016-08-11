import bluetooth as bt

socket = bt.BluetoothSocket(bt.RFCOMM)

host = "localhost"
socket.bind((host, bt.PORT_ANY))
port = socket.getsockname()[1]
print("port: " + str(port))
socket.listen(1)

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
# bt.advertise_service(socket, "BTServer", uuid)

print("Listening on " + host + ":" + str(port))

client_sock, addr = socket.accept()
print("Connection accepted from " + addr)

data = client_sock.recv(1024)
print(data)

client_sock.close()
socket.close()
