# Mini TCP Port Scanner

A lightweight TCP port scanner built with Python to explore network connectivity, socket programming, and basic network reconnaissance.

## Features

- Scan a user-defined TCP port range.
- Identify open TCP ports.
- Display common service labels.
- Report open, closed, no-response, and error counts.
- Configure connection timeouts.
- Validate port ranges and command-line arguments.
- Includes automated unit tests using Python's built-in `unittest`.

## Requirements

- Python 3.10 or newer
- Linux, macOS, or another supported Python environment
- No third-party Python packages required

## Usage

Scan the first 1,024 TCP ports on your own machine:

```bash
python scanner.py 127.0.0.1 --start 1 --end 1024
```

Scan a small local port range:

```bash
python scanner.py 127.0.0.1 --start 7998 --end 8002 --timeout 0.5
```

Scan a system you own or are explicitly authorized to test:

```bash
python scanner.py <authorized-host> --start 1 --end 1024
```

Replace `<authorized-host>` with the authorized target's IP address or hostname.

## Example Output

```text
Target: 127.0.0.1
Scanning TCP ports 7998-8002...

[OPEN] Port 8000  Service: HTTP

--- Scan Summary ---
Ports scanned: 5
Open:          1
Closed:        4
No response:   0
Errors:        0
```

Results vary depending on the target, network conditions, and active services.

## Run the Tests

```bash
python -m unittest discover -s tests -v
```

The test suite checks open-port detection, closed-port detection, and error handling.

## Project Structure

```text
day02-mini-port-scanner/
├── scanner.py
├── tests/
│   └── test_scanner.py
├── .gitignore
└── README.md
```

## Limitations

- This tool checks TCP connectivity; it does not scan UDP ports.
- Service names are common port associations, not verified application identities.
- A timeout does not conclusively prove that a port is filtered.
- The scanner uses sequential connections and is intended for learning and small scans.

## Responsible Use

Use this tool only on systems you own or have explicit authorization to test. Follow applicable laws and network policies.

## Learning Objectives

- Python socket programming
- TCP connection behavior
- Port scanning fundamentals
- Error handling and timeouts
- Automated testing
- Git and GitHub workflow


