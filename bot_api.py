from AI_API import API
import discord
import time 
import discord.ext.commands as commands
import asyncio
from snap import images,randoms,webpage,close_browser
import re

discord_token = "your_discord_bot_token_here"

intents = discord.Intents.default()
intents.message_content = True

bot=commands.Bot(command_prefix="-",intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.command()
async def ask(ctx,image_path, *, user_prompt):
    await ctx.send("Processing your request...")
    response = API("sonar", user_prompt, image_path)
    output= "".join(re.findall(r"\*\*(.*?)\*\*", response))
    print(output)
    await ctx.send(response)




bot.run(discord_token)


