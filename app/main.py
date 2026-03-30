from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins= ["*"]
app.add_middleware(CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

rooms={
        "room1": {
            "name": "Room 1",
            "description": "This is the single bed room."
        },
        "room2": {
            "name": "Room 2",
            "description": "This is the double bed room."
        },
        "room3": {
            "name": "Room 3",
            "description": "This is the third room."
    }
    }

@app.get("/")
def read_root():
    return { "msg": "Hello, Mestertc!", "v": "0.2" }

@app.get("/api/ip")
def read_Ip(request: Request):
    
    return {"ip": request.client.host}


@app.get("/items/{id}")
def read_item(item_id: int, q: str = None):
    return {"id": id, "q": q}


@app.get("/rooms")
def read_rooms(rooms: dict = rooms):
    return {"rooms": rooms}