import fetch_price
url = "https://pakhshabdi.com/product/%da%af%db%8c%d8%b1%d9%87-%d9%86%da%af%d9%87%d8%af%d8%a7%d8%b1%d9%86%d8%af%d9%87-%d8%b3%d8%b1%d8%af%d9%88%d8%b4/"



name, price = fetch_price.fetch_product_name_price(url)
print(f"نام محصول: {name}")
print(f"قیمت: {price}")
