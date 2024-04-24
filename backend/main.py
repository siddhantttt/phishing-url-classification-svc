# main.py
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from classifier import clf
from url_analyzer import get_url_attr

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def classify(url: str = Query(None, alias='url')):
    if not url:
        raise HTTPException(status_code=400,
                            detail="URL parameter is required and cannot be empty.")
    url_attr = get_url_attr(url)
    return {'output': clf.classify(url_attr)}
