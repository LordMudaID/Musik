import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "BadPeople Musik")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "LordMuda_ID")
ALIVE_NAME = getenv("ALIVE_NAME", "LordMuda")
BOT_USERNAME = getenv("BOT_USERNAME", "BadPeopleMusikBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "badpeopleassistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "BadHumanReborn")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "AsupanBadHumanReborn")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/643662c5551323d52e37f.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/LordMudaID/musikvideostream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/f486ab5efc63276e7ce8c.jpg")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/60780dd21e270007b4809.jpg")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/a34251372e7c0ebdb09ec.jpg")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/de6640d56acd9eee6eaa7.jpg")
