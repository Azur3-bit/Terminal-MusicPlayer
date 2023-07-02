# album Page

# Request to that page for items
# select all the divisions with - main_page_category_music (class)
from SongDivisonSelector import selectedSong_url_funtion
import requests
from bs4 import BeautifulSoup
songs_download = []


def Album_pageFuntion(url):
    req = requests.get(selected_songUrl)
    # ------ creating Soup Object ------
    soup = BeautifulSoup(req.content, "html5lib")
    # ------ getting all the Donwloadable Object ------
    songs = soup.find_all(class_="main_page_category_music")

    for it in songs:
        print("-----")
        anchorTag = it.a
        hrefElement = anchorTag.get("href")
        songs_download.append(hrefElement)
