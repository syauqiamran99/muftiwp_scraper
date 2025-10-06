# 🕌 MuftiWP Fatwa Scraper (Playwright + BeautifulSoup)

![Python](https://img.shields.io/badge/Python-3.13%2B-blue?logo=python)
![Playwright](https://img.shields.io/badge/Playwright-Automation-brightgreen?logo=microsoftedge)
![BeautifulSoup4](https://img.shields.io/badge/BeautifulSoup4-HTML%20Parser-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-success)
![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-red)

> 📚 **Automated scraper** for the [Mufti Wilayah Persekutuan](https://muftiwp.gov.my/en/) website —  
> collects, cleans, and exports all **Irsyad Fatwa** articles into a single Excel file for research and reference.

---

## 🚀 Features
✅ Fully automated scraping across all pages (`?start=0,25,50,...`)  
✅ Uses **Playwright** for full dynamic rendering  
✅ Cleans HTML using **BeautifulSoup4**  
✅ Exports articles into **Excel** neatly  
✅ Auto-detects when to stop scraping  
✅ Easy to customize for other MuftiWP categories  

---

## 🧰 Tech Stack
- **Python 3.13+**
- **Playwright**
- **BeautifulSoup4**
- **Pandas**
- **LXML + OpenPyXL**

---

## 🧑‍💻 Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/muftiwp_scraper.git
cd muftiwp_scraper
