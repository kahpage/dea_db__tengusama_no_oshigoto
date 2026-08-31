import sys
import json
from pathlib import Path
from typing import Any
import requests
from bs4 import BeautifulSoup
import lxml
import re

# Add project root to sys.path (find the directory containing db_structs.py)
_root = Path(__file__).resolve().parent
while _root.parent != _root:
    if (_root / "db_structs.py").exists():
        if str(_root) not in sys.path:
            sys.path.append(str(_root))
        break
    _root = _root.parent

from db_structs import (
    Medium,
    Circle,
    Event,
    EventGroup,
    Source,
    ReliabilityTypes,
    OriginTypes,
    Location,
)

PATH_EVENT = Path(__file__).parent
PATH_CIRCLES_JSON = PATH_EVENT / "circles.json"
NAME = PATH_EVENT.name


def retrieve_soup_fetch_if_needed(url: str) -> BeautifulSoup:
    """Retrieve BeautifulSoup object for the given URL, fetching the content if necessary."""
    html_path = PATH_EVENT / "raw.html"
    if not html_path.exists():
        print(f"Raw HTML file not found, fetching from {url} ...")
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(
                f"Failed to retrieve data from {url}, status code: {response.status_code}"
            )
        html_path.write_bytes(response.content)
    with html_path.open("rb") as f:
        return BeautifulSoup(f, "html.parser")


def sanitize_string(s: str) -> str:
    s = s.strip()
    s = re.sub(r"[\s\n\t]+", " ", s)
    return s


def main():
    """Create circles.json"""
    print(f"Retrieving circles information for {NAME} ...")
    raw_url = "https://web.archive.org/web/20160306174301id_/http://project-d.biz/eiyasho/circle_list.html"
    
    # Parse the HTML content to extract circle information
    soup = retrieve_soup_fetch_if_needed(raw_url)
    circles = []

    # table: with border=1
    tables = soup.select('table[cellpadding="0"]')
    # enabled = False
    
    for table in tables:
        table_rows = table.select("tr")
        if not table_rows:
            raise Exception("No rows found in the circles table.")

        for row in table_rows: 
                cols = row.select("td")
                if len(cols) < 7:
                    print("Skipping row with insufficient columns:", row)
                    continue

                circle_name = sanitize_string(cols[0].get_text())
                # if "天狗様のお仕事６" in position:
                #     enabled = True
                #     continue
                # if "諏訪子ランド３" in position:
                #     enabled = False
                #     continue
                # if not enabled:
                #     continue  # Skip until we find the enabled section
                # if len(cols) < 6:
                #     print("Skipping row with insufficient columns:", row)
                    # continue
                if "サークル名" in circle_name:
                    continue  # Skip header row
                event = sanitize_string(cols[2].get_text())
                if "天狗様のお仕事" not in event:
                    continue  # Skip rows not related to the specific event
                pen_name = sanitize_string(cols[1].get_text())
                if not pen_name:
                    continue  # Skip rows without pen name
                position = sanitize_string(cols[3].get_text())
                circle_links: list[str] = []
                hp_tag = cols[4].select_one("a")
                if hp_tag and hp_tag.has_attr("href"):
                    circle_links.append(hp_tag["href"])
                pixiv_tag = cols[5].select_one("a")
                if pixiv_tag and pixiv_tag.has_attr("href"):
                    circle_links.append(pixiv_tag["href"])
                twitter_tag = cols[6].select_one("a")
                if twitter_tag and twitter_tag.has_attr("href"):
                    circle_links.append(twitter_tag["href"])

                circle = Circle(
                    aliases=[circle_name],
                    pen_names=[pen_name] if pen_name else None,
                    links=circle_links if circle_links else None,
                    position=position,
                    # comments=", ".join(comment_parts) if comment_parts else None,
                )

                circles.append(circle)

    # Save the extracted circle information to a JSON file
    with open(PATH_CIRCLES_JSON, "w", encoding="utf-8") as f:
        json.dump([c.get_json() for c in circles], f, ensure_ascii=False, indent=2)
    print(f"Saved {len(circles)} circles to {PATH_CIRCLES_JSON}")


if __name__ == "__main__":
    main()
