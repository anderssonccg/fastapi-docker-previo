from typing import Annotated
from sqlmodel import Field, SQLModel

class NoteBase(SQLModel):
    title: str
    content: str

class Note(NoteBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class NoteCreate(NoteBase):
    pass