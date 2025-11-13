import json
import os

DEFAULT_SEARCH_LIMIT = 5


def load_movies() -> dict:
    path = "./data/movies.json"
    abs_path = os.path.abspath(path)
    with open(abs_path, "r") as f:
        data = json.load(f)
    return data
