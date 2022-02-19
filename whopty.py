from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import sys
import requests
import threading
from pytube import YouTube
import re
import os
token=input("your token:")

def song(x):
    r=requests.get(f"https://www.youtube.com/results?search_query={x}")
    url=re.findall('\watch\?v=[A-Za-z0-9-_]+',r.text)
    print("https://www.youtube.com/"+url[0])
    yt = YouTube(str("https://www.youtube.com/"+url[0]))
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(filename=x)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    return new_file
def deletesong(arg):
    sleep(10)
    os.remove(r"{}".format(arg))
class SimpleEcho(WebSocket):
    def sendmsg(self,data):
        print("starting")
        filename,channel=str(data).split(":")
        filename=song(filename)
        files = {'file': (filename, open(filename, 'rb'), 'text/plain')}
        json={"content":"","type":0,"sticker_ids":[],"attachments":[{"id":"0","filename":filename}]}
        headers={"authorization": token}
        r = requests.post(url=f'https://discord.com/api/v9/channels/{channel}/messages',json=json,files=files,headers=headers)
        files['file'][1].close()
        os.remove(r"{}".format(filename))
        self.sendMessage(f'let sex=new Audio("{r.json()["attachments"][0]["url"]}");sex.play()')

    def handleMessage(self):
        self.sendmsg(self.data)


    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

server = SimpleWebSocketServer("127.0.0.1", 8080, SimpleEcho)
server.serveforever()
