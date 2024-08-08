import requests
import time

# API URL
startId = 41990
#endId   = 42000
endId   = 42869
itemIds = []
counter = startId
item_list = []

while counter < endId:
    for i in range(100):
        if counter < endId:
            itemIds.append(counter)
        counter += 1
    

    joined_string = ','.join(str(element) for element in itemIds)
    print(joined_string)

    url = f"https://universalis.app/api/v2/Light/{joined_string}?listings=1&entries=0&hq=true"
    print(url)

    # Make a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Extract the items
        items = data.get("items", {})
        #print(items)
        # Iterate over the items and print the currentAveragePriceHQ
        for item_id in itemIds:
            item = items.get(str(item_id), {})
            min_Price_HQ = item.get("minPriceHQ", None)
            if min_Price_HQ != None and min_Price_HQ > 70000:
                item_list.append((item_id, min_Price_HQ))
            
        

    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

    time.sleep(1)
    itemIds.clear()

xivapiUrl = "https://xivapi.com/item?ids="
for item_id, min_Price_HQ in item_list:
    xivapiUrl += str(item_id) + ','

my_list = []

response = requests.get(xivapiUrl)
if response.status_code == 200:
    data = response.json()

    results = data.get("Results", {})
    
    
    for result in results:
        #print(result)
        for item in item_list:
            if item[0] == result["ID"]:
                my_list.append((result["Name"], item[1], item[0]))

print(my_list)



sorted_items = sorted(my_list, key=lambda x: x[1])
for name, min_Price_HQ, id in sorted_items:
    print(f"{min_Price_HQ} - {id} - {name} ")