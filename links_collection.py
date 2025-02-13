# To ensure the above script runs smoothly in PowerShell, 
# install the necessary dependencies using the following commands:

# Upgrade pip
# python -m pip install --upgrade pip

# Install required libraries
# pip install pandas playwright openpyxl cloudscraper

# Install Playwright browsers
# python -m playwright install

# (Optional) If using Playwright with Chromium only
# python -m playwright install chromium
# #-----------------------------------------------------------------------------------------

#Final code to copy all the company urls from all the pages from Zuba Crop Website.

import time
import random
import pandas as pd
import cloudscraper
from playwright.sync_api import sync_playwright

def scrape_company_urls(base_url, max_pages, output_file):
    company_urls = []
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/537.36"
    ]
    
    scraper = cloudscraper.create_scraper()
    
    with sync_playwright() as p:
        print("Launching browser...")
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        print("Browser launched.")
        
        for page_number in range(1, max_pages + 1):
            if page_number == 1:
                current_page_url = base_url
            else:
                current_page_url = base_url.replace(
                    "https://www.zaubacorp.com/companies-list/nic-K/city-MUMBAI/age-B/paidupcapital-D-company.html",
                    f"https://www.zaubacorp.com/companies-list/nic-K/city-MUMBAI/age-B/paidupcapital-D/p-{page_number}-company.html"
                )

            print(f"Fetching page: {current_page_url}")
            
            # Randomize headers for each request
            scraper.headers.update({"User-Agent": random.choice(user_agents)})
            
            # Add random delay to avoid rate-limiting
            time.sleep(random.uniform(5, 10))  # Wait 5-10 seconds
            
            response = scraper.get(current_page_url)
            if response.status_code == 200:
                print(f"Successfully accessed page {page_number}")
                page.set_content(response.text)
            elif response.status_code == 429:
                print(f"⚠️ 429 Too Many Requests. Retrying after a longer wait...")
                time.sleep(random.uniform(20, 30))  # Wait 20-30 seconds before retrying
                continue
            else:
                print(f"❌ Failed to fetch page {page_number}, Status Code: {response.status_code}")
                continue
            
            # Extract all company links from the current page
            company_links = page.query_selector_all(
                "body > main > div > div > div.container.information > div:nth-child(2) > table > tbody > tr > td:nth-child(2) > a"
            )
            print(f"Found {len(company_links)} company links on page {page_number}")
            
            for link in company_links:
                url = link.get_attribute("href")
                if url and url not in company_urls:
                    company_urls.append(url)
            print(f"Total collected URLs so far: {len(company_urls)}")
        
        browser.close()
        print("Browser closed.")
    
    print("Saving URLs to Excel...")
    df = pd.DataFrame({'URL': company_urls})
    df.to_excel(output_file, index=False, engine='openpyxl')
    print(f"Scraped {len(company_urls)} URLs and saved to {output_file}")

# Usage Example
base_url = "https://www.zaubacorp.com/companies-list/nic-K/city-MUMBAI/age-B/paidupcapital-D-company.html"
max_pages = 3
output_file = "MumRRB13251.xlsx"
scrape_company_urls(base_url, max_pages, output_file)






