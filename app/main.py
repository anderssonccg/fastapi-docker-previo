from fastapi import FastAPI, Request
from sqlmodel import create_engine, Session, select
from models import Note, NoteCreate
import json
import os

user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
host = os.getenv("DB_HOST")
database = os.getenv("DB_NAME")
port = os.getenv("DB_PORT")
url = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(url, echo=True)

app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Welcome to the FastAPI application! "
        "You can use this API to manage your notes."
    }


@app.get("/notes")
async def get_notes():
    with Session(engine) as session:
        notes = session.exec(select(Note)).all()
    return {"notes": notes}


@app.post("/notes")
async def create_note(note: NoteCreate):
    with Session(engine) as session:
        note_create= Note.model_validate(note)
        session.add(note_create)
        session.commit()
        session.refresh(note_create)
