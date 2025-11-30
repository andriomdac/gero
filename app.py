from fastapi import FastAPI
from routers.article import router as article_router
from database.config import Base, engine

app = FastAPI()
app.include_router(article_router)
