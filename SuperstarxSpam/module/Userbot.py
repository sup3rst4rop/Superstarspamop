
# Superstar - Telegram Projects
# (c) 2022 - 2023 Star
# Don't Kang Bitch -!


import os
import sys
import asyncio
import datetime
import time
from Superstarxspam import (HNDLR, SUDO_USERS, ALIVE_PIC, ALIVE_MSG, PING_MSG, __version__, start_time)
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram import __version__ as pyro_vr             
                

pongg = PING_MSG if PING_MSG else "SUPERSTAR X SPAM"
SUP_PIC = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/50cea9231fabf384c09e9.jpg"
Alivemsg = ALIVE_MSG if ALIVE_MSG else "SUPERSTAR X SPAM HERE."


Superstarxspam = f"⁂ {Alivemsg} ⁂\n\n"
Superstarxspam += f"━───────╯•╰───────━\n"
Superstarxspam += f"➠ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.10.4`\n"
Superstarxspam += f"➠ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ** : `{pyro_vr}`\n"
Superstarxspam += f"➠ **Superstarxspam version**  : `{__version__}`\n"
Superstarxspam += f"➠ **ᴄʜᴀɴɴᴇʟ** : [Join.](https://t.me/tsf_brand)\n"
Superstarxspam += f"━───────╮•╭───────━\n\n"
Superstarxspam += f"➠ **Source Code:** [•Repo•](https://github.com/sup3rst4rop/Superstarspamop)"


async def get_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    hmm = len(time_list)
    for x in range(hmm):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "
    time_list.reverse()
    up_time += ":".join(time_list)
    return up_time


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["ping"], prefixes=HNDLR))
async def ping(_, e: Message):       
      start = datetime.datetime.now()
      uptime = await get_time((time.time() - start_time))
      Fuk = await e.reply("**Pong !!**")
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 1000
      await Fuk.edit_text(f"⌾ {pongg} ⌾ \n\n ༝ ᴘɪɴɢ: `{ms}` ᴍs \n ༝ ᴜᴘᴛɪᴍᴇ: `{uptime}` \n ༝ ᴠᴇʀsɪᴏɴ: `{__version__}`")



@Client.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["alive"], prefixes=HNDLR))
async def alive(Superstarxspam: Client, e: Message):
       if ".jpg" in SUP_PIC or ".png" in SUP_PIC:
              await Superstarxspam.send_photo(e.chat.id, SUP_PIC, caption=Superstarxspam)
       if ".mp4" in SUP_PIC or ".MP4," in SUP_PIC:
              await Superstarxspam.send_video(e.chat.id, SUP_PIC, caption=Superstarxspam)



@Client.on_message(filters.user(SUDO_USERS) & filters.command(["restart", "reboot"], prefixes=HNDLR))
@Client.on_message(filters.me & filters.command(["restart", "reboot"], prefixes=HNDLR))
async def reboot(Superstarxspam: Client, e: Message):
        reboot_text = "**Re-starting** \n\n __Wait For A While To Use it Again__ "
        await e.reply_text(reboot_text)
        try:
            Superstarxspam.disconnect()
        except Exception as e:
            pass
        args = [sys.executable, "-m", "Superstarxspam"]
        os.execl(sys.executable, *args)
        quit()

            
