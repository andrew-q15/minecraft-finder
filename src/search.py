import requests


def searchFromWiki(query: str) -> list:
    response = requests.get(
        f"https://minecraft.wiki/rest.php/v1/search/page?format=json&limit=5&q={query}"
    )
    data = response.json()
    return data.get("pages", [])
