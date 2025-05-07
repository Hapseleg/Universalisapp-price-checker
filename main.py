import requests
import time

# sorted_items = sorted(get_names(), key=lambda x: x[1])
# for name, min_Price_HQ, id in sorted_items:
#     print(f"{min_Price_HQ} - {id} - {name} ")


# https://docs.universalis.app/#market-board-current-data
# https://universalis.app/api/v2/Lightz/42000,42001?listings=0&entries=0&hq=True
def get_universalis_prices(datacenter: str, ids: str, hq : bool = None, listings=0, entries=0):
    url = f"https://universalis.app/api/v2/{datacenter}/{ids}?listings={listings}&entries={entries}"
    if hq is not None:
        url += f"&hq={hq}"
    print(url)
    response = requests.get(url)
    data = {}
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # print(data)
    return data

# https://v2.xivapi.com/api/docs
# https://v2.xivapi.com/api/sheet/Item?rows=42000,42001
def get_xivapi_data(ids):
    url = f"https://v2.xivapi.com/api/sheet/Item?rows={ids}"
    response = requests.get(url)
    data = {}
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
    print(data)

# https://v2.xivapi.com/api/sheet/RecipeLookup/42000
# loop fields, if ALC.value != 0 then theres a recipe ID
# "BSM": {
#       "value": 5757,
#       "sheet": "Recipe",
#       "row_id": 5757,
#       "fields": {
#           "AmountIngredient": [2, 2, 1, 1, 0, 0, 8, 7],
#           "Ingredient": [
#               "row_id": 43998,
#                    "fields": {
#                       "Name": "Ruthenium Ingot",

get_universalis_prices("Light", "42000,42001", hq=True)
get_xivapi_data('42000')