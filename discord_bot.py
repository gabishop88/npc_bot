import discord, json

keys = {}
with open('secrets.json', 'r') as f:
    keys = json.load(f)

print (keys)

class NPCClient(discord.Client):

    async def on_ready(self):
        print('Bot is ready!')

    async def on_message(self,message):
        if message.author == client.user:
            return

        response = 'Thank you for your message, {0.author.mention}!'.format(message)
        await message.channel.send(response)

# @client.event
# async def on_ready():
#     print('Bot is ready!')

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     response = 'Thank you for your message, {0.author.mention}!'.format(message)
#     await message.channel.send(response)

if __name__ == '__main__':
    intents = discord.Intents.default()
    intents.message_content = True
    client = NPCClient(intents=intents)
    client.run(keys['DISCORD_BOTKEY'])