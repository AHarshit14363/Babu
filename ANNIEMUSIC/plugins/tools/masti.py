import random
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from ANNIEMUSIC import app
from config import SUPPORT_CHAT

BUTTON = InlineKeyboardMarkup([[InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url=SUPPORT_CHAT)]])

HOT = "https://graph.org/file/745ba3ff07c1270958588.mp4"
HORNY = "https://graph.org/file/eaa834a1cbfad29bd1fe4.mp4"
SMEXY = "https://graph.org/file/58da22eb737af2f8963e6.mp4"
LEZBIAN = "https://graph.org/file/ff258085cf31f5385db8a.mp4"
GAY = "https://graph.org/file/850290f1f974c5421ce54.mp4"
BIGBALL = "https://i.gifer.com/8ZUg.gif"
LANGD = "https://telegra.ph/file/423414459345bf18310f5.gif"
CUTIE = "https://graph.org/file/24375c6e54609c0e4621c.mp4"


@app.on_message(filters.command("horny"))
async def HORNY(_, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={user_id})"
    mm = random.randint(1, 100)
    SUCK = f"**🔥** {mention} **ɪꜱ** {mm}**% ʜᴏʀɴʏ!**"
    await e.reply(SUCK, buttons=BUTTON, file=HORNY)

@app.on_message(filters.command("hot"))
async def HOT(_, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={user_id})"
    mm = random.randint(1, 100)
    HOTIE = f"**🔥** {mention} **ɪꜱ** {mm}**% ʜᴏT!**"
    await e.reply(HOTIE, buttons=BUTTON, file=HOT)

@app.on_message(filters.command("sexy"))
async def SEMXY(_, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={user_id})"
    mm = random.randint(1, 100)
    ROPE = f"**🔥** {mention} **ɪꜱ** {mm}**% sᴇxʏ!**"
    await e.reply(ROPE, buttons=BUTTON, file=SEMXY)

@app.on_message(filters.command("gay"))
async def GAY(_, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={user_id})"
    mm = random.randint(1, 100)
    CHAKKA = f"**🍷** {mention} **ɪꜱ** {mm}**% ɢᴀʏ!**"
    await e.reply(CHAKKA, buttons=BUTTON, file=GAY)

@app.on_message(filters.command("lesbian"))
async def LEZBIAN(_, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={user_id})"
    mm = random.randint(1, 100)
    LEZBIAN = f"**💜** {mention} **ɪꜱ** {mm}**% ʟᴇᴢʙɪᴀɴ!**"
   await e.reply(HORNY, buttons=BUTTON, file=LEZBIAN)


@app.on_message(filters.command("boob"))
async def BIGBALL(_, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={user_id})"
    mm = random.randint(1, 100)
    DHOODH = f"**🍒** {mention}**'ꜱ ʙᴏᴏʙꜱ ꜱɪᴢᴇ ɪᴢ** {mm}**!**"
    await e.reply(DHODH, buttons=BUTTON, file=BIGBALL)

@app.on_message(filters.command("cock"))
async def LANGD(_, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={user_id})"
    mm = random.randint(1, 100)
    LAMBDA = f"**🍆** {mention}**'ꜱ ᴄᴏᴄᴋ ꜱɪᴢᴇ ɪᴢ** {mm}**ᴄᴍ**"
    await e.reply(LAMBDA, buttons=BUTTON, file=LANGD)

@app.on_message(filters.command("cute"))
async def CUTIE(_, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    mention = f"[{user_name}](tg://user?id={user_id})"
    mm = random.randint(1, 100)
    cutie = f"**🍑** {mention} {mm}**% ᴄᴜᴛᴇ**"
    await e.reply(cutie, buttons=BUTTON, file=CUTIE)
