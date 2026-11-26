"""make.fun bounty: Funniest Forecast for a City That Isn't
(slug: u-eager-stork-81-9647-funniest-forecast-for-a-city-2a8769cf).

Writes one funny weather-forecast line for an invented city to
/output/entry.txt. Gate: UTF-8, 1-120 characters, not only whitespace,
no trailing newline.
"""

import os

ENTRY = "In Galehaven, the wind has joined a union and now blows nine to five only, with a strict lunch break."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
