from datetime import timedelta
from types import SimpleNamespace
from typing import List

from streamlit import experimental_memo, markdown, selectbox, set_page_config, title

from seen_unseen_books.models import Book, Episodes
from seen_unseen_books.parse_feed import (
    BOOKS_EPISODES_TUPLE,
    BOOKS_TYPE,
    EPISODES_TYPE,
    fetch_books_from_feed,
)

sort_options = SimpleNamespace(recent="Most recent", popular="Most popular")


@experimental_memo(ttl=timedelta(days=1).total_seconds())
def books_episodes() -> BOOKS_EPISODES_TUPLE:
    return fetch_books_from_feed(25)


def create_page():
    page_title = "Books from The Seen and The Unseen"
    set_page_config(page_title=page_title)
    title(page_title)

    markdown(
        "An inexhaustive list of the books mentioned in the episode notes of the podcast [The Seen and The Unseen](http://seenunseen.in/) by Amit Varma."
    )

    books, episodes = books_episodes()
    display_format = selectbox(
        "How should the list of books be sorted?",
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


def lines_from_book_episodes(
    index: int, book: Book, book_episodes: Episodes
) -> List[str]:
    lines = []
    lines = [f"{index + 1}. {book.md()}"]
    lines.extend(book_episodes.md())
    return lines


def recent_books_episodes(
    books: BOOKS_TYPE, episodes: EPISODES_TYPE
) -> List[List[str]]:
    return [
        lines_from_book_episodes(i, book, episodes[book_key])
        for i, (book_key, book) in enumerate(books.items())
    ]


def popular_books_episodes(
    books: BOOKS_TYPE, episodes: EPISODES_TYPE
) -> List[List[str]]:
    return [
        lines_from_book_episodes(i, books[book_key], book_episodes)
        for i, (book_key, book_episodes) in enumerate(
            sorted(episodes.items(), key=lambda x: len(x[1]), reverse=True)
        )
    ]


def display_footer():
    title("About")
    markdown(
        "This is **NOT** affiliated to Amit Varma or the podcast in any form, but just created as a hobby project by someone that enjoys the podcast."
    )
    markdown(
        "Built and maintained by [Setu Shah](https://setu.me/). Source on [GitHub](https://github.com/setu4993/seen-unseen-books)."
    )


if __name__ == "__main__":
    create_page()
