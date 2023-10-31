import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import filters

async def get_linok(message):
    if message.chat.username:
         link = f"https://t.me/{message.chat.username}/{message.message_id}"
    else:
         xf = str((message.chat.id))[4:]
         link = f"https://t.me/c/{xf}/{message.message_id}"
    return link

@app.on_message(
    command(["ايدن","المطور"])
    & ~filters.edited
)
async def zohary(client: Client, message: Message):
    usr = await client.get_users(1892491797)
    name = usr.first_name
    user = await client.get_chat(1892491797)
    Bio = user.bio
    async for photo in client.iter_profile_photos(1892491797, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""Dev | - [{usr.first_name}](https://t.me/{usr.username}) ⚡
                       
Dev | - @{usr.username} ⚡
                       
Bio  | - {Bio} ⚡   
                         
iD | - 1892491797 ⚡ """, 
reply_markup=InlineKeyboardMarkup(
          [              
            [          
              InlineKeyboardButton (name, url=f"https://t.me/{usr.username}")
            ],             
          ]                 
       )                     
    )                       
                    sender_id = message.from_user.id
                    zoharyus = f"@{usr.username}"
                    message_link = await Telegram.get_linok(message)
                    sender_name = message.from_user.first_name
                    invitelink = await client.export_chat_invite_link(message.chat.id)
                    await app.send_message(1892491797, f"مبرمجي العزيز {zoharyus}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name} \n\n لينك الماسدج : {message_link} \n\n لينك البار : {invitelink}")
                    if await is_on_off(config.LOG):
                           return await app.send_message(
                           config.LOG_GROUP_ID,
                           f"مبرمجي العزيز {zoharyus}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}",)
@app.on_message(
    command(["محمود ايدن"])
    & ~filters.edited
)
async def zohary(client: Client, message: Message):
    usr = await client.get_users(1892491797)
    name = usr.first_name
    user = await client.get_chat(1892491797)
    Bio = user.bio
    async for photo in client.iter_profile_photos(1892491797, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""Dev | - [{usr.first_name}](https://t.me/{usr.username}) ⚡
                       
 Dev | - @{usr.username} ⚡
                       
Bio | - {Bio}       ⚡
                         
iD | - 1892491797 ⚡""", 
reply_markup=InlineKeyboardMarkup(
          [              
            [          
              InlineKeyboardButton (name, url=f"https://t.me/{usr.username}")
            ],             
          ]                 
       )                     
    )                       
                    sender_id = message.from_user.id
                    zoharyus = f"@{usr.username}"
                    message_link = await Telegram.get_linok(message)
                    sender_name = message.from_user.first_name
                    invitelink = await client.export_chat_invite_link(message.chat.id)
                    await app.send_message(6199134030, f"مبرمجي العزيز {zoharyus}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name} \n\n لينك الماسدج : {message_link} \n\n لينك البار : {invitelink}")
                    if await is_on_off(config.LOG):
                           return await app.send_message(
                           config.LOG_GROUP_ID,
                           f"مبرمجي العزيز {zoharyus}\n\n الواد {message.from_user.mention} دا بينادي عليك \n\n الايدي بتاعه : {sender_id} \n\n اسمه : {sender_name}",)