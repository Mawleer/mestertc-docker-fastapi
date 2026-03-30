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

@app.get("/ip",response_class=HTMLResponse)
def read_Ip(request: Request):
    
    return (f"<h2>ip: {request.client.host}</h2>")


@app.get("/items/{id}")
def read_item(item_id: int, q: str = None):
    return {"id": id, "q": q}

