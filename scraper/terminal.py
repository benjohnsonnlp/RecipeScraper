import json

from scraper.scrape import get_recipe

url = input("Where is the yum?")

print(json.dumps(get_recipe(url), indent=4))
