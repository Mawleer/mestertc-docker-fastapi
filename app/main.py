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



@app.get("/")
def read_root():
    return { "msg": "Hello, Mestertc!", "v": "0.2" }

@app.get("/api/ip")
def read_Ip(request: Request):
    
    return {"ip": request.client.host}


@app.get("/items/{id}")
def read_item(item_id: int, q: str = None):
    return {"id": id, "q": q}


rooms=[
        {
            "name": "201",
            "description": "This is the single bed room.",
            "price": "100"
        },
      {
            "name": "202",
            "description": "This is the double bed room.",
            "price": "150"      
        },
       {
            "name": "203",
            "description": "This is the third room.",
            "price": "80"
    }
    ]


@app.get("/rooms")
def read_rooms():
    return {"rooms": rooms}


@app.post("/bookings")
def create_booking():
    #skapa bokning i DB
    return {"msg": "Booking created"}