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

if __name__ == "__main__":
    product_url = "https://pakhshabdi.com/product/%da%a9%d8%a7%d8%b1%d9%88%d8%a7%d8%b4-%d8%b3%d8%b1-%d8%a8%d8%b7%d8%b1%db%8c/"
    price = fetch_price(product_url)
    print(f"قیمت محصول: {price}")
