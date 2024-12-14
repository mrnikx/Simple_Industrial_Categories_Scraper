import requests
from bs4 import BeautifulSoup
import pandas as pd
from config import URL as url

# Send request to Wikipedia
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")
    
    # List of unrelated categories that need to be identified
    excluded_categories = ["فهرست", "منابع"]
    
    # final list for storing information
    industries = []
    
    # Find all category titles (h2 , h3)
    for header in soup.find_all(["h2", "h3"]):
        category_title = header.text.strip()  # Category title
        
        # Checking that the category in the list is not irrelevant
        if category_title in excluded_categories:
            continue

        # Find the first <ul> list after sorting
        ul = header.find_next("ul")
        if ul is None:
            print(f"No list found for '{category_title}' category")
            continue  # Continue to the next category

        # Extract all items from a <li> list
        for li in ul.find_all("li"):
            industries.append({
                "Category": category_title,
                "Industry": li.text.strip()
            })

    # Save data to Excel file
    if industries:
        df = pd.DataFrame(industries)
        df.to_excel("tabriz_industries.xlsx", index=False)
        print("The data was successfully extracted and saved in an Excel file")
    else:
        print("No data were found!")
else:
    print("Error connecting to Wikipedia!")
