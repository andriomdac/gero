from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from database.config import get_db
from database.models.article import Article
from schemas import article
from schemas.article import (
    SchemaArticleCreate,
    SchemaArticleResponse,
    SchemaArticleSummaryResponse,
    SchemaArticleUpdate
)
from utils.db import get_object_or_404


router = APIRouter(prefix="/api/articles")

def get_article_or_404(article_id: int, db: Session):
    return get_object_or_404(Article, article_id, db, "Article")


@router.post("/", response_model=SchemaArticleSummaryResponse)
def create_article(schema: SchemaArticleCreate, db: Session = Depends(get_db)):
    article = Article(
        title = schema.title,
        body = schema.body
    )
    db.add(article)
    db.commit()
    db.refresh(article)
    return article


@router.get("/", response_model=list[SchemaArticleSummaryResponse])
def list_articles(db: Session = Depends(get_db)):
    articles = db.query(Article).all()
    return articles


@router.get("/{article_id}/", response_model=SchemaArticleResponse)
def get_single_article(article_id: int, db: Session = Depends(get_db)):
    article = get_article_or_404(article_id, db)
    return article

@router.delete("/{article_id}/")
def delete_article(article_id: int, db: Session = Depends(get_db)):
    article = get_article_or_404(article_id, db)
    db.delete(article)
    db.commit()
    return Response(status_code=204)

@router.put("/{article_id}/", response_model=SchemaArticleResponse)
def update_article(article_id: int, schema: SchemaArticleUpdate, db: Session = Depends(get_db)):
    article = get_article_or_404(article_id, db)
    article.title = schema.title
    article.body = schema.body

    db.commit()
    db.refresh(article)
    return article
