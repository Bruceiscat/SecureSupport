from fastapi import FastAPI
from pydantic import BaseModel

#intialize
app = FastAPI()

ORDERS = {
    1: {"id": 1, "item": "Keyboard", "price": 100, "owner": "justin"},
    2: {"id":2, "item": "Dog", "price":330, "owner": "bob"}
}

#validating
class ChatRequest (BaseModel):
    message:str



@app.post("/chat")
def chat(messages:ChatRequest):
    return messages

@app.get("/orders/{order_id}")
def order(order_id:int):
    return {"Order_id":ORDERS.get(order_id)}