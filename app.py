import requests
from bs4 import BeautifulSoup
import random
import time

def scrapeWikiArticle(url, hops_remaining):
    if hops_remaining <= 0:
        print("Reached the maximum number of hops. Stopping.")
        return

    try:
        response = requests.get(
            url=url,
            headers={"User-Agent": "WikipediaScraperBot/1.0"}
        )
        response.raise_for_status()  
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find(id="firstHeading")
        if title:
            print(f"Article Title: {title.text}")
        else:
            print("Title not found. Stopping.")
            return
        all_links = soup.find(id="bodyContent").find_all("a", href=True)
        random.shuffle(all_links)  
        link_to_scrape = None
        for link in all_links:
            href = link['href']
            if href.startswith("/wiki/") and not href.startswith("/wiki/Special:"):
                link_to_scrape = "https://en.wikipedia.org" + href
                break
        if link_to_scrape:
            print(f"Next link to scrape: {link_to_scrape}")
            time.sleep(1)
            scrapeWikiArticle(link_to_scrape, hops_remaining - 1)
        else:
            print("No valid links found. Stopping.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
starting_url = input("Enter the Wikipedia article URL to start from: ").strip()
hops = int(input("Enter the number of hops to perform: "))
scrapeWikiArticle(starting_url, hops)
