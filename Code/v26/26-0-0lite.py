import socket
import time

def setup():
    global menu
    print(f"Welcome to CryptChat {version}")
    return askname()

def askname():
    global menu, username
    username = input("What is your name? ")
    return connect()

def connect():
    global menu, serverip, serverport
    serverip = input("What is the ip of your server? ")
    serverport = input("What is the port of your server? ")
    if serverip and serverport:
        return connecttoserver()
    else:
        print("Invalid IP or Port")
        time.sleep(1)
        return connect()

def connecttoserver():
    global menu
    menu = "chat"
    try:
        socket.create_connection(serverip, timeout=10)
        return main()
    except OSError:
        print("Failed to connect to ", serverip)
        time.sleep(1)
        return connect()

def chat():
    global menu
    pass

def main():
    running = True
    while running:
        if menu == "setup":
            setup()
        elif menu == "chat":
            chat()

def load():
    global version, username, serverip, serverport

    version = "26.0.0 LITE"
    username = ""
    serverip = ""
    serverport = ""
    return setup()

load()
