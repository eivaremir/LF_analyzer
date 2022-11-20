from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
from engine import lexic
class Sentence(BaseModel):
    sentence: str

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}




@app.post("/lexicAnalysis")
async def lexic_analysis(body : Sentence):
    return {"analysis": lexic(body.sentence)}
