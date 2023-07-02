# user input For song 
# TODO Create a good Greet Module

import urlGenerator
import requests
import os
from bs4 import BeautifulSoup
urlGenerator.Greet()
urlGenerator.user_songName()
urlFindPage = urlGenerator.url_generator_forFindPage()
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
    SelectedSong_url_main = "https://pagalnew.com"+SelectedSong_url_main
    from pagalNewAlbumSong import getSongNameList
    songName_list_mainController = getSongNameList(SelectedSong_url_main)
    songs_download = []
    req = requests.get(SelectedSong_url_main)
    soup = BeautifulSoup(req.content, "html5lib")
    # ------ getting all the Donwloadable Object ------
    songs = soup.find_all(class_="main_page_category_music")
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
    print(songName)
    i = 0
    for current_url in songs_download:
        folderName = songName_list_mainController[i]
        i += 1
        fileName = folderName+".mp3"
        songName = folderName+".mp3"
        req = requests.get(url=current_url)
        soup = BeautifulSoup(req.content,"html5lib")
        download_button = soup.find_all(class_ = "dbutton")[1]
        href = download_button.get("href")
        downloadLink = "https://pagalnew.com/" + href
        print("downloadLink : ",downloadLink)
        donwload_reqLink = requests.get(downloadLink)
        current_dir = os.getcwd()
        songName = os.path.join(current_dir,songName)
        saveBinaryAudio(songName_tobeSaved=songName)


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
    
    