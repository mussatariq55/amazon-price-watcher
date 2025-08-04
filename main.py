from bs4 import BeautifulSoup
import requests
from smtplib import SMTP
import os
from dotenv import load_dotenv
import time

# Load environment variables from .env file
load_dotenv()

# Get sensitive info securely with safe fallback
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Ensure all environment variables are loaded
if not all([SMTP_ADDRESS, EMAIL_ADDRESS, EMAIL_PASSWORD]):
    print("❗ One or more required environment variables are missing.")
    exit()

# Amazon product URL
live_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

# Custom headers to mimic a real browser
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

# Retry logic: try up to 3 times with delay
max_retries = 3
for attempt in range(max_retries):
    try:
        response = requests.get(live_url, headers=headers, timeout=10)
        if response.status_code == 200:
            break
        else:
            print(f"Attempt {attempt+1}: Failed with status code {response.status_code}")
    except requests.RequestException as e:
        print(f"Attempt {attempt+1}: Connection error: {e}")
    time.sleep(2)
else:
    print("❗ Failed to fetch product page after multiple attempts.")
    exit()

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract price components
whole_price = soup.find(class_="a-price-whole")
fraction_price = soup.find(class_="a-price-fraction")

if not whole_price or not fraction_price:
    print("❗ Could not find the price on the page. HTML structure may have changed.")
    exit()

# Combine price parts and convert to float
try:
    total_price = float(f"{whole_price.getText().replace(',', '').strip()}{fraction_price.getText().strip()}")
except ValueError:
    print("❗ Failed to parse price into a float.")
    exit()

print(f"✅ Current Price: 💲{total_price}")

# Extract product title
product_title_tag = soup.find(class_="a-size-large product-title-word-break")
if not product_title_tag:
    print("❗ Could not find the product title.")
    exit()

product_title = product_title_tag.getText().replace('\n', ' ').strip()
print(f"🛍️ Product: {product_title}")

# Send email if price is below threshold
target_price = 100
if total_price < target_price:
    try:
        with SMTP(SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=EMAIL_ADDRESS,
                to_addrs=EMAIL_ADDRESS,  # Or use a separate recipient
                msg=(
                    f"Subject: Amazon Price Alert 🚨\n\n"
                    f"{product_title} is now 💲{total_price}!\n"
                    f"Check it here: {live_url}"
                )
            )
        print("📧 Email sent successfully!")
    except Exception as e:
        print(f"❗ Failed to send email: {e}")
