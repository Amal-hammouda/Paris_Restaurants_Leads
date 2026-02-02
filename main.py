import requests
import pandas as pd
import time

API_KEY = "Your_API_Key"
restaurants = []
target_total = 100  # El-hadaf mte3na

for start_index in range(0, target_total, 20):
    print(f"🔄 Jari jam3 el-xatit mte3 el-restaurants (men {start_index} l-{start_index + 20})...")

    params = {
        "engine": "google_maps",
        "q": "restaurants in Paris",
        "type": "search",
        "api_key": API_KEY,
        "start": start_index  # Hatha elli ykhallina n9allbou el-safhat
    }

    response = requests.get("https://serpapi.com/search.json", params=params)
    data = response.json()

    results = data.get("local_results", [])

    if not results:
        print("⚠️ Mafamach nata'ij okhra.")
        break

    for place in results:
        restaurant = {
            "Name": place.get("title"),
            "Address": place.get("address"),
            "Phone": place.get("phone"),
            "Website": place.get("website"),
            "Rating": place.get("rating"),
            "Google Maps Link": f"https://www.google.com/maps/place/?q=place_id:{place.get('place_id')}"
        }
        restaurants.append(restaurant)

    # Nestannao chwaya bech SerpApi ma ta3melnech block
    time.sleep(1)

# 1. Convert to DataFrame
df = pd.DataFrame(restaurants)

# 2. Save to CSV
df.to_csv("paris_restaurants_leads.csv", index=False, encoding="utf-8-sig")

# 3. Save to Excel
# NOTE: Lezem tseb el-maktaba hathi: pip install openpyxl
df.to_excel("paris_restaurants_leads.xlsx", index=False)

print("-" * 30)
print(f"✅ Mabrouk! El-fichie el-Excel w el-CSV tkhl7ou.")
print(f"📊 El-majmmou3: {len(df)} restaurant.")