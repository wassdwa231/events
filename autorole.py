import discord
from discord.ext import commands

Intents = discord.Intents.default()
Intents.message_content = True
Intents.members = True

bot = commands.Bot(command_prefix="!",intents=Intents)


@bot.event
async def on_ready():
    print("iam ready sir")


@bot.event
async def on_member_join(member: discord.Member):
        channel = discord.utils.get(member.guild.channels, name="welcome")
        if channel:
              await channel.send(f"Welcome at server {member.mention}")

        role = discord.utils.get(member.guild.roles, name="wick")
        if role:
            await member.add_roles(role)
