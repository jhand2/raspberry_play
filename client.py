import bluetooth as bt

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
addr = "localhost"
# services = bt.find_service(name=None, uuid=None, address=addr)


# print(str(services))

sock = bt.BluetoothSocket(bt.RFCOMM)
sock.connect((addr, 1))
