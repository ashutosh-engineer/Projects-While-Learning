#Fast API is ASGI application
#ASGI stands for Aynchronous webserver GatewayInterface
# FastAPI is Built on Starlette
#Starlette provide routing , excption andling , middlewares,Background tasks
#FAst APi specially supports async/await

# FastAPi aditionally provide pydantic validation , type-based schemas, automatic docs,recos

#Flask Gunicorn in production
#Fast Uvicorn ->ASGI-> starlette -> FastAPI


from fastapi import FastAPI , status
from fastapi import Depends
from routers.messages import chat_router
import time as t
from fastapi import Request 
from fastapi.responses import Response , JSONResponse
from fastapi import HTTPException
from fastapi.exception_handlers import http_exception_handler

app=FastAPI()

app.include_router(chat_router)

@app.middleware("http")
async def add_process_time_header(request : Request , call_next):
    start_time = t.perf_counter()

    response= await call_next(request)

    process_time=t.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)

    return response

@app.get("/errors/not-found")
def not_found():
    raise HTTPException(
        status_code=404,
        detail= "Resource not Found"
    )

@app.exception_handlers(HTTPException)
async def custom_http_exception_handler(
    request: Request,
    exc: HTTPException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "path": request.url.path
        }
    )




def common_parameteres(page: int, limit:int):
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

@app.get("/", status_code=status.HTTP_200_OK)
def server_running():
    return {"message" : "Server is running"}

@app.get("/health", status_code=status.HTTP_200_OK)
def health_status():
    return {
        "ok": True,
        "message" : "Healthy"
    }





