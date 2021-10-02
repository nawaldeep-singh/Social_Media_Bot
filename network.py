import socket
import cli_format as clif

def isConnected():
    print("Check for Connection",end="")
    clif.dot()
    IPaddress=socket.gethostbyname(socket.gethostname())
    if IPaddress=="127.0.0.1":
        print("No Internet Connection")
        return False
    else:
        print("Connected, with the IP address: "+ IPaddress)
        return True