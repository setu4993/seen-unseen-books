from datetime import timedelta
from types import SimpleNamespace

from streamlit import title, selectbox, markdown, cache, set_page_config

from seen_unseen_books.parse_feed import fetch_books_from_feed

if __name__ == "__main__":
    create_page()
