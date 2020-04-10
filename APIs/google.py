import requests

def main():
    
    # Make a GET request to a website
    res = requests.get("https://www.google.com/")
    print(res.text)
    
if __name__ == "__main__":
    main()