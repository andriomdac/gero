from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.config import get_db
from schemas.article import SchemaArticleCreate, SchemaArticleBase, SchemaArticleResponse



router = APIRouter(prefix="/api/articles")



@router.post("/")
def create_article(article: SchemaArticleCreate, db: Session = Depends(get_db)):
    
    return article
