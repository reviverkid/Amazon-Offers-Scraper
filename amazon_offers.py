import requests
from bs4 import BeautifulSoup
import time

def scrape_amazon_offers(search_query):
    search_query = search_query.replace(' ', '+')
    url = f"https://www.amazon.in/s?k={search_query}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "DNT": "1",  
        "Connection": "keep-alive",
    }

    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            
            for item in soup.select(".s-main-slot .s-result-item"):
                
                
                title_tag = item.h2  
                if title_tag: 
                    title = title_tag.get_text(strip=True)
                    try:
                        price = item.select_one(".a-price-whole").get_text(strip=True)
                        print(f"Product: {title}\nPrice: ₹{price}\n")
                    except AttributeError:
                        print("Price not found, skipping item...")
                        continue
                else:
                    print("No title found for this item, skipping...")
        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

# Example usage
scrape_amazon_offers("laptop deals")
