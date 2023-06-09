import socket
import struct

# Server configuration
HOST = '127.0.0.1'  # Server IP address
PORT = 1234        # Server port number

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Send the filename to the server
filename = 'h.jpg'  # Replace with the actual filename
filename_length = len(filename)
client_socket.send(struct.pack('!I', filename_length))
client_socket.send(filename.encode())

# Read the image file and send its data to the server
with open(filename, 'rb') as file:
    image_data = file.read()
    image_size = len(image_data)
    client_socket.send(struct.pack('!Q', image_size))
    client_socket.sendall(image_data)

print('Image sent successfully.')

# Close the client connection
client_socket.close()

