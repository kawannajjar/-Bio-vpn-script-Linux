# Bio-vpn-scrip-Linux

A Python script that reads a list of servers from a text file and allows the user to select a server to connect using `openconnect` on a Linux system.

## Features

- Reads server list from a `server.txt` file.
- Prompts the user to select a server by number.
- Uses `openconnect` to connect to the selected server.

## Prerequisites

Ensure the following are installed on your Linux system:

- Python 3.x
- `openconnect`
- `sudo` privileges

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/USERNAME/Bio-vpn-scrip-Linux.git
   cd Bio-vpn-scrip-Linux
2 .Create a server.txt file in the root directory with your server addresses, one per line.
Example:
vpn1.example.com
vpn2.example.com
vpn3.example.com

## Usage
1.Run the script with Python:
      ```bash
      python3 vpn_connect.py

## Testing

To run the tests, use the following command:

      ```bash
      pytest


## Supported Versions

This project supports the following versions:
- Python 3.9
- Docker 20.10





