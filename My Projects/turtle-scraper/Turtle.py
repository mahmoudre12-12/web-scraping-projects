import requests
import pandas as pd
from bs4 import BeautifulSoup
# Lists to store scraped data
turtle_names = []
turtle_info = []
# Base website URL (used to complete relative links)
base_url = "https://www.scrapethissite.com"
# Request the main turtles page (inside iframe)
page = requests.get("https://www.scrapethissite.com/pages/frames/?frame=i")
# Convert HTML into BeautifulSoup object
soup = BeautifulSoup(page.content, "lxml")
all_turtles = soup.find_all("div", class_="col-md-4 turtle-family-card")

# Loop through each turtle family
for turtle in all_turtles:
    # Extract turtle family name
    name = turtle.find("h3", class_="family-name").text.strip()
    turtle_names.append(name)
    # Get relative link
    link = turtle.find("a").get("href")
    # Combine base URL with relative link
    full_link = base_url + link
    # Request turtle details page
    page_2 = requests.get(full_link)
    soup_2 = BeautifulSoup(page_2.content, "lxml")
    # Extract description text
    info = soup_2.find("p", class_="lead").text.strip()
    turtle_info.append(info)
# Create pandas DataFrame
df = pd.DataFrame({
    "Turtle Family": turtle_names,
    "Description": turtle_info
})
# Save data to CSV file and false for index because we dont need it
df.to_csv("turtle_families.csv", index=False)
print("CSV file saved successfully!")