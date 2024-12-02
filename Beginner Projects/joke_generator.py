# Code Created By @Dypixx....

import requests
def fetch_random_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    try:
        response = requests.get(url)
        if response.status_code == 200:  # Check if the request was successful
            joke_data = response.json()
            if joke_data["type"] == "single":
                print(f"Here's a joke for you: {joke_data['joke']}")
            else:
                print(f"{joke_data['setup']} ... {joke_data['delivery']}")
        else:
            print(f"Oops! Couldn't fetch a joke. (Status Code: {
                  response.status_code})")
    except Exception as e:
        print(f"Yikes! Something went wrong: {e}")


# Call the function
fetch_random_joke()
