from datetime import timedelta
from types import SimpleNamespace

from streamlit import title, selectbox, markdown, cache, set_page_config

from seen_unseen_books.parse_feed import fetch_books_from_feed


@cache(ttl=timedelta(days=1).total_seconds())
def books_episodes():
    return fetch_books_from_feed(5)

if __name__ == "__main__":
    create_page()
