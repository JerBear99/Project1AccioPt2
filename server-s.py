import socket
import signal
import sys
import time

def handle_signal(signum, frame):
    global not_stopped
    not_stopped = False

def main():
    if len(sys.argv) != 2:
        sys.stderr.write("ERROR: Invalid number of arguments\n")
        sys.exit(1)

    port = int(sys.argv[1])

    # Set up signal handlers
    signal.signal(signal.SIGQUIT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)
    signal.signal(signal.SIGINT, handle_signal)

    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        # Bind the socket to listen on all interfaces
        server_socket.bind(("0.0.0.0", port))

        # Listen for incoming connections (up to 10)
        server_socket.listen(10)

        print(f"Server is listening on port {port}")

        not_stopped = True
        while not_stopped:
            # Accept a connection
            client_socket, client_addr = server_socket.accept()
            print(f"Accepted connection from {client_addr}")

            # Send "accio\r\n" to the client
            client_socket.send(b"accio\r\n")

            # Receive data from the client
            total_bytes_received = 0
            start_time = time.time()
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                total_bytes_received += len(data)

                # Check for a timeout (10 seconds)
                if time.time() - start_time > 10:
                    sys.stderr.write("ERROR: Connection timed out\n")
                    break

            # Print the amount of data received
            print(f"Received {total_bytes_received} bytes from {client_addr}")

            # Close the client socket
            client_socket.close()

    except OSError as e:
        sys.stderr.write(f"ERROR: {e}\n")
        sys.exit(1)

    # Close the server socket
    server_socket.close()
    print("Server is shutting down")

if __name__ == "__main__":
    main()