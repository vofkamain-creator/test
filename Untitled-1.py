#!/usr/bin/env python3
# Short random script generator

import random
import sys

subjects = ["A cat", "An old coder", "A wandering bot", "A small robot", "A quiet librarian"]
verbs = ["discovers", "chases", "pauses at", "builds", "whispers to"]
objects = ["a glowing key", "a forgotten line of code", "a paper boat", "a tiny star", "an empty notebook"]
places = ["under the bridge", "in the attic", "inside the server", "at dawn", "behind the curtain"]

def make_sentence():
    return f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)} {random.choice(places)}."

def main(count=5):
    for _ in range(count):
        print(make_sentence())

if __name__ == "__main__":
    try:
        n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    except Exception:
        n = 5
    main(n)