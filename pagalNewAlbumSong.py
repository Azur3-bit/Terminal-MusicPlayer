# Getting Song Name - pagal new album Song Page - 2023

import requests
from bs4 import BeautifulSoup
songName_lst = []
def getSongNameList(user_url):
    # user_url = url
    req = requests.get(url=user_url)
    # print(req.content)
    soup = BeautifulSoup(req.content,"html5lib")
    # print(soup.prettify())
    songName = soup.find(class_ = "main_page_category_music_txt")
    numberOfSongName = soup.find_all(class_ = "main_page_category_music_txt")
    # numberOfSongName = soup.find_all(class_ = "main_page_category_music_txt")
    numberOfSongName = len(numberOfSongName)
    print(numberOfSongName)
    # print(songName)
    for i in range(0,numberOfSongName):
        songName = soup.find_all(class_ = "main_page_category_music_txt")[i]
        # print(songName)
        songName_string = str(songName)
        songName_string_index_start = songName_string.find('<div style="color:#000000; font-weight:700;">')
        songName_string = songName_string[songName_string_index_start:]
        songName_string_EndIndex = songName_string.find("</div>")
        songName_string = songName_string[songName_string_index_start:songName_string_EndIndex]
        # print(songName_string)
        songName_string = songName_string.replace("\t"," ")
        songName_lst.append(songName_string.strip())
    return songName_lst        
    # print(songName_lst)
