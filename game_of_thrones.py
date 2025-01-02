import requests
url =  "https://thronesapi.com/api/v2/characters"
response = requests.get(url)
if response.status_code == 200:
    characters = response.json()
    for x in characters[:53]:
        first_name = x.get("firstName", "N/A")
       last_name = x.get("lastName","N/A")
       title = x.get("title", "N/A")
       family = x.get("family", "N/A")
       img_url = x.get("imageUrl","N/A")
       print(f'first name and last name:{first_name} {last_name}')
       print(f'title: {title}')
       print(f'family: {family}')
       print(f"face:{img_url}")
       print("-"*20) #this prints a line in your code
       
else:
     print("failed to retrieve data")
