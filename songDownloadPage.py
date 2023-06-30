# Song Download Page

import requests
from serverConnection import establishConnection
from bs4 import BeautifulSoup
from SongDivisonSelector import songName
import os
from SongDivisonSelector import selectedSong_url_funtion

user_reqUrl = selectedSong_url_funtion()
# print(user_reqUrl)
req = requests.get(url=user_reqUrl)
# print(req.content)

soup = BeautifulSoup(req.content,"html5lib")
# print(soup.prettify())

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
folderName = songName()
# current_path = os.curdir()
# print("Current Dir : ", current_path)
os.mkdir(folderName)
print("Directory Created ")
os.chdir(os.path.join(folderName))
current_dir = os.getcwd()
# print("Directory Changed to : ",current_dir)

fileName = folderName+".mp3"

def saveBinaryAudio():
    with open(fileName,"wb") as BinaryAudio:
        BinaryAudio.write(donwload_reqLink.content)
        print("File Saved : ",current_dir)

saveBinaryAudio()