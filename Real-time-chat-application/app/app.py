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

app=FastAPI()

class Chatmessage(BaseModel):
    sender: str
    message: str
    room_id:int 

@app.post("/messages" , status_code=status.HTTP_200_OK)
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






