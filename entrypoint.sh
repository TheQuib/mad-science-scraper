#!/bin/sh

INTERVAL=${SCRAPE_INTERVAL:-300}

while true
do
    python scraper.py
    sleep "$INTERVAL"
done