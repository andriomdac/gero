from pydantic import BaseModel

class SchemaArticleBase(BaseModel):
    title: str
    body: str

class SchemaArticleResponse(SchemaArticleBase):
    id: int

class SchemaArticleCreate(SchemaArticleBase):
    pass
