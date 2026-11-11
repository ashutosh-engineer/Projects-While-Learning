from pydantic import BaseModel 
from fastapi import BackgroundTasks
from fastapi import APIRouter , status

chat_router=APIRouter(prefix = "/messages" , tags=["Messages"])

class Chatmessage(BaseModel):
    sender: str
    message: str
    room_id:int 

def write_file_logs(message: str):
    with open("logs.txt", "a", encoding="utf-8") as file:
        file.write(f"{message}\n")


@chat_router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Create a chat message"
)
def messages(
    chat: Chatmessage,
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(
        write_file_logs,
        f"{chat.sender}: {chat.message}"
    )
    return {
        "sender" : chat.sender,
        "message" : chat.message,
        "room_id" : chat.room_id
    }
