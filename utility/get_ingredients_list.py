
import requests
from utility.spoonacular_api import get_key


def get_ingredients_list(query):
  headers = {
   'Content-Type': 'application/json'
  }
  key = get_key()
  r = requests.get(f'https://api.spoonacular.com/food/ingredients/search?sortDirection=asc&number=100&apiKey={key}&query={query}', headers=headers)
  return r.json(),r.status_code