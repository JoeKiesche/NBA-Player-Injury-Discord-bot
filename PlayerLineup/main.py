import requests 
from bs4 import BeautifulSoup
from player import player
import discord
import os

#Fetch URl using beautiful soup
url = "https://www.rotowire.com/basketball/nba-lineups.php"

#Parse the HTML using beautiful soup
response = requests.get(url)

#Parse the HTML using beautiful soup
soup = BeautifulSoup(response.text, "html.parser")

playersHTML = soup.find_all('li', title='Very Likely To Play')

activePlayers = []

for p in playersHTML:
    temp = p.text.strip().split('\n')
    activePlayers.append(player(temp[1], temp[0], 1))

notPlayersHTML= soup.find_all('li', title='Very Unlikely To Play')
nonActivePlayers = []

for p in notPlayersHTML:
    temp = p.text.strip().split('\n')
    nonActivePlayers.append(player(temp[1], temp[0], 0))

print("Active players on tonights slate:\n")
for p in activePlayers:
    print(str(p))
    



print("NON Active players on tonights slate:\n")
for p in nonActivePlayers:
    print(str(p))



#BOT token 
TOKEN = 'Put Discord bot token here'
client = discord.Client(intents=discord.Intents.default())


@client.event
async def on_ready():
    #Shows in terminal if the bot is working
    print("Bot is online")
    
    #Gets the channel by its ID 
    #Where the X is put the channel ID number of where you want the bot to display the list of players
    #you get the channel ID by going into devloper mode in your account settings on the discord app
    #then right clicking on the channel and clicking "copy ID"
    channel = client.get_channel("XXXXXX")
    
    
    #prints in nba-injuries thread on server if bot is working
    await channel.send("#####################")
    await channel.send("##### NEW SLATE #####")
    await channel.send("#####################")
    await channel.send("Sending current players not playing on tonights slate.....")
    
    #loop through and print all non-active players
    for p in nonActivePlayers:
        await channel.send(str(p))
        await channel.send("-----------------------------------------------")
    await channel.send("Finished..........")

client.run(TOKEN)
