# InstaScrapper

**InstaScrapper** is a lightweight Python tool that leverages Google Custom Search Engine (CSE) to scrape public Instagram profiles.

---

## 🚀 Features

- 🔍 Searches public Instagram profiles via Google CSE
- 📧 Generates emails using a custom template
- 🧾 Exports results to:
  - `instagram_profiles.csv` — full profile data + emails
  - `instagram_profiles.txt` - profiles list
- 📓 Logs progress to `instagram_scraper.log`

---

## 📦 Requirements

1. Google Programmable Search Engine:

    - Go to: https://programmablesearchengine.google.com/

    - Click "Add" and set the sites to search as: `www.instagram.com/*`

    - Enable "Image Search" if you want photos too.

    - Note the Search Engine ID (cx).

2. Google Cloud Custom Search API Key:

    - Go to: https://console.cloud.google.com/

    - Create a new project or use an existing one.

    - Enable Custom Search API.

    - Generate an API Key.

Once you have the CX and API_KEY replace the value inside the script:

```
API_KEY = "YOUR_GOOGLE_API_KEY"
CSE_ID = "YOUR_CUSTOM_SEARCH_ENGINE_ID"
```

Install Dependencies:

```bash
python3 -m venv ENV
source ENV/bin/activate
pip install -r requirements.txt
```

Then Run Script:

```bash
python InstaScrapper.py
```

Example:
```bash
▪   ▐ ▄ .▄▄ · ▄▄▄▄▄ ▄▄▄· .▄▄ ·  ▄▄· ▄▄▄   ▄▄▄·  ▄▄▄· ▄▄▄·▄▄▄ .▄▄▄  
██ •█▌▐█▐█ ▀. •██  ▐█ ▀█ ▐█ ▀. ▐█ ▌▪▀▄ █·▐█ ▀█ ▐█ ▄█▐█ ▄█▀▄.▀·▀▄ █·
▐█·▐█▐▐▌▄▀▀▀█▄ ▐█.▪▄█▀▀█ ▄▀▀▀█▄██ ▄▄▐▀▀▄ ▄█▀▀█  ██▀· ██▀·▐▀▀▪▄▐▀▀▄ 
▐█▌██▐█▌▐█▄▪▐█ ▐█▌·▐█ ▪▐▌▐█▄▪▐█▐███▌▐█•█▌▐█ ▪▐▌▐█▪·•▐█▪·•▐█▄▄▌▐█•█▌
▀▀▀▀▀ █▪ ▀▀▀▀  ▀▀▀  ▀  ▀  ▀▀▀▀ ·▀▀▀ .▀  ▀ ▀  ▀ .▀   .▀    ▀▀▀ .▀  ▀
        🔍 Instagram Public Profile Scraper via Google CSE
                        by Tower450
    
🔍 Enter search keywords (e.g., 'fitness coach Berlin'): berlin techno
2025-09-18 15:51:20,436 [INFO] 🔄 Fetching page 1 (results 1–10)
2025-09-18 15:51:22,130 [INFO] 🔄 Fetching page 2 (results 11–20)
2025-09-18 15:51:23,536 [INFO] 🔄 Fetching page 3 (results 21–30)
2025-09-18 15:51:25,107 [INFO] 📧 Username list saved to 'instagram_profiles.csv'
2025-09-18 15:51:25,107 [INFO] ✅ Results saved to 'instagram_profiles.txt
```

You are in buisness! :)
