import requests
from bs4 import BeautifulSoup

def fetch_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        price_element = soup.select_one("p.price")

        if price_element:
            return price_element.get_text(strip=True)
        else:
            return "قیمت پیدا نشد."
    else:
        return f"خطا در دریافت صفحه. کد وضعیت: {response.status_code}"
