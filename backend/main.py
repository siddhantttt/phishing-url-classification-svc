# main.py
from fastapi import FastAPI, Query

from classifier import clf
from url_analyzer import get_url_attr

app = FastAPI()


@app.get("/classify")
def classify(url: str = Query(None, alias='url')):
    url_attr = get_url_attr(url)
    print(clf)
    return {}
