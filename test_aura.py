#!/usr/bin/env python3
"""
Simple test script for AURA
Tests basic server-client connectivity
"""

import socket
import time
import threading
import sys

def test_connection(host='localhost', port=8888):
    """Test if we can connect to the server"""
    print(f"Testing connection to {host}:{port}...")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((host, port))
        print("✓ Connection successful")
        sock.close()
        return True
    except Exception as e:
        print(f"✗ Connection failed: {e}")
        return False

def test_message_send(host='localhost', port=8888):
    """Test sending a message"""
    print(f"\nTesting message send to {host}:{port}...")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((host, port))
        
        test_message = "Test message from AURA test script"
        sock.send(test_message.encode('utf-8'))
        print(f"✓ Message sent: {test_message}")
        
        sock.close()
        return True
    except Exception as e:
        print(f"✗ Message send failed: {e}")
        return False

def main():
    print("=" * 50)
    print("AURA Test Script")
    print("=" * 50)
    
    if len(sys.argv) > 1:
        host = sys.argv[1]
    else:
        host = 'localhost'
    
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
    else:
        port = 8888
    
    # Run tests
    tests_passed = 0
    total_tests = 2
    
    if test_connection(host, port):
        tests_passed += 1
    
    time.sleep(1)
    
    if test_message_send(host, port):
        tests_passed += 1
    
    print("\n" + "=" * 50)
    print(f"Tests completed: {tests_passed}/{total_tests} passed")
    print("=" * 50)
    
    return 0 if tests_passed == total_tests else 1

if __name__ == '__main__':
    sys.exit(main())
