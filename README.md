# Project1AccioPt2
# Simple Python Server
This is a simple Python server application that listens on a specified port and responds to incoming connections. The server sends the message "accio\r\n" to connected clients and counts the amount of data received from them. It also handles termination signals (SIGQUIT, SIGTERM, SIGINT) and timeouts.

## Usage

To run the server, use the following command:

```bash
python3 server-s.py <PORT>
