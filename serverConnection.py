# Server Connection

from urlGenerator import url_generator_forFindPage
import requests

print(" -- Inside Section Selector -- ")

# final URL
user_url = url_generator_forFindPage()
print(user_url)


# Establishing Connection
def establishConnection():
    request = requests.get(user_url)
    # print(request)
    return request


def connectionStatus(url):
    requestStatus = establishConnection()
    stirng_requestStatus = str(requestStatus)
    print(f"SERVER Response Code {stirng_requestStatus}")

    if ("20" in stirng_requestStatus):
        print("\n<STATUS> - Connection Established to the server ... ")
    else:
        print("\nConnection Failed")
