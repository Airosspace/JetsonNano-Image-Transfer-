import socket
import struct

# Server configuration
HOST = '127.0.0.1'  # Server IP address
PORT = 1234        # Server port number

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)

print('Server is listening on {}:{}'.format(HOST, PORT))

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print('Connected to client:', client_address)

    # Receive the filename from the client
    filename_length = struct.unpack('!I', client_socket.recv(4))[0]
    filename = client_socket.recv(filename_length).decode()
    print('Received filename:', filename)

    # Receive the image size from the client
    image_size = struct.unpack('!Q', client_socket.recv(8))[0]
    print('Received image size:', image_size)

    # Receive the image data from the client
    image_data = b''
    while len(image_data) < image_size:
        remaining = image_size - len(image_data)
        image_data += client_socket.recv(min(4096, remaining))

    # Save the image file
    with open(f"r/{filename}", 'wb') as file:
        file.write(image_data)
        print('Image file saved:', filename)

    # Close the client connection
    client_socket.close()
