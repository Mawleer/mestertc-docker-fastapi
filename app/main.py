from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def read_root():
    return { "msg": "Hello, Mestertc!", "v": "0.2" }

@app.get("/api/ip")
def read_Ip(request: Request):
    
    return {"ip": request.client.host}

@app.get("/items/{id}")
def read_item(item_id: int, q: str = None):
    return {"id": id, "q": q}

