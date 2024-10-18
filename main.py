from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class Item(BaseModel):
    id: int
    request: str
    response: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

items = []

@app.post("/items/")
async def create_item(item: Item):
    items.append(item)
    return {"message": "Item adicionado com sucesso!", "item": item}

@app.get("/items/")
async def get_items():
    return items

@app.get("/items/{id}")
async def get_item(id: str):
    for item in items:
        if item.id == id:
            return item
    return {"error": "Item não encontrado"}

# uvicorn main:app --reload