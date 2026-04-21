from fastapi import APIRouter
from app.scraper.amazon import scrape_amazon
from app.scraper.flipkart import scrape_flipkart
from app.services.anomaly import detect_anomaly

router = APIRouter()

price_history = []

@router.get("/amazon")
def get_amazon_price(url: str):
    price = scrape_amazon(url)
    price_history.append(price)
    return {"price": price}

@router.get("/flipkart")
def get_flipkart_price(url: str):
    price = scrape_flipkart(url)
    price_history.append(price)
    return {"price": price}

@router.get("/anomaly")
def anomaly():
    return {"status": detect_anomaly(price_history)}
