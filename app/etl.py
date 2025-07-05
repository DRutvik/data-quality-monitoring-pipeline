import pandas as pd
import requests

def fetch_data():
    url = "https://api.covidtracking.com/v1/states/current.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)
        df.to_csv("data.csv", index=False)
        print("✅ Data saved to data.csv")
    else:
        print(f"❌ Failed to fetch data. Status code: {response.status_code}")

if __name__ == "__main__":
    fetch_data()