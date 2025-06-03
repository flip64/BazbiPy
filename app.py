from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fetch_price import fetch_product_name_price
import json
import os

app = FastAPI()

DB_FILE = "prices.json"

class URLInput(BaseModel):
    url: str

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {}

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.post("/check_price/")
def check_price(data: URLInput):
    url = data.url.strip()
    nameproduct ,current_price  = fetch_product_name_price(url)

    if current_price is None:
        raise HTTPException(status_code=400, detail="Could not fetch price from URL.")

    db = load_db()
    old_price = db.get(url)

    if old_price is None:
        db[url] = current_price
        save_db(db)
        return {
            "status": "first_time",
            "message": "Price saved for the first time.",
            "name" : nameproduct ,
            "price": current_price
        }

    if current_price != old_price:
        db[url] = current_price
        save_db(db)
        return {
            "name"  : nameproduct , 
            "status": "changed",
            "message": "Price has changed.",
            "old_price": old_price,
            "new_price": current_price
        }

    return {
        "status": "unchanged",
        "message": "Price has not changed.",
        "name" : nameproduct , 
        "price": current_price
    }
