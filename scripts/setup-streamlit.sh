#!/bin/sh
set -e

mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"setu+seen-unseen-books@setu.me\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
