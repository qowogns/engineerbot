import requests
from bs4 import BeautifulSoup
import discord
import os
from datetime import datetime
import asyncio

client = discord.Client()
token = "ODA3MjQ5MjQwOTI1NTM2MjU2.YB1PcQ.r3X2QFuTt_iYfUAACZA0fZuhno0"
bad = ["tlqkf", "ㅅㅂ", "rotoRL", "개새끼", "씨발", "니애미", "sldoal", "qudtls", "qt", "ㅄ", "병신", "tq"]
defaultprefix = ';'
defaultcolour = 0xcdcdcd

@client.event
async def on_ready():
    print("봇이 온라인으로 전환되었습니다.")

@client.event
async def on_message(message):
    if message.author.bot:
        return None

@client.event
async def on_message(message):
    if message.content == "!안녕":
        my_channel = message.channel.guild.get_channel(807258161735401484)
        await message.channel.send("안녕하세요")

    if message.content == "!설정":
        my_channel = message.channel.guild.get_channel(807258161735401484)
        embed = discord.Embed(title="Title", description="Description", color=0x62c1cc)
        embed.add_field(name="Name", value="Value", inline=False)
        embed.add_field(name="Name1", value="Value1", inline=False)
        await message.channel.send(embed=embed)

    mc = message.content
    for i in bad:
        if i in mc:
            my_channel = message.channel.guild.get_channel(807258161735401484)
            await message.channel.send(f"{message.author.mention}님이 욕을 하셨습니다.")
            await message.delete()

client.run(token)
