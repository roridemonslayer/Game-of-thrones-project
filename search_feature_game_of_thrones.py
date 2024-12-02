import requests
#this query funtion is a parameter used to call back the function. 
#use def when u wanna use api to search sum in your python
def search_character(query):
    url = f"https://thronesapi.com/api/v2/characters"
    response = requests.get(url)

    if response.status_code == 200:
        characters = response.json()

        for character in characters:
            # Search for character name matching query
            if query.lower() in character["firstName"].lower() or query.lower() in character["lastName"].lower() or query.lower() in character["title"].lower():
                print(f'Name: {character["firstName"]} {character["lastName"]}')
                print(f'Title: {character["title"]}')
                print(f'Family: {character["family"]}')
                print(f'Image URL:{character["imageUrl"]}')
                print("-" * 20)
    else:
        print("Failed to retrieve data")

search_query = input("Enter a character name or family to search: ")
search_character(search_query)
