from collections import defaultdict
from typing import Dict, Tuple

from feedparser import parse
from loguru import logger

from seen_unseen_books.books_from_episode import fetch_books_from_episode
from seen_unseen_books.models import Episode, Episodes


def fetch_books_from_feed(max_pages: int = 20) -> Tuple[dict, dict]:
    books = {}
    episodes: Dict[str, Episodes] = defaultdict(Episodes)

    # Page 0 and page 1 of the RSS feed are the same, so we skip page 0.
    for page in range(1, 1 + max_pages):
        feed = parse(f"https://seenunseen.in/feed/?paged={page}")

        for entry in feed.entries:
            episode_url = entry.links[0]["href"]
            episode_books = fetch_books_from_episode(episode_url)
            # Replace previously cached books with new ones if there's ones with the same key.
            books.update(episode_books)
            episode = Episode(title=entry["title"], url=episode_url)
            for book in episode_books.keys():
                episodes[book].episodes.append(episode)
        logger.info(f"Page {page} parsed. Total books so far: {len(books)}.")

    return books, episodes
