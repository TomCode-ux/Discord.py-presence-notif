import discord
from discord.ext import commands, tasks
import requests


intents = discord.Intents.default()
client = commands.Bot(command_prefix='!')

userlist = discord.Embed(title="Users List")
userlist2 = discord.Embed(title="Users List1")
usernotif = discord.Embed(title="your warning")



client.started = False
@client.event
async def on_ready():
    if not client.started:
        client.started = True
        print('We have logged in as {0.user}'.format(client))





def loll():
    request.start()


global mesg
global list
list = '1'
mesg = 'not sent'
lol = {
            "userids": [
    #  user ids
            ]
        }
# add an user to the list
@client.command()
async def add(ctx, arg):
    args = int(arg)
    if type(args) == int:
        lol['userids'].append(arg)
        await ctx.send('Added!:white_check_mark: ')

global intmsg
intmsg = 'not sent'
@tasks.loop(seconds = 10)
async def request():
        await client.wait_until_ready()
        global intmsg
        if intmsg == 'not sent':
            global msg
            channel = client.get_channel(802281808908910657)
            msg = await channel.send(embed=userlist)
            intmsg = 'sent'

        response = requests.post("https://presence.roblox.com/v1/presence/users",data = lol )

        for data in response.json()['userPresences']:
            global on
            global presence
            userid = data['userId']
            username = requests.get(f"https://users.roblox.com/v1/users/{userid}" )
            presence = 'Unknown'
            if data['userPresenceType'] == 0:
                presence = 'Offline'
            elif data['userPresenceType'] == 1:
                presence = 'Website'
            elif data['userPresenceType'] == 2:
                presence = 'In-game'
            elif data['userPresenceType'] == 3:
                presence = 'Developing'

            name = username.json()['name']
            for field in userlist.fields and userlist2.fields:
                if field.name == name:
                    userlist2.add_field(name=name, value=f'{presence}\n' + '  https://www.roblox.com/users/'+ str(data['userId'])+'/profile', inline=False)
                    userlist.add_field(name=name, value=f'{presence}\n' + '  https://www.roblox.com/users/'+ str(data['userId'])+'/profile', inline=False)
                    break
            else:

                userlist2.add_field(name=name, value=f'{presence}\n' + '  https://www.roblox.com/users/'+ str(data['userId'])+'/profile', inline=False)
                userlist.add_field(name=name, value=f'{presence}\n' + '  https://www.roblox.com/users/'+ str(data['userId'])+'/profile', inline=False)
        global list
        if list == '1':
            await msg.edit(embed=userlist2)
            userlist.clear_fields()
            list = '2'
        else:
            await msg.edit(embed=userlist)
            userlist2.clear_fields()
            list ='1'
        global mesg
        if response.json()['userPresences'][3]['userPresenceType'] == 2 or 0 or 1:
            if response.json()['userPresences'][3]['userPresenceType'] == 2:
                if mesg == 'not sent':
                    print('message is not sent, sending...')
                    channel = client.get_channel(802281808908910657)
                    game = response.json()['userPresences'][3]['placeId']
                    usernotif.add_field(name='Game: https://www.roblox.com/games/' + str(game),value='', inline=False)
                    mesg = 'sent'
                    await channel.send(embed=usernotif)
                    await channel.send('||@everyone||')
                    usernotif.clear_fields()
                    print('sent message')
            elif response.json()['userPresences'][3]['userPresenceType'] == 1 or 0:
                if mesg == 'sent':
                    usernotif.clear_fields()
                    print('presence is 1 or 0, clearing fields')
                    mesg ='not sent'

loll()
client.run('bot token')
