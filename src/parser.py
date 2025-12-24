from bs4 import BeautifulSoup
from src.utils import is_valid_article


def extract_links(html: str) -> list[str]:
    
    soup = BeautifulSoup(html, "html.parser")
    links = []

    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"] #BeautifulSoup tag objects behave like dicts.. therefore we can do a_tag["href"] and get the value of that key... tag objects are <a> <div> <p> etc..
        if is_valid_article(href):
            links.append(href)

    links = list(set(links))
    return links