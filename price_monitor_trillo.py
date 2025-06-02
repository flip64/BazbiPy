import json
import requests
from fetch_price import get_price  # فرض می‌کنیم این تابع توی fetch_price.py هست

# فایل‌ها
INPUT_FILE = 'products.json'
PRICES_FILE = 'prices.json'

# Trello
TRELLO_API_KEY = 'your_trello_api_key'
TRELLO_TOKEN = 'your_trello_token'
TRELLO_LIST_ID = 'your_trello_list_id'  # لیستی که کارت ساخته می‌شود

def create_trello_card(name, desc):
    url = "https://api.trello.com/1/cards"
    params = {
        'key': TRELLO_API_KEY,
        'token': TRELLO_TOKEN,
        'idList': TRELLO_LIST_ID,
        'name': name,
        'desc': desc
    }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        print("کارت در Trello ساخته شد.")
    else:
        print(f"خطا در ساخت کارت Trello: {response.text}")

def load_products():
    with open(INPUT_FILE, 'r') as f:
        return json.load(f)

def load_prices():
    try:
        with open(PRICES_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_prices(prices):
    with open(PRICES_FILE, 'w') as f:
        json.dump(prices, f, indent=2)

def main():
    products = load_products()
    old_prices = load_prices()
    changed_items = []

    for product in products:
        url = product.get('url')
        product_id = product.get('id', url)
        try:
            price = get_price(url)
            old_price = old_prices.get(product_id)
            if old_price is None:
                old_prices[product_id] = price
            elif price != old_price:
                changed_items.append((product_id, url, old_price, price))
                old_prices[product_id] = price
        except Exception as e:
            print(f"خطا در گرفتن قیمت {url}: {e}")

    if changed_items:
        print("تغییرات قیمت پیدا شد و در Trello ثبت می‌شود:")
        for pid, url, old_price, new_price in changed_items:
            name = f"تغییر قیمت محصول {pid}"
            desc = f"آدرس: {url}\nقیمت قبلی: {old_price}\nقیمت جدید: {new_price}"
            create_trello_card(name, desc)
    else:
        print("هیچ تغییر قیمتی پیدا نشد.")

    save_prices(old_prices)

if __name__ == '__main__':
    main()
