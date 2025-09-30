#!/usr/bin/env python3
"""
AURA Server - Armed-forces Unified Relay Application
Server component for message relay
"""

import socket
import threading
import json
import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class AURAServer:
    def __init__(self, host='0.0.0.0', port=8888):
        self.host = host
        self.port = port
        self.clients = []
        self.lock = threading.Lock()
        self.running = False
        
    def start(self):
        """Start the relay server"""
        self.running = True
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        
        logging.info(f"AURA Server started on {self.host}:{self.port}")
        
        try:
            while self.running:
                try:
                    server_socket.settimeout(1.0)
                    client_socket, address = server_socket.accept()
                    logging.info(f"New connection from {address}")
                    
                    client_thread = threading.Thread(
                        target=self.handle_client,
                        args=(client_socket, address)
                    )
                    client_thread.daemon = True
                    client_thread.start()
                except socket.timeout:
                    continue
                except Exception as e:
                    if self.running:
                        logging.error(f"Error accepting connection: {e}")
        finally:
            server_socket.close()
            logging.info("Server stopped")
    
    def handle_client(self, client_socket, address):
        """Handle individual client connection"""
        client_info = {
            'socket': client_socket,
            'address': address,
            'joined': datetime.now().isoformat()
        }
        
        with self.lock:
            self.clients.append(client_info)
        
        try:
            while self.running:
                data = client_socket.recv(4096)
                if not data:
                    break
                
                message = data.decode('utf-8')
                logging.info(f"Received from {address}: {message}")
                
                # Relay message to all other clients
                self.relay_message(message, client_socket)
        except Exception as e:
            logging.error(f"Error handling client {address}: {e}")
        finally:
            with self.lock:
                self.clients = [c for c in self.clients if c['socket'] != client_socket]
            client_socket.close()
            logging.info(f"Client {address} disconnected")
    
    def relay_message(self, message, sender_socket):
        """Relay message to all connected clients except sender"""
        with self.lock:
            for client in self.clients:
                if client['socket'] != sender_socket:
                    try:
                        client['socket'].send(message.encode('utf-8'))
                    except Exception as e:
                        logging.error(f"Error sending to {client['address']}: {e}")
    
    def stop(self):
        """Stop the server"""
        self.running = False

def main():
    server = AURAServer()
    try:
        server.start()
    except KeyboardInterrupt:
        logging.info("Shutting down server...")
        server.stop()

if __name__ == '__main__':
    main()
