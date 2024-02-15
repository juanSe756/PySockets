import socket
import threading

def receive_message(client_socket):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            print(data)
        except:
            break

def main():
    server_ip = input("Ingresa la dirección IP del servidor: ")
    server_port = int(input("Ingresa el puerto del servidor: "))
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    username = input("Ingresa tu nombre de usuario: ")
    client_socket.send(username.encode('utf-8'))
    receive_thread = threading.Thread(target=receive_message, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    main()
