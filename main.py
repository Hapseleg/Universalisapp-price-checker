import requests

# API URL
itemIds = [41995,41996,41997]

url = f"https://universalis.app/api/v2/Europe/{itemIds}?listings=1&hq=true"

# Make a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Extract the items
    items = data.get("items", {})
    print(data)
    # Iterate over the items and print the currentAveragePriceHQ
    for item_id in itemIds:
        item = items.get(str(item_id), {})
        current_average_price_hq = item.get("currentAveragePriceHQ", None)
        print(f"Item {item_id} - currentAveragePriceHQ: {current_average_price_hq}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

