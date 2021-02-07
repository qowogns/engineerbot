#-*- coding:utf-8 -*-

import discord
import asyncio
import urllib.request

if not discord.opus.is_loaded():
     discord.opus.load_opus('opus')

client = discord.Client()
client.run('token')

@client.event
async def on_ready():
    print("="*20)
    print(client.user.name)
    print('봇 작동 중') 
    print("="*20)

@client.event
async def on_message(message):
    if message.content.startswith("!영어듣기평가문제지"):
        await client.send_file(message.channel, "2017년 제1회 고1 영어듣기평가 문제-1.jpg")
