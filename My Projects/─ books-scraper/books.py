from bs4 import BeautifulSoup
import requests
import pandas as pd

book_titles = []
book_prices = []
star_books = []

# Loop through all 50 pages
for page_num in range(1, 51):  # 1 to 50 (inclusive)
    print(f"Scraping page {page_num}...")  # Track progress
    
    # Fetch the page
    url = f"https://books.toscrape.com/catalogue/page-{page_num}.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    
    # Find all books on this page
    all_books = soup.find("ol", class_='row')
    book_details = all_books.find_all("article", class_='product_pod')
    
    # Extract data from each book on THIS page
    for book in book_details:
        # Get title
        title = book.find("h3").find("a")["title"]
        book_titles.append(title)
        
        # Get price
        price = book.find("p", class_='price_color').text
        book_prices.append(price)
        
        # Get star rating and convert immediately
        star_element = book.find("p", class_='star-rating')
        classes = star_element["class"]
        
        if "Five" in classes:
            star_books.append("⭐⭐⭐⭐⭐")
        elif "Four" in classes:
            star_books.append("⭐⭐⭐⭐")
        elif "Three" in classes:
            star_books.append("⭐⭐⭐")
        elif "Two" in classes:
            star_books.append("⭐⭐")
        else:
            star_books.append("⭐")

# Create DataFrame and save
MY_books = {
    "Book Title": book_titles, 
    "Book Prices": book_prices, 
    "Book Rating": star_books
}

df = pd.DataFrame(MY_books)
df.to_csv("All_Books.csv", index=False)

print(f"\nScraped {len(book_titles)} books total!")
print("Saved to All_Books.csv")