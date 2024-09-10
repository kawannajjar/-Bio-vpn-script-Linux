# -Bio-vpn-script-Linux
A Python script to automate VPN connections on Linux using OpenConnect. The script reads a list of servers from a text file, allows the user to select a server, and connects to it via OpenConnect.
# Bio-vpn-script-Linux

A Python script that reads a list of servers from a text file and allows the user to select a server to connect using `openconnect` on a Linux system.

## Features

- Reads server list from a `server.txt` file.
- Prompts the user to select a server by number.
- Uses `openconnect` to connect to the selected server.
- Designed to run on Linux with `bash` and `openconnect`.

## Prerequisites

Ensure the following are installed on your Linux system:

- Python 3.x
- `openconnect`
- `sudo` privileges

To install `openconnect`, run:

```bash
sudo apt-get install openconnect
