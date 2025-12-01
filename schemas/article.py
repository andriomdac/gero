from pydantic import BaseModel


class SchemaArticleBase(BaseModel):
    id: int
    body: str
    title: str

class SchemaArticleSummaryResponse(BaseModel):
    id: int
    title: str

class SchemaArticleResponse(BaseModel):
    id: int
    title: str
    body: str

class SchemaArticleCreate(BaseModel):
    title: str
    body: str

class SchemaArticleUpdate(SchemaArticleCreate):
    pass
