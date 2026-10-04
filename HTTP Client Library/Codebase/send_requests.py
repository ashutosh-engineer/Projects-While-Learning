import socket
import ssl
from urllib.parse import urlsplit

class Send_request:

    def choose_request(self, request: str, url: str):
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
                return "YOU SHOULD CHOOSED SOMETHING"

    def Open_connection(self , url:str) -> socket.socket:
        if url == "":
            raise ValueError("Parse the URL please")

        parsed_url = urlsplit(url)
        if parsed_url.port is not None:
            port=parsed_url.port
        elif parsed_url.scheme == "https":
            port=443 
            # In case of https
        else:
            port=80
            #In case of http

        hostnames : str= parsed_url.hostname 
        # This will give me Domain name

        if hostnames is None:
            raise ValueError("Hostname is missing ")
        else:
            print("Host name found")

        connection = socket.create_connection((hostnames, port) , timeout=10)
        print("Connection Initialised")


        return connection
     

        

        