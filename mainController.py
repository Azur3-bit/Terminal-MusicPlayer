# user input For song 
# TODO Create a good Greet Module

import urlGenerator
import requests
import os
from bs4 import BeautifulSoup

urlGenerator.Greet()
urlGenerator.user_songName()

# Generating First Url - Find Page 
urlFindPage = urlGenerator.url_generator_forFindPage()
# print(urlFindPage)

# ----------- Setting Server Connection -----------
import serverConnection
connection_findPage =  serverConnection.establishConnection()
serverConnection.connectionStatus(url=urlFindPage)
 
 
# ----------- Show Avilable Options - Song options -----------
from SongDivisonSelector import showAvailableSongList
SelectedSong_url_main = showAvailableSongList()
print("Url Of Selected Song : ",SelectedSong_url_main) 


def saveBinaryAudio(songName_tobeSaved):
    with open(songName_tobeSaved,"wb") as BinaryAudio:
        BinaryAudio.write(donwload_reqLink.content)
        print("Downloaded : ",songName_tobeSaved)
        # print("File Saved : ",current_dir)

albumCheck = SelectedSong_url_main[1:6]
if(albumCheck == "album"):
    # Pass Request and store data in a list 
    
    SelectedSong_url_main = "https://pagalnew.com"+SelectedSong_url_main
    # print(" ---&&&------&&&------&&&------&&&------&&&--- ")
    # print(SelectedSong_url_main)
    from pagalNewAlbumSong import getSongNameList
    songName_list_mainController = getSongNameList(SelectedSong_url_main)
    # print(songName_list_mainController) 
    # print(" ---&&&------&&&------&&&------&&&------&&&--- ")
    songs_download = []
    req = requests.get(SelectedSong_url_main)
    # print(req.content)

    # ------ creating Soup Object ------
    soup = BeautifulSoup(req.content, "html5lib")
    # print(soup.prettify())

    # ------ getting all the Donwloadable Object ------

    songs = soup.find_all(class_="main_page_category_music")
    # print(songs)

    for it in songs:
        print("-----")
        anchorTag = it.a
        hrefElement = anchorTag.get("href")
        # print(hrefElement)
        songs_download.append(hrefElement)

    
    from SongDivisonSelector import songName
    folderName = songName()
    try:
        os.mkdir(folderName)
        print("Directory Created ")
        os.chdir(os.path.join(folderName))
    except FileExistsError:
        print("Directory Already Exists ! ")
        os.chdir(os.path.join(folderName))
        
    current_dir = os.getcwd()
    # print("Directory Changed to : ",current_dir)
    print(songName)
    i = 0
    for current_url in songs_download:
        # download each song one by one
        folderName = songName_list_mainController[i]
        i += 1
        fileName = folderName+".mp3"
        songName = folderName+".mp3"
        req = requests.get(url=current_url)
        soup = BeautifulSoup(req.content,"html5lib")
        # print(soup.prettify())
# getting Song Name <START>  .. .
        # Selecting Donwload Button 
        download_button = soup.find_all(class_ = "dbutton")[1]
        # print(download_button)
        # generting Href 
        href = download_button.get("href")
        # print(href)
        downloadLink = "https://pagalnew.com/" + href
        print("downloadLink : ",downloadLink)

        # Downloading songs 
        donwload_reqLink = requests.get(downloadLink)

        # Getting Folder Name 
        current_dir = os.getcwd()
        # print(current_dir)
        songName = os.path.join(current_dir,songName)
        saveBinaryAudio(songName_tobeSaved=songName)
    
# getting Song Name END <END>...


else:
    print("Inside ELse Block ")
    # print(SelectedSong_url_main)
    preLink = "https://pagalnew.com"
    actualLink = preLink+SelectedSong_url_main
    req = requests.get(actualLink)
    soup = BeautifulSoup(req.content,"html5lib")
    downloadButton = soup.find_all(class_ = "dbutton")[1]
    # getting Href 
    hrefLink = downloadButton.get("href")
    href = preLink+hrefLink
    donwload_reqLink = requests.get(href)
    # print(type(hrefLink))
    songName = soup.find(class_ = "up")
    songName = songName.string
    songName = songName+".mp3"
    curr_dir = os.getcwd()
    curr_dir = os.path.join(curr_dir,songName)
    saveBinaryAudio(curr_dir)
    
    