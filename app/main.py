# This file contains the FastAPI application with endpoints
import logging
from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
from database import get_db, engine
from schemas import PostCreate, PostResponse

#Configure logging
logging.basicConfig(
    filename="/app/logs/app/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

# Create database tables on startup if they do not exist
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/posts", response_model=List[PostResponse])
def get_posts(db: Session = Depends(get_db)):
    logger.info("GET /posts - fetching all posts")
    posts = db.query(models.Post).all()
    return posts

@app.post("/posts", response_model=PostResponse, status_code=201)
def add_post(post: PostCreate, db: Session = Depends(get_db)):
    logger.info(f"POST /posts - creating post: {post.title}")
    db_post = models.Post(title=post.title, content=post.content)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post