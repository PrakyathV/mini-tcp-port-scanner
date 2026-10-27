
import socket
import threading
import unittest

from scanner import scan_port


class TestScanPort(unittest.TestCase):
    def test_open_port(self):
        # Create a temporary TCP listener on an available local port.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind(("127.0.0.1", 0))
            server.listen(1)
            port = server.getsockname()[1]

            result = scan_port("127.0.0.1", port, 1.0)

        self.assertEqual(result, "OPEN")

    def test_closed_port(self):
        # Reserve an available port, then close it before scanning.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
            server.bind(("127.0.0.1", 0))
            port = server.getsockname()[1]

        result = scan_port("127.0.0.1", port, 1.0)

        self.assertEqual(result, "CLOSED")

    def test_invalid_hostname(self):
        result = scan_port("invalid host name !", 80, 0.5)

        self.assertEqual(result, "ERROR")


if __name__ == "__main__":
    unittest.main()

