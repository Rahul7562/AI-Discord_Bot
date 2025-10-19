from AI_API import API
import discord
import time 
import discord.ext.commands as commands
import asyncio

discord_token = "YOUR_DISCORD_BOT_TOKEN_HERE"

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
async def ask(ctx, *, user_prompt):
    await ctx.send("Processing your request...")
    response = asyncio.to_thread(API,"sonar-pro", user_prompt)
    await ctx.send(response)

bot.run(discord_token)
