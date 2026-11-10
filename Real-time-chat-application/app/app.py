#Fast API is ASGI application
#ASGI stands for Aynchronous webserver GatewayInterface
# FastAPI is Built on Starlette
#Starlette provide routing , excption andling , middlewares,Background tasks
#FAst APi specially supports async/await

# FastAPi aditionally provide pydantic validation , type-based schemas, automatic docs,recos

#Flask Gunicorn in production
#Fast Uvicorn ->ASGI-> starlette -> FastAPI


from fastapi import FastAPI , status
from pydantic import BaseModel
from fastapi import Depends

app=FastAPI()

class Chatmessage(BaseModel):
    sender: str
    message: str
    room_id:int 

def common_parameteres(page: int = 1, limit:int =10):
    return {
        "page" : page,
        "limit":limit
    }

@app.get("/message" ,
        status_code=status.HTTP_200_OK,
        summary="For testing FastAPI dependency Injection")
def dependency_injection(parameteres : dict = Depends(common_parameteres)):
    return {
        "paramteres" : parameteres,
        "message" : "Dependency"
    }

@app.post("/messages" , status_code=status.HTTP_200_OK , summary="Created an route for sending chat details")
def messages(chat : Chatmessage):
    return {
        "sender" : chat.sender,
        "message" : chat.message,
        "room_id" : chat.room_id
    }

@app.get("/", status_code=status.HTTP_200_OK)
def server_running():
    return {"message" : "Server is running"}

@app.get("/health", status_code=status.HTTP_200_OK)
def health_status():
    return {
        "ok": True,
        "message" : "Healthy"
    }






