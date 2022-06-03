import discord
import random
#import asyncio

TOKEN = "OTgyMTQ5Mjc1OTg5NDY3MjQ2.Gd9SuR.-V6x0MoBECj3cpd2jyRT3XnW0xP8UwhalQVyg8"
CHANNEL_ID = "CHANNEL_ID"
client = discord.Client()

#bot起動完了時に実行される処理
@client.event
async def on_ready():
    channel = client.get_channel(CHANNEL_ID)
    print('ログイン成功')

#メッセージ受信時に実行される処理
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #受信したメッセージが"hey"だったとき"hello"を返す
    if message.content == "スロット":
        probability =random.randint(1,399)
        slot_list = ['<:emoji_15:981257788011466883>', '<:emoji_18:981264371302940762>', '<:emoji_17:981263484111188028>',
                     '<:emoji_16:981259118599868446>', '<:emoji_19:981266091697401856>','<:emoji_20:982184176486875186>'
                     '']
        A = random.choice(slot_list)
        B = random.choice(slot_list)
        C = random.choice(slot_list)
        if int(probability) ==int(1):
            await message.channel.send("ボーナス確定！！！")
            #await asyncio.sleep(3)
            await message.channel.send( '<:emoji_19:981266091697401856>'+'<:emoji_19:981266091697401856>'+'<:emoji_19:981266091697401856>')
        else:
            D = A+B+C
            await message.channel.send(D)
        if(A==B and B==C):
          await message.channel.send("大当たりー！！")
        #await message.channel.send('hello')

client.run(TOKEN)