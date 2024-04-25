
#Mars Photo Viewer
#The following code will return photos from Mars taken from NASAs Curiosity, Opportunity, and Spirit rovers

#Visit this page for the API calls from NASA. Browse APIs, then select Mars Rover Photos
#https://api.nasa.gov/

#in the space below, create your code that reaches the desired outcome. You may use old code of yours to accomplish this task as you see fit

#YOU MAY NOT USE MORE THAN 35 LINES OF CODE. COMMENTS AND BLANK LINES DO NOT COUNT TOWARDS THIS REQUIRMENT
#YOU MUST HAVE AT LEAST 1 COMMENT LINE FOR EVERY 4 LINES OF CODE

#IMPORTS
import requests
from PIL import Image
from io import BytesIO

def fetch_pic(base_url, api_key):
    #concatenate a url with the base_url, your api key, and the extra parameters for the desired date
    #This is the format your url request should be:
    #https://api.nasa.gov/planetary/apod?api_key=YOUR_API_KEY&date=YYYY-MM-DD
    url = base_url+api_key
    print(url)
    response = requests.get(url)
    rover_data = response.json()
    return rover_data

#base_url is the beginning of the url that we will go to for our APOD
base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&page=2&api_key="
#below, paste your NASA API Key.
api_key = "npE0I9YUgP2MrggW2aYD1buK6ntPJhsJObu6ZVea"
pic_data = fetch_pic(base_url, api_key)

#if the response we get back has a 'url'...
if 'url' in pic_data:
    print("Title:", pic_data['title'])
    print("Date:", pic_data['date'])
    print("Explanation:", pic_data['explanation'])
    print("HD URL:", pic_data.get('hdurl', "Not available"))
    print("URL:", pic_data['url'])

    # Open and display the image
    response = requests.get(pic_data['url'])
    image = Image.open(BytesIO(response.content))
    image.show()
#otherwise, if it did not have a url...
else:
    print("Error:", pic_data.get('msg', 'Unknown error'))

