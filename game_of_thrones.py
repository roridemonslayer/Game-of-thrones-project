#okay so here were going to actually request data from the API and stuff 
# were going to use the thrones API 
# we will need to use the GET request which basiclly allows us to ask if we can get data from an API
#with imporat were telling python to import requests(a popular tool for making HTTP requets in python)
import requests
#this url is where we want to get our data from  when we use the import function
url =  "https://thronesapi.com/api/v2/characters"
#  u use the request.get() method when you want to get request to use DATA from a specifc URL
response = requests.get(url)
# what this does is that it checks the status code of application 
#200 meants its solid and it wa way for the server to tell us if the requests was sucessful 
#just for me, anything ur use api just use the vairble reponse so u can get the status code easier

if response.status_code == 200:
    #what this does is take the raw data from the api and just basically put it into a python way of looking weather it be through a list or discitoanry
    #This make data easier to work with so use the response.json() function work and access data 
    characters = response.json()
    #what were saying here is that we want the computer to loop back 5 times to get 5 characeters
    #its important so that the api will return list
    for x in characters[:53]:
        #this just prints out name in a list in out API
        #character is the varible referts to the character dictionary 
        #the ['name'] key is to access the characters name in the list
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