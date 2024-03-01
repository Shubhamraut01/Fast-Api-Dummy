from typing import Union
import random
from datetime import datetime
from pydantic import BaseModel
from fastapi import FastAPI , HTTPException

app = FastAPI()

books = ["Python", "Java", "C++", "C", "C#", "JavaScript", "TypeScript", "Go", "Rust", "Kotlin", "Swift", "Dart", "PHP", "Ruby", "Perl", "R", "Scala", "Groovy", "Lua", "Haskell", "Erlang", "Clojure", "F#", "Rust", "Kotlin", "Swift", "Dart", "PHP", "Ruby", "Perl", "R", "Scala", "Groovy", "Lua", "Haskell", "Erlang", "Clojure", "F#"]

@app.get("/")
async def read_root():
    return {"Hello": "World","author":"Shubham"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    if len(books) < book_id:
        raise HTTPException(status_code=404,detail = f"Item not found")
    else:
        return {"book_name": books[book_id]}

@app.get("/random/")
async def random_book():
    return { books[random.randint(0,len(books)-1)]}


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
print(external_data)
user = User(**external_data)
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123