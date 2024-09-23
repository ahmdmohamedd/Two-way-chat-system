TCP Two-Way Chat System

This repository contains a simple two-way chat system implemented using TCP (Transmission Control Protocol). The system consists of a server and multiple clients that can exchange messages in real-time. The chat system demonstrates the basics of socket programming in Python.

## Features

- Two-way communication between the server and multiple clients.
- Supports real-time message exchange.
- Simple and lightweight implementation using Python's `socket` library.

## Technologies Used

- Python 3.x
- Socket Programming (TCP)

## How It Works

The system operates using the TCP protocol to establish a connection between the server and clients. 

1. **TCP Server**: The server listens for incoming connections on a specific IP address and port. Once a client connects, the server can send and receive messages.
2. **TCP Client**: The client connects to the server using the server's IP address and port. After connecting, both the client and server can send and receive messages.
3. **Two-Way Communication**: Messages can be sent from the client to the server and from the server to the client, facilitating real-time chat.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ahmdmohamedd/Two-way-chat-system.git
    cd Two-way-chat-system
    ```

## Usage

1. **Start the Server**:
    The server will listen for incoming client connections.

    ```bash
    python Receiver.py
    ```

2. **Run the Client**:
    Multiple clients can connect to the server by specifying the server's IP address and port.

    ```bash
    python Sender.py
    ```

### Example

1. **Server-side:**

    ```bash
    Server started. Waiting for connection...
    Client connected from ('127.0.0.1', 50578)
    ```

2. **Client-side:**

    ```bash
    Connected to the server.
    Enter your message: Hello from client!
    ```

## File Structure

```bash
tcp-chat-system/
│
├── Receiver.py         # The TCP server script
├── Sender.py         # The TCP client script
├── README.md         # Project documentation
```

## How to Contribute

Contributions are welcome! If you'd like to contribute to this project:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit the changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a Pull Request.
