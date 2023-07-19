import requests
import codecs
import random
import os
os.system("")
def download_with_progress(url):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    file_name = url.split('/')[-1]
    file_size = int(response.headers.get('content-length', 0))
    chunk_size = 8192
    downloaded_size = 0
    print("\033[1;34;40m","Downloading: " + file_name,"\033[0m")
    print("\033[1;32;40m","Size: " + str(file_size // 1024 // 1024) + " MB","\033[0m")
    with open(file_name, "wb") as file:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                file.write(chunk)
                downloaded_size += len(chunk)
                progress = int(downloaded_size / file_size * 100)
                print("\033[1;"+str(random.randint(31,37))+";40m",f"Download progress: {progress}%","\033[0m", end="\r")
    return file_name

print("\033[1;36;40m","""
 █████╗ ██╗      █████╗  █████╗ ████████╗██╗   ██╗    ██████╗  ██████╗ ██╗    ██╗███╗   ██╗██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██║     ██╔══██╗██╔══██╗╚══██╔══╝██║   ██║    ██╔══██╗██╔═══██╗██║    ██║████╗  ██║██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
███████║██║     ███████║███████║   ██║   ██║   ██║    ██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝
██╔══██║██║     ██╔══██║██╔══██║   ██║   ╚██╗ ██╔╝    ██║  ██║██║   ██║██║███╗██║██║╚██╗██║██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗
██║  ██║███████╗██║  ██║██║  ██║   ██║    ╚████╔╝     ██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝     ╚═══╝      ╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

Github : ""","\033[0m")
link = input("\033[1;32;40mYour link AlaaTV : \033[0m",)
if link.startswith("https://alaatv.com/"):
    print("\033[1;31;40m","Loading .","\033[0m",end="\r")
    req = requests.get(link,stream=True,allow_redirects=True)
    print("\033[1;33;40m","Loading ..","\033[0m", end="\r")
    all = []
    if req.reason == "OK":
        print("\033[1;37;40m","Loading ...","\033[0m", end="\r")
        r = req.text
        for i in r.split('{"video":[{"link":"'):
            rs = i.split('",')[0]
            if rs.startswith("https:"):
                all.append(codecs.decode(rs, 'unicode-escape'))
        for i in r.split('"src":"'):
            rs = i.split('",')[0]
            if rs.startswith("https:"):
                all.append(codecs.decode(rs, 'unicode-escape'))
        all = list(set(all))
        print("\033[1;35;40m","1 - 1080p","   link :",all[0],"\033[0m")
        print("\033[1;35;40m","2 - 720p","    link :",all[1],"\033[0m")
        print("\033[1;35;40m","3 - 480p","    link :",all[2],"\033[0m")
        als = input("\033[1;33;40m select number to download: \033[0m")
        if als.isdigit():
            if als in ["1","2","3"]:
                download_with_progress(all[int(als)-1])
            else:
                exit("You did not select the correct option.")
        else:
            exit("Error in retrieving data from the website.")
    else:
        exit("Error: The link is not related to alaatv.com.")