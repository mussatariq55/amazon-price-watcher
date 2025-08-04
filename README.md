
# 🛒 Amazon Price Watcher in Python
A secure and lightweight price tracker for Amazon products, built with Python. Get notified via email when the price of a product drops below your desired threshold.

This project showcases web scraping, email automation, and secure credential management — a practical blend of convenience and code.

<img width="3072" height="2048" alt="tycs1x7jaxrga0creef81y3jg4" src="https://github.com/user-attachments/assets/5de0565d-0c34-4882-9666-4bbb3cb07946" />

---

## 🚀 Features
- Scrapes real-time Amazon product prices using `BeautifulSoup`
- Sends you an email alert when the price drops below your set limit
- Uses secure environment variables — no passwords hardcoded in code
- Mimics a browser session to reduce bot detection
- Designed to run manually or on a schedule (e.g. via cron or Task Scheduler)  

---

## 🧠 Built With
- Python 3.7+  
- `requests` for making HTTP requests  
- `smtplib` to send secure email alerts
- `BeautifulSoup` for HTML parsing 
- `dotenv`  to manage sensitive credentials with a `.env` file  
- Amazon product pages (no API needed)

---

## 💻 How It Works
1. The script sends a request to your chosen Amazon product page.
2. It parses the page to extract the current price and product title.
3. If the price is lower than your target threshold: It sends you a formatted email with the price and link.
4. Otherwise, it exits silently — ready to check again later.

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/amazon-price-watcher.git
cd amazon-price-watcher
```

### 2. Install Dependencies
```bash
pip install requests
pip install beautifulsoup4
pip install python-dotenv
```

### 3. Set Environment Variables

#### Create a .env file:
```bash
SMTP_ADDRESS=smtp.gmail.com
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
```
---

## ▶️ Running the Script
After setting the environment variables, run the script:

```bash
python main.py
```
The script will:
- Check the product’s current price
- Send an email alert if it’s below your threshold
- You can run this manually or schedule it to run automatically using cron (Linux/macOS) or Task Scheduler (Windows).

---
## 🙌 Credits
- 👨‍💻 **Built by: Mussa Tariq
- LinkedIn: https://www.linkedin.com/in/mussa-tariq-0652712a0/
- 📦 Amazon – for product pages
- 🧪 BeautifulSoup
- 📧 Python’s smtplib
---

## 📬 Final Note
Now you’ll never miss a deal. Let Python do the watching — and you do the saving.



