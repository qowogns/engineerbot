#-*-coding: utf-8
# 사전파일 Fixer

import discord
import asyncio

client = discord.Client()

f = open("wordslist.txt", "r", encoding='utf8')
data = f.read()
l_data = data.split("\n")

@client.event
async def on_ready():
    print("끝말잇기 하는 사기리")
    print("="*20)

@client.event
async def on_message(message):
    global l_data
    m = message.content
    if message.content.startswith('!끝 '):
        win = 0
        cound = 0
        if m[-1] == m[3]:
            await client.send_message(message.channel, '한글자, 앞뒤가 같은 단어는 안돼요!')
        elif m[3:] in l_data:
            for i in l_data:
                if m[-1] == i[0]:
                    if len(i) >= 2: #답할 단어가 2음절 이상일 경우
                        print('답변 시도')
                        await client.send_message(message.channel, i)
                        l_data.remove(i)
                        win = 1
                        break
                    else: # 사전 파일에 한글자인 단어가 있어서 사용한 코드
                        while len(i) >= 2:
                            i_data.remove(i)
                            if len(i) >= 2:
                                print('다시 답변 시도')
                                await client.send_message(message.channel, i)
                                l_data.remove(i)
                                win = 1
                                break
            if win == 0:
                await client.send_message(message.channel, '제가 졌어요.')
        else:
            await client.send_message(message.channel, '제 사전에 없는 단어이거나 이미 제가 사용한 단어입니다.')
            
    elif message.content.startswith('!사전 '):
        m = message.content
        await client.send_message(message.channel, 'http://krdic.naver.com/search.nhn?query='+m[4:]+'&kind=all')
            


client.run('token')
