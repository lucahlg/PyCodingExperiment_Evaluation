import io

class MeteredFile(io.BufferedRandom):
    """Implement using a subclassing model."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._read_bytes = 0
        self._write_bytes = 0
        self._read_ops = 0
        self._write_ops = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def read(self, size=-1):
        data = super().read(size)
        self._read_bytes += len(data)
        self._read_ops += 1
        return data

    @property
    def read_bytes(self):
        return self._read_bytes

    @property
    def read_ops(self):
        return self._read_ops

    def write(self, b):
        super().write(b)
        self._write_bytes += len(b)
        self._write_ops += 1

    @property
    def write_bytes(self):
        return self._write_bytes

    @property
    def write_ops(self):
        return self._write_ops

import socket

class MeteredSocket:
    """Implement using a delegation model."""
    
    def __init__(self, sock):
        self.sock = sock
        self._recv_bytes = 0
        self._send_bytes = 0
        self._recv_ops = 0
        self._send_ops = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()

    def recv(self, bufsize, flags=0):
        data = self.sock.recv(bufsize, flags)
        self._recv_bytes += len(data)
        self._recv_ops += 1
        return data

    @property
    def recv_bytes(self):
        return self._recv_bytes

    @property
    def recv_ops(self):
        return self._recv_ops

    def send(self, data, flags=0):
        sent_bytes = self.sock.send(data, flags)
        self._send_bytes += sent_bytes
        self._send_ops += 1
        return sent_bytes

    @property
    def send_bytes(self):
        return self._send_bytes

    @property
    def send_ops(self):
        return self._send_ops


# Beispiel für die Verwendung von MeteredSocket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('en.wikipedia.org', 80))

with MeteredSocket(sock) as metered_socket:
    metered_socket.send(b'GET /wiki/Platform_as_a_service / HTTP/1.1\r\nHost: en.wikipedia.org\r\nConnection: close\r\n\r\n')
    response = metered_socket.recv(4096)
    print(f'Bytes sent: {metered_socket.send_bytes}')
    print(f'Send operations: {metered_socket.send_ops}')
    print(f'Bytes received: {metered_socket.recv_bytes}')
    print(f'Receive operations: {metered_socket.recv_ops}')
