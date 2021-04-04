from datetime import timedelta
from types import SimpleNamespace
from typing import List

from streamlit import title, selectbox, markdown, cache, set_page_config

from seen_unseen_books.parse_feed import (
    BOOKS_EPISODES_TUPLE,
    BOOKS_TYPE,
    EPISODES_TYPE,
    fetch_books_from_feed,
)

sort_options = SimpleNamespace(recent="Most recent", popular="Most popular")


@cache(ttl=timedelta(days=1).total_seconds())
def books_episodes() -> BOOKS_EPISODES_TUPLE:
    return fetch_books_from_feed(5)


def create_page():
    page_title = "Books from The Seen and The Unseen"
    set_page_config(page_title=page_title)
    title(page_title)

    markdown(
        "These are all the books mentioned in various episodes of the podcast [The Seen and The Unseen](http://seenunseen.in/) by Amit Varma."
    )

    books, episodes = books_episodes()
    display_format = selectbox(
        "How should the books be sorted?",
        [sort_options.recent, sort_options.popular],
    )
    if display_format == sort_options.recent:
        output_lines = recent_books_episodes(books, episodes)
    elif display_format == sort_options.popular:
        output_lines = popular_books_episodes(books, episodes)
    else:
        output_lines = []
    for lines in output_lines:
        markdown("\n".join(lines))

    display_footer()

if __name__ == "__main__":
    create_page()
