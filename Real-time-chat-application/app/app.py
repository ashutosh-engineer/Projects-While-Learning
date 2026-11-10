#Fast API is ASGI application
#ASGI stands for Aynchronous webserver GatewayInterface
# FastAPI is Built on Starlette
#Starlette provide routing , excption andling , middlewares,Background tasks
#FAst APi specially supports async/await

# FastAPi aditionally provide pydantic validation , type-based schemas, automatic docs,recos

#Flask Gunicorn in production
#Fast Uvicorn ->ASGI-> starlette -> FastAPI


from fastapi import FastAPI , status

app=FastAPI()

@app.get("/", status_code=status.HTTP_200_OK)
def server_running():
    return {"message" : "Server is running"}

@app.get("/health", status_code=status.HTTP_200_OK)
def health_status():
    return {
        "ok": True,
        "message" : "Healthy"
    }






