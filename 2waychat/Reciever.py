import socket
import threading

# IP address and port of Raspberry Pi B
IP_ADDRESS_B = '0.0.0.0'  # Raspberry Pi B's IP address
PORT = 5000  # Replace with the desired port number

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to Raspberry Pi B's IP address and port
s.bind((IP_ADDRESS_B, PORT))

# Listen for incoming connections
s.listen(1)

print("Waiting for a connection...")

# Accept a connection from Raspberry Pi A
connection, address = s.accept()

print("Connected to:", address)

# Function to receive messages from Raspberry Pi A
def receive_messages():
    while True:
        data = connection.recv(1024).decode()
        print("Received:", data)

# Start a thread to receive messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Send messages until the user types "end connection"
while True:
    message = input("Enter a message (type 'end connection' to terminate): ")
    connection.sendall(message.encode())
    if message == "end connection":
        break

# Close the connection and socket
connection.close()
s.close()
