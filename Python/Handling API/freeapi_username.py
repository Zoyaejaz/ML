import requests

def fetch_random_user_freeapi():
    url="https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data=response.json()

    if data["success"] and "data" in data:
        user_data=data["data"]
        username=user_data["login"]["username"]
        country=user_data["location"]["country"]
        return username,country
    else:
        raise Exception("Failed to fetch user data")

def main():
    try:
        username,country=fetch_random_user_freeapi()
        print(f"Username: {username} \n Country:  {country}")
    except Exception as e:
        print(str(e))

if __name__=="__main__":
    main()
#if __name__ == "__main__": main() means “run the main() function only when this Python file is executed directly.” Python gives every file a special variable called __name__; when you run the file directly, its value becomes "__main__", so the condition becomes true and main() runs. But if another Python file imports this file, __name__ will be the file's name instead of "__main__", so main() will not run automatically. This is mainly used to prevent the main program from starting automatically when the file is imported into another program.
