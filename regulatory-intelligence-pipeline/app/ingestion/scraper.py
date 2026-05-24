import requests
from bs4 import BeautifulSoup

FCA_URL = "https://www.fca.org.uk/news"


def fetch_fca_updates():
    response = requests.get(FCA_URL)

    soup = BeautifulSoup(response.text, "html.parser")

    headlines = soup.find_all("a")

    updates = []

    for item in headlines[:10]:
        text = item.get_text(strip=True)

        if text:
            updates.append({
                "title": text,
                "content": f"Regulatory update regarding {text}"
            })

    return updates