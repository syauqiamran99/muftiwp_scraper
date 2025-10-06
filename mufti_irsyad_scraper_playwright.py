from playwright.sync_api import sync_playwright
import pandas as pd
import time
from bs4 import BeautifulSoup
import re

# 🌐 Base URL (no need to change unless switching categories)
BASE_URL = "https://muftiwp.gov.my/en/artikel/irsyad-fatwa/irsyad-fatwa-umum-cat"

data = []

def safe_get_html(page, selector, retries=5, delay=2):
    """Safely fetch element inner_html with retries."""
    for attempt in range(retries):
        try:
            el = page.query_selector(selector)
            if el:
                html_content = el.inner_html().strip()
                if html_content:
                    return html_content
        except Exception as e:
            print(f"⚠️ Attempt {attempt + 1} failed: {e}")
        time.sleep(delay)
    return ""

# 🚀 Main scraping loop
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    for start in range(0, 2000, 25):  # ✅ Fixed pagination: 0, 25, 50, 75, ...
        url = f"{BASE_URL}?start={start}" if start > 0 else BASE_URL
        print(f"\n🔍 Launching Chromium for page start={start}...")

        try:
            page.goto(url, timeout=60000)
            page.wait_for_load_state("networkidle")
            page.wait_for_timeout(3000)

            # 🧩 Save rendered HTML (optional debug)
            safe_page_name = re.sub(r'[^a-zA-Z0-9_-]', '_', str(start))
            with open(f"rendered_page_umum_{safe_page_name}.html", "w", encoding="utf-8") as f:
                f.write(page.content())

            # ✅ Extract list of articles
            article_links = page.query_selector_all("td.list-title a")

            if not article_links:
                print(f"⚠️ No more articles found at start={start}. Stopping loop.")
                break

            print(f"✅ Found {len(article_links)} articles on page {start}.")
            links = []
            for a in article_links:
                href = a.get_attribute("href")
                title = a.inner_text().strip() if a.inner_text() else "Untitled"
                if href:
                    full_link = "https://muftiwp.gov.my" + href if href.startswith("/") else href
                    links.append((title, full_link))

            print(f"🔗 Prepared {len(links)} links for scraping.\n")

            # 📚 Scrape each article
            for idx, (title, link) in enumerate(links, start=1):
                print(f"📖 [{idx}/{len(links)}] Fetching: {title}")

                try:
                    page.goto(link, timeout=60000)
                    page.wait_for_load_state("networkidle")
                    page.wait_for_timeout(3000)

                    found = False
                    for attempt in range(3):
                        try:
                            page.wait_for_selector("div[itemprop='articleBody'] p", timeout=8000)
                            found = True
                            break
                        except:
                            print(f"⚠️ Attempt {attempt + 1}: content not ready, retrying...")
                            time.sleep(2)

                    if not found:
                        print(f"❌ No article content found for: {title}")
                        content_text = "No content found."
                    else:
                        html_body = safe_get_html(page, "div[itemprop='articleBody']")
                        soup = BeautifulSoup(html_body, "html.parser")

                        paragraphs = []
                        for p_tag in soup.find_all("p"):
                            text = p_tag.get_text(separator=" ", strip=True)
                            if text:
                                paragraphs.append(text)

                        content_text = "\n\n".join(paragraphs) if paragraphs else "No content found."

                    data.append({
                        "E": title,
                        "F": content_text.strip(),
                        "I": link
                    })

                    print(f"✅ Done: {title}\n")
                    time.sleep(2)

                except Exception as e:
                    print(f"❌ Error scraping {link}: {e}\n")
                    data.append({"E": title, "F": "Error loading page", "I": link})
                    continue

        except Exception as e:
            print(f"🚨 Error loading page {url}: {e}")
            continue

    browser.close()

# 💾 Save to Excel with clear name
safe_name = re.sub(r'[^a-zA-Z0-9_-]', '_', "irsyad_fatwa_umum_all_pages")
output_file = f"{safe_name}.xlsx"

df = pd.DataFrame(data, columns=["E", "F", "I"])
df.to_excel(output_file, index=False)

print(f"\n🎉 Done! Saved {len(df)} articles across all pages to {output_file}")
print("💡 Tip: In Excel, enable 'Wrap Text' for Column F to view full text neatly.")
