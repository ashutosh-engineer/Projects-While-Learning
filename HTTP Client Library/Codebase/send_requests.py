import socket
import ssl
from urllib.parse import urlsplit


class SendRequest:

    def choose_request(self, request: str, url: str) -> str:
        match request.upper():
            case "GET":
                return "SENDING GET REQUEST"
            case "POST":
                return "SENDING POST REQUEST"
            case "PUT":
                return "SENDING PUT REQUEST"
            case "DELETE":
                return "SENDING DELETE REQUEST"
            case _:
                return "YOU SHOULD CHOOSE SOMETHING"

    def open_connection(self, url: str) -> socket.socket:
        if not url:
            raise ValueError("URL cannot be empty")

        parsed_url = urlsplit(url)

        if parsed_url.scheme not in ("http", "https"):
            raise ValueError("Only HTTP and HTTPS URLs are supported")

        hostname = parsed_url.hostname

        if hostname is None:
            raise ValueError("Hostname is missing")

        if parsed_url.port is not None:
            port = parsed_url.port
        elif parsed_url.scheme == "https":
            port = 443
        else:
            port = 80

        connection = socket.create_connection((hostname, port), timeout=10)

        if parsed_url.scheme == "https":
            context = ssl.create_default_context()
            connection = context.wrap_socket(
                connection,
                server_hostname=hostname,
            )

        return connection

    def receive_response(self, connection: socket.socket) -> bytes:
        response_parts = []

        try:
            while True:
                data = connection.recv(4096)

                if not data:
                    break

                response_parts.append(data)
        except socket.timeout:
            print("Receiving timed out")

        return b"".join(response_parts)

    def close_connection(self, connection: socket.socket) -> None:
        connection.close()
