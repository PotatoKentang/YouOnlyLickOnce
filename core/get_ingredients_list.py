
import requests
from utility.spoonacular_api import get_key


def get_ingredients_list(query):
  headers = {
   'Content-Type': 'application/json'
  }
  key = get_key()
  r = requests.get(f'https://api.spoonacular.com/food/ingredients/search?query={query}&sortDirection=asc&number=100&apiKey={key}', headers=headers)
  return r.json(),r.status_code

def get_ingredients_list_by_id(id,amount="150",unit="grams"):
  headers = {
   'Content-Type': 'application/json'
  }
  key = get_key()
  r = requests.get(f'https://api.spoonacular.com/food/ingredients/{id}/information?apiKey={key}&amount={amount}&unit={unit}', headers=headers)
  return r.json(),r.status_code