
import requests
from utility.calorie_ninjas import get_key


def get_nutrients(query):
  headers = {
   'X-Api-Key' : get_key(),
  }
  r = requests.get('https://api.calorieninjas.com/v1/nutrition?query='+query, headers=headers)
  return r.json(),r.status_code