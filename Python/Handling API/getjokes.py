import requests

def fetch_jokes():
    url="https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
    response=requests.get(url)
    data=response.json()

    if data["success"] and "data" in data:
       joke=data["data"]["data"][0]
       content=joke["content"]
       id=joke["id"]
       return content,id
    else:
       raise Exception("Failed to fetch data") 

def main():
    try:
        content,id=fetch_jokes()
        print(f"ID: {id}") 
        print(f"JOKE: {content}")
    except Exception as e:
        # Print the error message if something goes wrong
        print(str(e))

if __name__=="__main__":
    main()

