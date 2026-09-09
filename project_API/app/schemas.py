from pydantic import BaseModel
from typing import Optional


# CREATE KNOWLEDGE
class KnowledgeCreate(BaseModel):
    category: str
    content: str


# FULL UPDATE
class KnowledgeUpdate(BaseModel):
    category: str
    content: str


# PARTIAL UPDATE
class KnowledgePatch(BaseModel):
    category: Optional[str] = None
    content: Optional[str] = None