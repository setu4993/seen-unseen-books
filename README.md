# The Seen and The Unseen - Books

A couple weeks ago, as I was about to start 'The Three Languages of Politics', I was wondering just how many episodes of [The Seen and The Unseen](http://seenunseen.in/) had the book been recommended in. One thing led to another, and I wondered: "Which are all the books that have ever been recommended on the podcast, and in which episodes?" I didn't think there was an easy way to find that, so, I built one.

A few hours and a couple weekends later, here we are.

## Implementation

I start from the podcast's RSS feed, and iteratively parse through each entry on each page. For each page, I fetch the raw HTML for the entry's show notes, and from that page, extract the books mentioned in that episode, thus creating an incremental list that maps each book with the episodes it was mentioned in.

## Tools

- `poetry` for dependency management.
- `feedparser` for parsing the RSS feed.
- `beautifulsoup4` for parsing the HTML pages.
- `streamlit` for displaying the UI / UX.

The page is also hosted on [Streamlit Sharing](https://share.streamlit.io/setu4993/seen-unseen-books/main/display.py).
