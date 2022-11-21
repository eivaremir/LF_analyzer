from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union
from engine import lexic,syntax
from fastapi.middleware.cors import CORSMiddleware

class Sentence(BaseModel):
    sentence: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
async def root():
    return {"message": "Hello World"}




@app.post("/lexicAnalysis")
async def lexic_analysis(body : Sentence):
    return {"analysis": lexic(body.sentence)}

@app.post("/syntaxAnalysis")
async def lexic_analysis(body : Sentence):
    return syntax(body.sentence)
