import socket
import threading
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345
def handle_client(client_socket, username):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(f"Mensaje recibido de {username}: {data}")
            broadcast(f"{username}: {data}", client_socket)
        except:
            break

    # Cuando el cliente se desconecta
    print(f"Cliente {username} desconectado.")
    client_socket.close()

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                clients.remove(client)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_IP, SERVER_PORT))
    server_socket.listen(5)
    print(f"Servidor escuchando en {SERVER_IP} port: {SERVER_PORT}")

    while True:
        client_socket, _ = server_socket.accept()
        username = client_socket.recv(1024).decode('utf-8')
        print(f"Cliente {username} conectado.")
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket, username))
        client_thread.start()

clients = []

if __name__ == "__main__":
    main()
