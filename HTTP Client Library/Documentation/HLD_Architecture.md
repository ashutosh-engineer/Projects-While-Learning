# High-Level Design (HLD)

This project is a simple HTTP client library built in Python to understand how client-server communication works at the network level. The system is designed in a modular way so that each part performs a specific task clearly and efficiently.

The main purpose of the project is to allow a user to register, log in, choose an HTTP method, send a request to a URL, and view the server response. It also stores request and activity logs in files for each user.

The architecture contains four major components: the user interface, authentication module, request handling module, and file logging module. The user interface handles all terminal-based input and output. The authentication module checks registration and login details using a dictionary for user storage. The request handling module creates HTTP requests, opens a socket connection, sends the request, and receives the response. The file logging module stores each user’s activity and request history in personal files.

The networking layer is the core of the project. It opens a TCP connection using sockets, sends the HTTP request, and receives the server response. This part is kept low-level so the project can demonstrate how HTTP communication works without hiding the details behind advanced libraries.

The main flow of the system is straightforward. First, the user registers or logs in. Next, the user selects an HTTP method and enters a URL. Then the request is sent to the server, the response is displayed, and the result is saved in the user’s log file. The entire system is controlled by the main module, which connects all the components together.

This design is simple, easy to understand, and suitable for a learning project. It follows the LLD closely while focusing on the overall structure, responsibilities, and flow of the system.
