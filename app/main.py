from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

id_counter = 1
posts = []

class Post(BaseModel):
    title: str
    content: str

@app.get("/posts")
def get_posts():
    return posts

@app.post("/posts")
def add_post(post: Post):
    global id_counter
    row = {
           "id": id_counter,
           "title": post.title,
           "content": post.content
    }
    id_counter += 1
    posts.append(row)
    return "row"