
#!/usr/bin/env python3

import argparse
import errno
import socket
from collections import Counter
from datetime import datetime

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    5432: "PostgreSQL",
    8000: "HTTP",
    8080: "HTTP-Proxy",
}


def scan_port(host, port, timeout):
    """Return OPEN, CLOSED, NO RESPONSE, or ERROR."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))

            if result == 0:
                return "OPEN"
            if result == errno.ECONNREFUSED:
                return "CLOSED"
            if result == errno.ETIMEDOUT:
                return "NO RESPONSE"

            return "NO RESPONSE"

    except (socket.timeout, TimeoutError):
        return "NO RESPONSE"
    except OSError:
        return "ERROR"


def scan_ports(host, start_port, end_port, timeout):
    """Scan TCP ports and summarize their connection results."""
    results = Counter()
    open_ports = []

    print(f"\nTarget: {host}")
    print(f"Scan started: {datetime.now():%Y-%m-%d %H:%M:%S}")
    print(f"Scanning TCP ports {start_port}-{end_port}...\n")

    for port in range(start_port, end_port + 1):
        status = scan_port(host, port, timeout)
        results[status] += 1

        if status == "OPEN":
            service = COMMON_PORTS.get(port, "Unknown")
            open_ports.append((port, service))
            print(f"[OPEN] Port {port:<5} Service: {service}")

    print("\n--- Scan Summary ---")
    print(f"Ports scanned: {sum(results.values())}")
    print(f"Open:          {results['OPEN']}")
    print(f"Closed:        {results['CLOSED']}")
    print(f"No response:   {results['NO RESPONSE']}")
    print(f"Errors:        {results['ERROR']}")

    return open_ports


def main():
    parser = argparse.ArgumentParser(
        description="Mini TCP Port Scanner for authorized systems."
    )
    parser.add_argument("host", help="Target IP address or hostname")
    parser.add_argument("--start", type=int, default=1,
                        help="First port (default: 1)")
    parser.add_argument("--end", type=int, default=1024,
                        help="Last port (default: 1024)")
    parser.add_argument("--timeout", type=float, default=0.5,
                        help="Timeout per port in seconds")

    args = parser.parse_args()

    if not 1 <= args.start <= 65535:
        parser.error("--start must be between 1 and 65535")

    if not 1 <= args.end <= 65535:
        parser.error("--end must be between 1 and 65535")

    if args.start > args.end:
        parser.error("--start cannot be greater than --end")

    if args.end - args.start > 4095:
        parser.error("Maximum range is 4096 ports per scan")

    if args.timeout <= 0:
        parser.error("--timeout must be greater than zero")

    scan_ports(args.host, args.start, args.end, args.timeout)


if __name__ == "__main__":
    main()

