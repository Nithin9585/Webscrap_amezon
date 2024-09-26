from bs4 import BeautifulSoup
import os
import csv

# Create a CSV file and write the header row
with open('amazon_data.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Price', 'Number of Buyers', 'Number of Ratings', 'Rating', 'Image Link'])

    # Loop through HTML files in the 'data' directory
    for file in os.listdir("data"):
        with open(f"data/{file}", encoding="utf-8") as f:
            html_doc = f.read()
        
        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html_doc, 'html.parser')
        
        # Extract the title
        title_tag = soup.find("span", class_="a-size-base-plus a-color-base a-text-normal")
        title = title_tag.get_text(strip=True) if title_tag else "N/A"
        
        # Extract the price
        price_tag = soup.find("span", class_="a-price-whole")
        price = price_tag.get_text(strip=True) if price_tag else "N/A"
        
        # Extract the number of buyers
        buyers_tag = soup.find("span", class_="a-size-base a-color-secondary")
        buyers = buyers_tag.get_text(strip=True) if buyers_tag else "N/A"
        
        # Extract the number of ratings
        ratings_tag = soup.find("span", class_="a-size-base s-underline-text")
        ratings = ratings_tag.get_text(strip=True) if ratings_tag else "N/A"
        
        # Extract the rating
        rating_tag = soup.find("span", class_="a-icon-alt")
        rating = rating_tag.get_text(strip=True) if rating_tag else "N/A"
        
        # Extract the image link
        img_tag = soup.find("img", class_="s-image")
        img_link = img_tag['src'] if img_tag and 'src' in img_tag.attrs else "N/A"
        
        # Print the extracted data (optional)
        
        
        # Write the data to the CSV file
        writer.writerow([title, price, buyers, ratings, rating, img_link])
