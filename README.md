# AURA
Armed-forces Unified Relay Application

## Overview
AURA (Armed-forces Unified Relay Application) is a secure messaging relay system designed for military communications. It provides real-time message relay capabilities between multiple clients through a central server.

## Features
- Real-time message relay between multiple clients
- Multi-threaded server supporting concurrent connections
- Simple and secure client-server architecture
- Configurable server and client parameters
- Logging for monitoring and auditing
- Easy to deploy and use

## Architecture
AURA consists of two main components:
1. **Server (`aura_server.py`)**: Relay server that manages connections and forwards messages
2. **Client (`aura_client.py`)**: Client application for sending and receiving messages

## Requirements
- Python 3.6 or higher
- No external dependencies (uses Python standard library)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Sudarshan-Hegde/AURA.git
   cd AURA
   ```

2. Make scripts executable (Linux/Mac):
   ```bash
   chmod +x aura_server.py aura_client.py
   ```

## Usage

### Starting the Server
Run the server on the default port (8888):
```bash
python3 aura_server.py
```

The server will start listening for client connections.

### Starting a Client
Connect to the server:
```bash
python3 aura_client.py [host] [port]
```

Examples:
```bash
# Connect to localhost on default port
python3 aura_client.py

# Connect to specific host and port
python3 aura_client.py 192.168.1.100 8888
```

### Sending Messages
Once connected, type your message and press Enter. The message will be relayed to all other connected clients.

To exit, type `quit` or press Ctrl+C.

## Configuration
Edit `config.json` to customize server and client settings:
- Server host and port
- Maximum connections
- Logging settings
- Security options

## Security Considerations
- Currently implements basic relay functionality
- For production use, consider adding:
  - Authentication and authorization
  - Message encryption (TLS/SSL)
  - Access control lists
  - Message validation and sanitization

## Testing
To test the application:

1. Start the server in one terminal:
   ```bash
   python3 aura_server.py
   ```

2. Start multiple clients in separate terminals:
   ```bash
   python3 aura_client.py
   ```

3. Send messages from any client and verify they appear on all other clients

## Example Session
**Terminal 1 (Server):**
```
$ python3 aura_server.py
2025-01-01 12:00:00 - INFO - AURA Server started on 0.0.0.0:8888
2025-01-01 12:00:05 - INFO - New connection from ('127.0.0.1', 54321)
2025-01-01 12:00:10 - INFO - New connection from ('127.0.0.1', 54322)
```

**Terminal 2 (Client 1):**
```
$ python3 aura_client.py
2025-01-01 12:00:05 - INFO - Connected to AURA server at localhost:8888
AURA Client - Type your messages and press Enter to send
Type 'quit' to exit
> Hello from Command Alpha
> 
[RECEIVED] Hello from Command Bravo
```

**Terminal 3 (Client 2):**
```
$ python3 aura_client.py
2025-01-01 12:00:10 - INFO - Connected to AURA server at localhost:8888
AURA Client - Type your messages and press Enter to send
Type 'quit' to exit
> 
[RECEIVED] Hello from Command Alpha
> Hello from Command Bravo
```

## License
This project is provided as-is for educational and operational purposes.

## Contributing
Contributions are welcome! Please ensure any changes maintain the security and reliability standards required for military applications.
