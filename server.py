import socket
import threading

def handle_tcp_client(client_socket):
    request = client_socket.recv(1024)
    print(f"[TCP] Received: {request.decode()}")
    client_socket.send("ACK from TCP Server".encode())
    client_socket.close()

def tcp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5000))
    server.listen(5)  

    print("[TCP] Server is listening...")
    
    while True:
        client, addr = server.accept()
        print(f"[TCP] Accepted connection from: {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_tcp_client, args=(client,))
        client_handler.start()

def handle_udp_client(data, addr, server_socket):
    print(f"[UDP] Received: {data.decode()} from {addr}")
    server_socket.sendto("ACK from UDP Server".encode(), addr)

def udp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("0.0.0.0", 5001))
    
    print("[UDP] Server is listening...")

    while True:
        data, addr = server.recvfrom(1024)
        client_handler = threading.Thread(target=handle_udp_client, args=(data, addr, server))
        client_handler.start()

def main():
    tcp_server_thread = threading.Thread(target=tcp_server)
    udp_server_thread = threading.Thread(target=udp_server)

    tcp_server_thread.start()
    udp_server_thread.start()

    tcp_server_thread.join()
    udp_server_thread.join()

if __name__ == "__main__":
    main()
