<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13+-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Playwright-Automation-brightgreen?logo=microsoftedge&logoColor=white" />
  <img src="https://img.shields.io/badge/BeautifulSoup-Data%20Parsing-orange?logo=html5&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Processing-yellow?logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" />
</p>

---

# 🕌 MuftiWP Irsyad Fatwa Scraper

A **fully automated Python scraper** that extracts all *Irsyad Fatwa* articles from [MuftiWP.gov.my](https://muftiwp.gov.my/en).  
It leverages **Playwright**, **BeautifulSoup**, and **Pandas** to perform structured data extraction and export them into Excel files for analysis.

This project is designed for researchers, data analysts, and developers who want to build structured datasets of Islamic fatwa articles for study or reference.

---

## ⚙️ Features

✅ Automatically scrapes all articles (titles, links, and content)  
✅ Handles **multi-page categories** (`?start=0,100,200,…`) seamlessly  
✅ Cleans HTML tags and outputs readable paragraphs  
✅ Saves output as an Excel file (`.xlsx`)  
✅ Retries safely if network delays occur  
✅ Supports different fatwa categories (Ramadhan, Haji Korban, Umum, etc.)

---

## 🧰 Tech Stack

- **Python 3.13+**
- **Playwright** (for browser automation)
- **BeautifulSoup4** (for HTML parsing)
- **Pandas** (for data processing and Excel export)

---

## 🚀 How to Run

1️⃣ **Install dependencies**
```bash
pip install -r requirements.txt

2️⃣ Run the scraper

python mufti_irsyad_scraper_playwright.py

3️⃣ Output
Your output file will be saved as:

irsyad_fatwa_umum_all_pages.xlsx
You can modify the base URL inside the script to scrape other categories like:

BASE_URL = "https://muftiwp.gov.my/en/artikel/irsyad-fatwa/irsyad-fatwa-haji-korban-cat"

📊 Example Output (Excel Preview)
Title	Content	Link
IRSYAD HUKUM SIRI KE-935: TREND BODY TEA	“This article discusses the permissibility…”	https://muftiwp.gov.my/
...
IRSYAD HUKUM SIRI KE-910: ANCAMAN PENYELUDUPAN TERHADAP NEGARA	“This fatwa explains the threat of smuggling…”	https://muftiwp.gov.my/
...

🧠 Author

Ahmad Syauqi Bin Amran Nor
📍 Kuala Lumpur, Malaysia
💼 LinkedIn Profile

📧 syauqiamran@yahoo.com

🧾 License

This project is licensed under the MIT License — you’re free to modify, distribute, or use it for your own research and projects, provided proper attribution is given.

.

🌟 Acknowledgements

Special thanks to Pejabat Mufti Wilayah Persekutuan (MuftiWP) for providing valuable open access to Islamic fatwa knowledge and scholarly references.
