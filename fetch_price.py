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
        print(f"  قیمت     : {price}")
    else:
        print("قیمت یافت نشد.")
 




def fetch_product_name_price(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # استخراج نام محصول
    name_tag = soup.find("h1", class_="product_title")
    product_name = name_tag.text.strip() if name_tag else None

    # استخراج قیمت محصول
    price_tag = soup.find("span", class_="woocommerce-Price-amount")
    product_price = price_tag.text.strip() if price_tag else None

    return product_name, product_price


