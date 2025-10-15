from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
from database import get_db, engine
from schemas import PostCreate

# Create tables at the first start
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    return db.query(models.Post).all()

@app.post("/posts")
def add_post(post: PostCreate, db: Session = Depends(get_db)):
    db_post = models.Post(title=post.title, content=post.content)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return "db_post"