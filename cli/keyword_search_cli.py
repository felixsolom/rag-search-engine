#!/usr/bin/env python3

import argparse
from search_utils import DEFAULT_SEARCH_LIMIT, load_movies


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            # print the search query here
            print(f"Searching for: {args.query}")
            data = load_movies()
            matched_items = get_query(data, args.query)
            for i, item in enumerate(matched_items, start=1):
                print(f"{i}. {item}")
        case _:
            parser.print_help()


def get_query(data: dict, query: str) -> list[str]:
    matched_items = []
    for movie in data.get("movies", []):
        title = movie.get("title", "")
        if query in title:
            matched_items.append(title)
            if len(matched_items) >= DEFAULT_SEARCH_LIMIT:
                break
    return matched_items


if __name__ == "__main__":
    main()
