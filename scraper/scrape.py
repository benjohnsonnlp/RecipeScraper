import requests
from bs4 import BeautifulSoup


def get_recipe(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    ingredients = []
    for ingredient in soup.select('[itemprop="recipeIngredient"]'):
        ingredients.append(ingredient.text)
    directions = []
    for direction in soup.select('[itemprop="recipeInstructions"]'):
        direction = direction.text.strip()
        if '\n' in direction:
            for subdirection in direction.split('\n'):
                if subdirection.strip():
                    directions.append(subdirection.strip())
        else:
            directions.append(direction)
    return {
        'ingredients': ingredients,
        'directions': directions,
    }


if __name__ == '__main__':
    print(get_recipe('https://www.allrecipes.com/recipe/240314/grandma-ruths-snickerdoodle-cookies/'))
