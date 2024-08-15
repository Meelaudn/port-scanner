# port-scanner
# Nmap Python Script

This is a Python script that utilizes the `nmap` library to perform network scans. The script allows users to input a target IP and scan options, and then displays the results of the scan, including hostnames, states, protocols, and port statuses.

## Prerequisites

- **Python 3.x**: Make sure you have Python installed on your system.
- **Nmap**: This script requires the `nmap` command-line tool to be installed. You can install it using your package manager:
  ```bash
  # Ubuntu/Debian
  sudo apt-get install nmap

  # Fedora
  sudo dnf install nmap

  # macOS (using Homebrew)
  brew install nmap

## Example output

Enter the target IP: xxx.xxx.x.x
Enter the scan options: -p 1-100

Host: xxx.xxx.x.x (hostname)
State: up
Protocol: tcp
Port: 22   State: open
Port: 80   State: closed

