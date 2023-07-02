
# Neccesaary Imports
# - 3 total
# import requests
# from bs4 import BeautifulSoup
# import os

# Auxiliary Imports
# - None

# personal Comments

# ? TODO - move To next page

print(" -- Inside  URL Generator -- ")


principal_url = "https://pagalnew.com/"
supplemenrty_url = "search.php?find="

# Greet


def Greet():
    
    print("\t\t\t----------------------------------")
    print("\t\t\tWelcome to Song Downloader - azur3")
    print("\t\t\t----------------------------------")


# Funtion to get Name of the song
def user_songName():
    global song_name
    global manipulated_user_songName
    # song_name = "Bloody Daddy"
    song_name = input("Enter Song Name : ")
    manipulated_user_songName = song_name.replace(" ", "+")
    # print(f"Entered song Name - {song_name}")
    # print(f"Mainpulated song Name - {manipulated_user_songName}")



def url_generator_forFindPage():
    # global final_url
    final_url = principal_url+supplemenrty_url+manipulated_user_songName
    # print(f"url - {final_url}")
    return final_url
