"""
RadioPlayer, Telegram Voice Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
import re
from youtube_dl import YoutubeDL

from dotenv import load_dotenv

if os.path.exists(".env"):
    load_dotenv(".env")

ydl_opts = {
    "geo-bypass": True,
    "nocheckcertificate": True
    }
ydl = YoutubeDL(ydl_opts)
links=[]
finalurl=""
STREAM=os.environ.get("STREAM_URL", "http://stream.zenolive.com/8wv4d8g4344tv")
regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
match = re.match(regex,STREAM)
if match:
    meta = ydl.extract_info(STREAM, download=False)
    formats = meta.get('formats', [meta])
    for f in formats:
        links.append(f['url'])
    finalurl=links[0]
else:
    finalurl=STREAM

class Config:
    ADMIN = os.environ.get("ADMINS", "691224603")
    ADMINS = [int(admin) if re.search('^\d+$', admin) else admin for admin in (ADMIN).split()]
    API_ID = int(os.environ.get("API_ID", "7706870"))
    CHAT = int(os.environ.get("CHAT", "-1001296119865"))
    LOG_GROUP=os.environ.get("LOG_GROUP", "")
    if LOG_GROUP:
        LOG_GROUP=int(LOG_GROUP)
    else:
        LOG_GROUP=None
    STREAM_URL=https://youtu.be/BxhDqNeTHKM
    ADMIN_ONLY=os.environ.get("ADMIN_ONLY", "N")
    REPLY_MESSAGE=os.environ.get("REPLY_MESSAGE", None)
    if REPLY_MESSAGE:
        REPLY_MESSAGE=REPLY_MESSAGE
    else:
        REPLY_MESSAGE=None
    EDIT_TITLE=os.environ.get("EDIT_TITLE", True)
    if EDIT_TITLE == "False":
        EDIT_TITLE=None
    RADIO_TITLE=os.environ.get("RADIO_TITLE", "Music 24/7 | Radio Mode")
    if RADIO_TITLE == "False":
        RADIO_TITLE=None
    DURATION_LIMIT=int(os.environ.get("MAXIMUM_DURATION", 100))
    DELAY = int(os.environ.get("DELAY", 10))
    API_HASH = os.environ.get("API_HASH", "6982374bef85e9953a1ee53a02e92991")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1937706744:AAF_YwZadKqoYg8g_OEgS_QVluOA5V2fuok") 
    SESSION = os.environ.get("SESSION_STRING", "AQA03Pr_MPQ0mbluAm9VP0ARBD0ZWO3sEWydW-rav6doq1OkH9yQrpmLn4fpbP7z6RZLxlT-NRaOZl2OSLG84G9uuZUxB-Z3sef5bMzttpiK8DUdxPznYPsSQ6k9Qe_P8cE3CMJSRqBaskltWD6tAhiKyyayTE8jgrdo8mMmdOn3A1nWpW82Xu2gFlFxfwcvu01kEOJlp2d-5-AMbUFP0YsR6aLTyuuJ9tDIWYcSfYP5QI3a60GLqCJAJiL1vSmiRCxlvxgMIWal-_Hace-K2c9laRRuhWCyVDyNqhpFaC2O5E0gAWVYiHfq4dCbKSrczBARAXhEc3SZ4o_vrTVLNmphckfQFwA")
    playlist=[]
    msg = {}

