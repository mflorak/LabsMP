import requests

BASE_URL = 'http://127.0.0.1:5001/items'
AUTH = ('admin', 'password123')

def log(action, response):
    print(f"\n--- {action} ---")
    print(f"Status: {response.status_code}")
    try:
        print(f"Body: {response.json()}")
    except:
        print(f"Body: {response.text}")

resp = requests.get(BASE_URL)
log("GET ALL ITEMS", resp)

new_item = {
    "id": 555,
    "name": "Gaming Mouse",
    "price": 49.99,
    "size": "Medium",
    "color": "Black",
    "weight": 0.150
}
resp = requests.post(BASE_URL, json=new_item, auth=AUTH)
log("POST (Create Item)", resp)

resp = requests.get(f"{BASE_URL}/555")
log("GET ITEM 555", resp)

update_data = {"price": 39.99, "color": "Red"}
resp = requests.put(f"{BASE_URL}/555", json=update_data, auth=AUTH)
log("PUT (Update Item)", resp)

#resp = requests.delete(f"{BASE_URL}/555", auth=AUTH)
#log("DELETE (Remove Item)", resp)

resp = requests.get(BASE_URL)
log("GET ALL ITEMS (Final)", resp)