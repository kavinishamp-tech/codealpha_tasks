import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "https://books.toscrape.com/catalogue/"
RATING_MAP = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

headers = {"User-Agent": "Mozilla/5.0"}
data = []
page = 1

while True:
    url = f"{BASE_URL}page-{page}.html"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        break  # No more pages

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text.strip()
        rating = RATING_MAP.get(book.p["class"][1], 0)  # Convert to number
        data.append([title, price, rating])

    page += 1

df = pd.DataFrame(data, columns=["Title", "Price", "Rating"])
df.to_csv("books_dataset.csv", index=False)
print(f"Scraping complete! {len(df)} books saved.")
