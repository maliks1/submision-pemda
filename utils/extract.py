from urllib.parse import urljoin
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup


BASE_URL = "https://fashion-studio.dicoding.dev/"


def _fetch_soup(url):
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, timeout=15) as response:
        html = response.read()
    return BeautifulSoup(html, "html.parser")


def _extract_from_card(card):
    lines = [line.strip() for line in card.get_text("\n", strip=True).splitlines() if line.strip()]
    product = {
        "Title": "",
        "Price": "",
        "Rating": "",
        "Colors": "",
        "Size": "",
        "Gender": "",
    }

    if lines:
        product["Title"] = lines[0]

    for line in lines:
        if not product["Price"] and (line.startswith("$") or line.lower() == "price unavailable"):
            product["Price"] = line
        if "rating" in line.lower() and not product["Rating"]:
            product["Rating"] = line
        if "colors" in line.lower() and not product["Colors"]:
            product["Colors"] = line
        if line.lower().startswith("size:"):
            product["Size"] = line.split(":", 1)[1].strip()
        if line.lower().startswith("gender:"):
            product["Gender"] = line.split(":", 1)[1].strip()

    return product


def extract_products(start_url=None):
    current_url = start_url or BASE_URL
    visited_urls = set()
    products = []
    next_id = 1

    while current_url and current_url not in visited_urls:
        visited_urls.add(current_url)

        try:
            soup = _fetch_soup(current_url)
        except Exception:
            break

        titles = soup.find_all("h3")
        for title in titles:
            card = title.find_parent(["article", "div", "li"]) or title.parent
            if not card:
                continue

            product = _extract_from_card(card)
            if product["Title"]:
                product["id"] = str(next_id)
                products.append(product)
                next_id += 1

        next_link = soup.find("a", string=lambda s: bool(s and s.strip().lower() == "next"))
        if not next_link:
            next_link = soup.find("a", string=lambda s: bool(s and "next" in s.strip().lower()))

        if not next_link:
            break

        href = (next_link.get("href") or "").strip()
        if not href or href == "#":
            break

        current_url = urljoin(current_url, href)

    return products
