from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

#必須放在{item_id}上方，否則無法讀取
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/items/{item_id}")
async def read_item(item_id : int):
    return {"item_id": item_id}