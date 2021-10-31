#  Copyright (C) 2020  @Copyless786(π.$)
# credits to @Simpleboy786 (@SimpleBoy786)
import asyncio
import os
import re

from userbot import lionub

from ..funcs.managers import edit_delete, edit_or_reply
from ..helpers.utils import reply_id
from . import (
    changemymind,
    deEmojify,
    fakegs,
    kannagen,
    moditweet,
    reply_id,
    trumptweet,
    tweets,
)

plugin_category = "fun"


@lionub.lion_cmd(
    pattern="fakegs(?:\s|$)([\s\S]*)",
    command=("fakegs", plugin_category),
    info={
        "header": "Fake google search meme",
        "usage": "{tr}fakegs search query ; what you mean text",
        "examples": "{tr}fakegs LionXub ; One of the Popular userbot",
    },
)
async def nekobot(lion):
    "Fake google search meme"
    text = lion.pattern_match.group(1)
    reply_to_id = await reply_id(lion)
    if not text:
        if lion.is_reply and not reply_to_id.media:
            text = reply_to_id.message
        else:
            return await edit_delete(lion, "`What should i search in google.`", 5)
    lionx = await edit_or_reply(lion, "`Connecting to https://www.google.com/ ...`")
    text = deEmojify(text)
    if ";" in text:
        search, result = text.split(";")
    else:
        await edit_delete(
            lion,
            "__How should i create meme follow the syntax as show__ `.fakegs top text ; bottom text`",
            5,
        )
        return
    lionfile = await fakegs(search, result)
    await asyncio.sleep(2)
    await lion.client.send_file(lion.chat_id, lionfile, reply_to=reply_to_id)
    await lionx.delete()
    if os.path.exists(lionfile):
        os.remove(lionfile)


@lionub.lion_cmd(
    pattern="trump(?:\s|$)([\s\S]*)",
    command=("trump", plugin_category),
    info={
        "header": "trump tweet sticker with given custom text",
        "usage": "{tr}trump <text>",
        "examples": "{tr}trump LionXub is One of the Popular userbot",
    },
)
async def nekobot(lion):
    "trump tweet sticker with given custom text_"
    text = lion.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lion)

    reply = await lion.get_reply_message()
    if not text:
        if lion.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(lion, "**Trump : **`What should I tweet`", 5)
    lionx = await edit_or_reply(lion, "`Requesting trump to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    lionfile = await trumptweet(text)
    await lion.client.send_file(lion.chat_id, lionfile, reply_to=reply_to_id)
    await lionx.delete()
    if os.path.exists(lionfile):
        os.remove(lionfile)


@lionub.lion_cmd(
    pattern="modi(?:\s|$)([\s\S]*)",
    command=("modi", plugin_category),
    info={
        "header": "modi tweet sticker with given custom text",
        "usage": "{tr}modi <text>",
        "examples": "{tr}modi LionXub is One of the Popular userbot",
    },
)
async def nekobot(lion):
    "modi tweet sticker with given custom text"
    text = lion.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lion)

    reply = await lion.get_reply_message()
    if not text:
        if lion.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(lion, "**Modi : **`What should I tweet`", 5)
    lionx = await edit_or_reply(lion, "Requesting modi to tweet...")
    text = deEmojify(text)
    await asyncio.sleep(2)
    lionfile = await moditweet(text)
    await lion.client.send_file(lion.chat_id, lionfile, reply_to=reply_to_id)
    await lionx.delete()
    if os.path.exists(lionfile):
        os.remove(lionfile)


@lionub.lion_cmd(
    pattern="cmm(?:\s|$)([\s\S]*)",
    command=("cmm", plugin_category),
    info={
        "header": "Change my mind banner with given custom text",
        "usage": "{tr}cmm <text>",
        "examples": "{tr}cmm LionXub is One of the Popular userbot",
    },
)
async def nekobot(lion):
    text = lion.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lion)

    reply = await lion.get_reply_message()
    if not text:
        if lion.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(lion, "`Give text to write on banner, man`", 5)
    lionx = await edit_or_reply(lion, "`Your banner is under creation wait a sec...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    lionfile = await changemymind(text)
    await lion.client.send_file(lion.chat_id, lionfile, reply_to=reply_to_id)
    await lionx.delete()
    if os.path.exists(lionfile):
        os.remove(lionfile)


@lionub.lion_cmd(
    pattern="kanna(?:\s|$)([\s\S]*)",
    command=("kanna", plugin_category),
    info={
        "header": "kanna chan sticker with given custom text",
        "usage": "{tr}kanna text",
        "examples": "{tr}kanna LionXub is One of the Popular userbot",
    },
)
async def nekobot(lion):
    "kanna chan sticker with given custom text"
    text = lion.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lion)

    reply = await lion.get_reply_message()
    if not text:
        if lion.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(lion, "**Kanna : **`What should i show you`", 5)
    lionx = await edit_or_reply(lion, "`Kanna is writing your text...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    lionfile = await kannagen(text)
    await lion.client.send_file(lion.chat_id, lionfile, reply_to=reply_to_id)
    await lionx.delete()
    if os.path.exists(lionfile):
        os.remove(lionfile)


@lionub.lion_cmd(
    pattern="tweet(?:\s|$)([\s\S]*)",
    command=("tweet", plugin_category),
    info={
        "header": "The desired person tweet sticker with given custom text",
        "usage": "{tr}tweet <username> ; <text>",
        "examples": "{tr}tweet iamsrk ; LionXub is One of the Popular userbot",
    },
)
async def nekobot(lion):
    "The desired person tweet sticker with given custom text"
    text = lion.pattern_match.group(1)
    text = re.sub("&", "", text)
    reply_to_id = await reply_id(lion)

    reply = await lion.get_reply_message()
    if not text:
        if lion.is_reply and not reply.media:
            text = reply.message
        else:
            return await edit_delete(
                lion,
                "what should I tweet? Give some text and format must be like `.tweet username ; your text` ",
                5,
            )
    if ";" in text:
        username, text = text.split(";")
    else:
        await edit_delete(
            lion,
            "__what should I tweet? Give some text and format must be like__ `.tweet username ; your text`",
            5,
        )
        return
    lionx = await edit_or_reply(lion, f"`Requesting {username} to tweet...`")
    text = deEmojify(text)
    await asyncio.sleep(2)
    lionfile = await tweets(text, username)
    await lion.client.send_file(lion.chat_id, lionfile, reply_to=reply_to_id)
    await lionx.delete()
    if os.path.exists(lionfile):
        os.remove(lionfile)
