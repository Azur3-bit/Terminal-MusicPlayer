# SongDivisonSelector

from serverConnection import establishConnection
from bs4 import BeautifulSoup
import requests

print("-- Inside Song Division selector Module -- ")

connection = establishConnection()
# print(connection.content)

# Creating Soup Object

soup = BeautifulSoup(connection.content, "html5lib")
# print(soup.prettify())

searchedResult = soup.find_all(class_="main_page_category_music_box")
# print(searchedResult)

songName_list = []
links_list = []

for it in searchedResult:
    # print(it)
    bTag = it.find("b")
    # print(bTag)
    bTag_stringConversion = str(bTag)
    # slicing
    bTag_stringConversion = bTag_stringConversion[8:-9]
    bTag_stringConversion = bTag_stringConversion.strip()
    songName_list.append(bTag_stringConversion)



# Links
for it in searchedResult:
    album = it.a
    href_current = album.get("href")
    links_list.append(href_current)

# songSelection
def SongSelection(user_selectedSong):
    link = links_list[user_selectedSong]
    # print(link)
    return link

# print(songName_list)


def showAvailableSongList():
    i = 1
    print("\n ... List of Avialable Songs ... \n")
    for it in songName_list:
        # print(z)
        print("-------------------")
        print(f"{i}. --- {it}")
        # print("-------------------")
        str_it = str(it)
        # print(len(str_it))
        i = i+1
        # totalNumberOfSongs += totalNumberOfSongs
    print(f"found {i-1} songs ")
    global userSelection
    userSelection = int(input("Enter Your Choice : "))
    userSelection = userSelection-1
    global selectedSong_url
    selectedSong_url = SongSelection(userSelection)
    return selectedSong_url
    


# Return Song Name 
def songName():
    return songName_list[userSelection]

# Return Selected Song U


# def recursiveCallRequired():
#     if(song[1:6] == "album"):
#         return True
#     else:
#         return False
    

# if (song[1:6] == "album"):
#     selected_songUrl = selectedSong_url_funtion()
#     # print(url)
#     # Completing Url
#     principal_url = "https://pagalnew.com/"
#     selected_songUrl = principal_url+selected_songUrl
#     req = requests.get(selected_songUrl)
#     # print(req.content)
#     # ------ creating Soup Object ------
#     soup = BeautifulSoup(req.content, "html5lib")
#     # print(soup.prettify())
#     # ------ getting all the Donwloadable Object ------
#     songs_download = []
#     songs = soup.find_all(class_="main_page_category_music")
#     # print(songs)

#     for it in songs:
#         print("-----")
#         anchorTag = it.a
#         hrefElement = anchorTag.get("href")
#         print(hrefElement)
#         # songs_download.append(hrefElement)

