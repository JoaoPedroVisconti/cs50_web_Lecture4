import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key=a15a02da3e9efc08debdc155fe36aee9&format=1")
    
    if res.status_code != 200:
        # Just saying to quit the program if something goes wrong
        raise Exception("ERROR: API request unsuccessful")
    
    # Taking the result of the request and extract that JSON data
    # and saving in a variable call data.
    data = res.json()
    
    print(data)
    
if __name__ == "__main__":
    main()
    
