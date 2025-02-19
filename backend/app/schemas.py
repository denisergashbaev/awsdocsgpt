from pydantic import BaseModel, HttpUrl

class query(BaseModel):
    prompt: str
    temperature: float | None = 0.00
    similarity_threshold: float | None = 0.50
    sentences: str | None = "short"
    results: int | None = 5

class chunk(BaseModel):
    page_title: str
    page_url: HttpUrl
    content: str
    similarity: float

class search_response(BaseModel):
    sources: list[chunk]

class chat_response(search_response):
    answer: str