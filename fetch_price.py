import requests
from bs4 import BeautifulSoup

def get_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("خطا در دریافت صفحه")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    price_tag = soup.find("span", class_="woocommerce-Price-amount amount")
    if price_tag:
        price = price_tag.get_text(strip=True)
        print(f"قیمت قهوه جوش ۳ کاپ استیل: {price}")
    else:
        print("قیمت یافت نشد.")

