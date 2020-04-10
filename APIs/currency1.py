import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key=a15a02da3e9efc08debdc155fe36aee9&format=1")
    
    if res.status_code != 200:
        raise Exception("Error: API request unsuccessful")
    
    data = res.json()
    # Extract information from the API
    rate = data["rates"]["BRL"]
    #* "rates" is the key
    
    print(f"1 EUR is equal to {rate} BRL")
    
if __name__ == "__main__":
    main()
    
