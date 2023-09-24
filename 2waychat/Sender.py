import socket
import threading

# IP address and port of Raspberry Pi B
IP_ADDRESS_B = '192.168.1.120'  # Replace with Raspberry Pi B's IP address
PORT = 5000  # Replace with the desired port number

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server (Raspberry Pi B)
s.connect((IP_ADDRESS_B, PORT))

# Function to receive messages from Raspberry Pi B
def receive_messages():
    while True:
        data = s.recv(1024).decode()
        print("Received:", data)

# Start a thread to receive messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Send messages until the user types "end connection"
while True:
    message = input("Enter a message (type 'end connection' to terminate): ")
    s.sendall(message.encode())
    if message == "end connection":
        break

# Close the socket
s.close()
