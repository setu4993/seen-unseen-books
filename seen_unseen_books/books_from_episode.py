from re import sub
from typing import Dict
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from seen_unseen_books.models import Book


BOOK_KEYS_BLACKLIST = [
    "indian_express",
    "times_of_india",
    "economic_times",
    "hindu",
    "mint",
]


def remove_special_characters(input_str: str) -> str:
    return sub(r"\W+", " ", input_str).strip()


def book_key(input_str: str) -> str:
    return sub(r"\s+", "_", input_str.lower())


def fetch_books_from_episode(episode_url: str) -> Dict[str, Book]:
    html_page = requests.get(episode_url)
    parsed_html = BeautifulSoup(html_page.text, "html.parser")

    content_div = parsed_html.find("div", attrs={"class": "entry-content"})
    content_div_strings = [s for s in content_div.stripped_strings]

    content_div_sequential = {
        curr_str: next_str
        for curr_str, next_str in zip(content_div_strings[:-1], content_div_strings[1:])
    }

    books = {}
    for i_tag in content_div.find_all("i"):
        name = remove_special_characters(i_tag.text)
        try:
            author = remove_special_characters(content_div_sequential[i_tag.text])
        except KeyError:
            continue
        try:
            google_redirect_url = urlparse(i_tag.a["data-saferedirecturl"])
            book_url = urlparse(google_redirect_url.query[2:]).geturl()
        except TypeError:
            book_url = None

        if book_key(name) in BOOK_KEYS_BLACKLIST:
            continue

        books[book_key(name)] = Book(
            title=name,
            author=author,
            url=book_url,
        )
    return books
