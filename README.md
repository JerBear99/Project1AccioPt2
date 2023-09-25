# Project1AccioPt2
# Simple Python Server

This is a basic Python server application that listens on a specified port, accepts incoming connections, and responds to clients with the message "accio\r\n". The server is designed to gracefully handle termination signals and clean up resources when necessary.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Terminating the Server](#terminating-the-server)
- [Testing](#testing)
- [License](#license)

## Introduction

This Python server is a minimal implementation that demonstrates the following:

- Listening on a specified port for incoming connections.
- Responding with a fixed message to clients.
- Gracefully handling termination signals (SIGQUIT, SIGTERM, SIGINT).
- Closing client and server sockets appropriately.

It's a starting point for building more complex server applications.

## Features

- Listens on a specified port for incoming connections.
- Responds to clients with the message "accio\r\n".
- Gracefully handles termination signals for clean shutdown.

## Prerequisites

Before running the server, ensure you have the following prerequisites installed:

- Python 3.x

## Usage

To use the server, follow these steps:

1. Clone this repository to your local machine.

2. Open a terminal window and navigate to the project directory.

3. Run the server with the desired port number. Replace `<PORT>` with the port number you want to use:

   ```bash
   python3 server-s.py <PORT>

## Errors
Failed Tests
2. Server handles incorrect port (0/5)
3. Server gracefully handles SIGINT signal (0/5)
6. Server starts receiving data (0/5)
7. Server accepts another connection after the first connection finished (0/5)
8. When server receives 10 connections simultaneously, it accepts and process them sequentially without rejecting (0/5)
11. Server successfully receives a small amount of data (~500 bytes) using the instructor's version of the client (0/10)
12. Server prints the correct value for the received data from the previous test (0/10)
13. Server successfully receives a large amount of data (~10 MiBytes) using the instructor's version of the client (without emulated delays and/or transmission errors) (0/10)
14. Server prints the correct value for the received data from the previous test (0/10)
15. Server successfully receives a large amount of data (~10 MiBytes) using the instructor's version of the client (with emulated delays and/or transmission errors) (0/5)
16. Server prints the correct value for the received data from the previous test (0/5)