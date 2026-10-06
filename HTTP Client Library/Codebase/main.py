from Authentication import login , Authenticate
from send_requests import SendRequest


print("Kindly Register user")
name= input("Enter Your name")
password= int(input("Enter Your password"))
if Authenticate.register_user(name, password) == True:
    print("Kindly login to continue")
    login.logined(name , password)

print("Send Request MEthod is active")
Connection=SendRequest.open_connection("https://www.google.com")
Connection.receive_response()
Connection.close()

      