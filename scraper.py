from bs4 import BeautifulSoup
import requests

# step1 : prompt the user for the url to scrap
url = input("Enter the url of the website you want to scrape :")
tags = input("Enter the tags you want to extract comma seperated. Ex : h1 , p , a : ")

#create tag array separated by commas
tag_list = [tag.strip() for tag in tags.split(",")]
print(tag_list)

#step 2 : handling the requests (we sent a requewst get a response back)
try:
    response = requests.get(url)#getting the response back
    response.raise_for_status() # raises status for non 200 responses

    #step 3 : transform the response into  a BeautifulSoup object 
    soup= BeautifulSoup(response.text ,'html.parser')
   
    # iterate through the tag list/array to find the matching tags in the site
    for tag in tag_list:
        match = soup.find_all(tag)
    print(f"Found {len(match)} number of {tag} elements :")
    #printing the elements
    for element in match:
        print(element.get_text())
except requests.exceptions.RequestException as e:
    # Handle any request-related error (connection, timeout, invalid URL, etc.)
    print(f"An error occurred: {e}")
