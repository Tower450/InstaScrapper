import requests
import csv
import re
import time
import logging

API_KEY = "YOUR_GOOGLE_API_KEY"
CSE_ID = "YOUR_CUSTOM_SEARCH_ENGINE_ID"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("instagram_scraper.log"),
        logging.StreamHandler()
    ]
)

def print_banner():
    banner = r"""
▪   ▐ ▄ .▄▄ · ▄▄▄▄▄ ▄▄▄· .▄▄ ·  ▄▄· ▄▄▄   ▄▄▄·  ▄▄▄· ▄▄▄·▄▄▄ .▄▄▄  
██ •█▌▐█▐█ ▀. •██  ▐█ ▀█ ▐█ ▀. ▐█ ▌▪▀▄ █·▐█ ▀█ ▐█ ▄█▐█ ▄█▀▄.▀·▀▄ █·
▐█·▐█▐▐▌▄▀▀▀█▄ ▐█.▪▄█▀▀█ ▄▀▀▀█▄██ ▄▄▐▀▀▄ ▄█▀▀█  ██▀· ██▀·▐▀▀▪▄▐▀▀▄ 
▐█▌██▐█▌▐█▄▪▐█ ▐█▌·▐█ ▪▐▌▐█▄▪▐█▐███▌▐█•█▌▐█ ▪▐▌▐█▪·•▐█▪·•▐█▄▄▌▐█•█▌
▀▀▀▀▀ █▪ ▀▀▀▀  ▀▀▀  ▀  ▀  ▀▀▀▀ ·▀▀▀ .▀  ▀ ▀  ▀ .▀   .▀    ▀▀▀ .▀  ▀
        🔍 Instagram Public Profile Scraper via Google CSE
                        by Tower450
    """
    print(banner)

def extract_name_from_instagram_title(title):
    # Example: "John Doe (@johndoe) • Instagram photos and videos"
    match = re.match(r"^(.+?)\s+\(@.*?\)", title)
    if match:
        return match.group(1).strip()
    return ""

def extract_username_from_link(link):
    return link.rstrip('/').split('/')[-1]

def instagram_search(query, total_results=30, username_output_csv="instagram_profiles.csv", username_output_file="instagram_profiles.txt"):
    query = f"site:instagram.com {query}"
    base_url = "https://www.googleapis.com/customsearch/v1"
    
    usernames = []
    results = []
    start_index = 1
    page = 1

    while len(results) < total_results:
        logging.info(f"🔄 Fetching page {page} (results {start_index}–{start_index + 9})")

        params = {
            "key": API_KEY,
            "cx": CSE_ID,
            "q": query,
            "start": start_index,
            "num": min(10, total_results - len(results)),
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        items = data.get("items", [])
        if not items:
            logging.warning("⚠️ No more results returned by the API.")
            break

        for item in items:
            title = item.get("title", "")
            link = item.get("link", "")
            snippet = item.get("snippet", "")

            name = extract_name_from_instagram_title(title)
            username = extract_username_from_link(link)
            if username:
                usernames.append(username)

            results.append({
                "name": name,
                "username": username,
                "bio_snippet": snippet,
                "profile_url": link
            })

        start_index += 10
        page += 1
        time.sleep(1)

    with open(username_output_csv, mode='w', newline='', encoding='utf-8') as f:
        fieldnames = ["name", "username", "bio_snippet", "profile_url"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)
    
    with open(username_output_file, mode='w', encoding='utf-8') as f:
        for username in usernames:
            f.write(username + "\n")
    logging.info(f"📧 Username list saved to '{username_output_csv}'")

    logging.info(f"✅ Results saved to '{username_output_file}'")

    return results

if __name__ == "__main__":
    print_banner()
    search_query = input("🔍 Enter search keywords (e.g., 'fitness coach Berlin'): ")
    
    instagram_search(
        query=search_query,
        total_results=30,
        username_output_csv="instagram_profiles.csv",
        username_output_file="instagram_profiles.txt"
    )

