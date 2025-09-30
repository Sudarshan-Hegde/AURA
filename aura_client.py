#!/usr/bin/env python3
"""
AURA Client - Armed-forces Unified Relay Application
Client component for sending and receiving messages
"""

import socket
import threading
import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class AURAClient:
    def __init__(self, host='localhost', port=8888):
        self.host = host
        self.port = port
        self.socket = None
        self.running = False
        
    def connect(self):
        """Connect to the relay server"""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((self.host, self.port))
            logging.info(f"Connected to AURA server at {self.host}:{self.port}")
            self.running = True
            return True
        except Exception as e:
            logging.error(f"Failed to connect: {e}")
            return False
    
    def receive_messages(self):
        """Receive messages from the server"""
        while self.running:
            try:
                data = self.socket.recv(4096)
                if not data:
                    break
                message = data.decode('utf-8')
                print(f"\n[RECEIVED] {message}")
                print("> ", end="", flush=True)
            except Exception as e:
                if self.running:
                    logging.error(f"Error receiving message: {e}")
                break
        
    def send_message(self, message):
        """Send message to the server"""
        try:
            self.socket.send(message.encode('utf-8'))
            return True
        except Exception as e:
            logging.error(f"Error sending message: {e}")
            return False
    
    def disconnect(self):
        """Disconnect from the server"""
        self.running = False
        if self.socket:
            self.socket.close()
        logging.info("Disconnected from server")

def main():
    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        host = 'localhost'
    
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
    else:
        port = 8888
    
    client = AURAClient(host, port)
    
    if not client.connect():
        return
    
    # Start receiving thread
    receive_thread = threading.Thread(target=client.receive_messages)
    receive_thread.daemon = True
    receive_thread.start()
    
    print("AURA Client - Type your messages and press Enter to send")
    print("Type 'quit' to exit")
    
    try:
        while client.running:
            message = input("> ")
            if message.lower() == 'quit':
                break
            if message:
                client.send_message(message)
    except KeyboardInterrupt:
        print("\nInterrupted")
    finally:
        client.disconnect()

if __name__ == '__main__':
    main()
