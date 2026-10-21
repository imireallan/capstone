from typing import TypedDict

from pydantic import BaseModel


class Answer(TypedDict):
    text: str
    context: str


class Transformer(BaseModel):
    question: str
    answers: list[Answer]
