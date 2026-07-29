import socket
import threading
import time

clients = []
clients_lock = threading.Lock()

version = ""
servername = ""
serverip = ""
serverport = ""
menu = "setup"

def broadcast(message, sender_conn):
    """Send message to all clients except the sender."""
    with clients_lock:
        for client in clients:
            if client is not sender_conn:
                try:
                    client.sendall(message)
                except Exception:
                    # Client disconnected, will be cleaned up in handle_client
                    if client in clients:
                        clients.remove(client)
                    client.close()

def handle_client(conn, addr):
    """Handle individual client connections in a separate thread."""
    print(f"[NEW CONNECTION] {addr} connected to {servername}.")

    with clients_lock:
        clients.append(conn)
    
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            
            print(f"[{addr}] {data.decode('utf-8')}")
            
            # Broadcast to everyone ELSE
            broadcast(data, conn)
            
    except Exception as e:
        print(f"[ERROR] {addr}: {e}")
    finally:
        with clients_lock:
            if conn in clients:
                clients.remove(conn)
        conn.close()
        print(f"[DISCONNECTED] {addr} removed.")

def setup():
    print(f"Welcome to CryptChat {version}")
    return askname()

def askname():
    global servername
    servername = input("What is your server name? ")
    return host()

def host():
    global serverip, serverport
    serverip = input("What is the ip you want to host your server on? (e.g., 0.0.0.0) ")
    serverport_input = input("What is the port you want to host your server on? ")
    
    if serverip and serverport_input:
        try:
            serverport = int(serverport_input)
            return startserver()
        except ValueError:
            print("Invalid Port Number")
            time.sleep(1)
            return host()
    else:
        print("Invalid IP or Port")
        time.sleep(1)
        return host()

def startserver():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Allow quick restart of the server on the same port
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        server_socket.bind((serverip, serverport))
        server_socket.listen()
        print(f"[LISTENING] {servername} is running on {serverip}:{serverport}")
        print("Waiting for connections...")
        
        # Main server loop to accept connections
        while True:
            conn, addr = server_socket.accept()
            # Start a new thread for each client
            thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            thread.start()
            
    except OSError as e:
        print(f"Failed to host on {serverip}: {e}")
        time.sleep(1)
        return host()
    except KeyboardInterrupt:
        print("\n[SHUTDOWN] Server stopping.")
        server_socket.close()

def info():
    global menu
    print(f"Server: {servername} | IP: {serverip} | Port: {serverport}")
    print(f"Active Clients: {len(clients)}")

def main():
    running = True
    while running:
        if menu == "setup":
            setup()
        elif menu == "info":
            info()

def load():
    global version, servername, serverip, serverport, menu
    version = "26.0 SERVER"
    servername = ""
    serverip = ""
    serverport = ""
    menu = "setup"
    return main()

if __name__ == "__main__":
    load()   
