import socket
import signal
import sys
import time

server_socket = None  # Declare server_socket outside the try block

def handle_signal(signum, frame):
    global not_stopped
    not_stopped = False
    print("Received signal. Cleaning up...")
    if server_socket:
        server_socket.close()
    sys.exit(0)

def main():
    if len(sys.argv) != 2:
        sys.stderr.write("ERROR: Invalid number of arguments\n")
        sys.exit(1)

    try:
        port = int(sys.argv[1])
        if not (0 < port < 65536):
            raise ValueError("Port number out of range")

        signal.signal(signal.SIGQUIT, handle_signal)
        signal.signal(signal.SIGTERM, handle_signal)
        signal.signal(signal.SIGINT, handle_signal)

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        server_socket.bind(("0.0.0.0", port))
        server_socket.listen(10)

        print(f"Server is listening on port {port}")

        not_stopped = True
        while not_stopped:
            client_socket, client_addr = server_socket.accept()
            print(f"Accepted connection from {client_addr}")

            client_socket.send(b"accio\r\n")

            total_bytes_received = 0
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                total_bytes_received += len(data)

            print(f"Received {total_bytes_received} bytes from {client_addr}")

            client_socket.close()

    except OSError as e:
        sys.stderr.write(f"ERROR: {e}\n")
        sys.exit(1)

    finally:
        if server_socket:
            server_socket.close()

    print("Server is shutting down")

if __name__ == "__main__":
    main()
