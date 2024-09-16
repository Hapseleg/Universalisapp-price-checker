import requests
import time

# API URL
startId = 41990
#endId   = 42000
endId   = 43347
itemIds = []
counter = startId
item_list = []

def get_item_list(url_extra, ids_arr, min_price, tag):
    ids = ','.join(str(element) for element in ids_arr)
    url = f"https://universalis.app/api/v2/Light/{ids}{url_extra}"
    got_list = []
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
        for item_id in ids_arr:
            item = items.get(str(item_id), {})
            min_Price_HQ = item.get(tag, None)
            #print(min_Price_HQ)
            #print(item.get("itemID", None))
            if min_Price_HQ != None and min_Price_HQ > min_price:
                got_list.append((item_id, min_Price_HQ))
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

    time.sleep(1)
    print(got_list)
    return got_list
    #itemIds.clear()

def get_names():
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
    return my_list
                     

def timed_node_Ids(exp):
    ids_arr = []
    match exp:
        case "arr":
            ids_arr =  [4800,4816,5118,5120,5121,5146,5147,5148,5149,5150,5151,5158,5273,5350,5365,5394,5395,5537,5545,5546,5547,6147,6148,6152,6199,6209,7588,7589,7590,7591,7592,7593,7594,7595,7610,7611,7724,7733,7734,7760,7763,7766,8024,8030,8031,9518,9519,10093,10095,10096,10098,10099,10335]
        case "hw":
            ids_arr =  [4833,5159,5160,5163,5226,5392,12536,12538,12540,12587,12634,12877,12882,12884,12889,12896,12897,12898,12899,12900,12901,12902,12903,12904,12943,12944,12945,13765,13767,13768,14148,14151,14154,14957,15646,15647,16721,16722,16723,16724,16725,16726]
        case "sb":
            ids_arr =  [17944,17948,19853,19857,19860,19865,19907,19918,19934,19958,19959,19968,19970,19971,19972,19973,19991,21085,21086,22417,22418,22419,22420,23179,23180,24240,24241,24242,24243,24255]
        case "shb":
            ids_arr =  [27688,27704,27705,27726,27727,27728,27729,27730,27731,27761,27822,27828,27833,27835,27836,28716,28717,29968,29970,29972,29974,29976,29978,30485,30486,32950,32951,32952,32953,32954,32955]
        case "ew":
            ids_arr =  [36167,36179,36195,36207,36214,36215,36217,37278,37279,37691,37694,37817,37818,37819,37820,37821,37822,38933,38934,39705,39706,39707,39708,39709,39710]
        case "dt":
            ids_arr =  [44135,44136,44137,44138,44139,44140]
    #ids = ','.join(str(element) for element in ids_arr)
    itemIds.append(ids_arr)
    url = f"?listings=1&entries=0"
    item_list.extend(get_item_list(url,ids_arr, 800,"minPrice"))


def dt_craft_items():
    ids_arr = []
    while counter < endId:
        for i in range(100):
            if counter < endId:
                itemIds.append(counter)
            counter += 1
        

        #ids = ','.join(str(element) for element in itemIds)
        print(itemIds)
        url = f"https://universalis.app/api/v2/Light/{itemIds}?listings=1&entries=0&hq=true"
        item_list.append(get_item_list(url,ids_arr,70000,"minPriceHQ"))
        itemIds.clear()
        
        # print(url)

        # # Make a GET request to the API
        # response = requests.get(url)

        # # Check if the request was successful
        # if response.status_code == 200:
        #     # Parse the JSON response
        #     data = response.json()
            
        #     # Extract the items
        #     items = data.get("items", {})
        #     #print(items)
        #     # Iterate over the items and print the currentAveragePriceHQ
        #     for item_id in itemIds:
        #         item = items.get(str(item_id), {})
        #         min_Price_HQ = item.get("minPriceHQ", None)
        #         if min_Price_HQ != None and min_Price_HQ > 70000:
        #             item_list.append((item_id, min_Price_HQ))
        # else:
        #     print(f"Failed to fetch data. Status code: {response.status_code}")

        # time.sleep(1)
        # itemIds.clear()

#dt_craft_items()
timed_node_Ids("arr")
timed_node_Ids("hw")
timed_node_Ids("sb")
timed_node_Ids("shb")

# xivapiUrl = "https://xivapi.com/item?ids="
# for item_id, min_Price_HQ in item_list:
#     xivapiUrl += str(item_id) + ','

# my_list = []

# response = requests.get(xivapiUrl)
# if response.status_code == 200:
#     data = response.json()

#     results = data.get("Results", {})
    
    
#     for result in results:
#         #print(result)
#         for item in item_list:
#             if item[0] == result["ID"]:
#                 my_list.append((result["Name"], item[1], item[0]))

#print(my_list)



sorted_items = sorted(get_names(), key=lambda x: x[1])
for name, min_Price_HQ, id in sorted_items:
    print(f"{min_Price_HQ} - {id} - {name} ")