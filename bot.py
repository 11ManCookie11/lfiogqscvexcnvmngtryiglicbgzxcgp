
import discord
from discord.ext import commands, tasks
import sqlite3
import random
import requests
import ast
import io
from PIL import Image, ImageDraw, ImageFont, ImageOps
import ffmpeg
import json
import asyncio
from itertools import cycle
import cv2
from pyzbar import pyzbar
import qrcode
import os
import psutil
from Cybernator import Paginator
import ast
import sqlite3

bot = commands.Bot(command_prefix='=')
COLOR_ERROR = 0xFF0000

connection = sqlite3.connect('./Data/main_data.db')
cursor = connection.cursor()

@bot.event
async def on_ready():
    cursor.execute("""CREATE TABLE IF NOT EXISTS guilds (
        name_guild TEXT,
        id_guild INT,
        
    )""")

    for guild in bot.guilds:
        if cursor.execute(f"SELECT id_guild FROM guilds WHERE id_guild = {guild.id}").fetchone() is None:
            cursor.execute(f"INSERT INTO guilds VALUES ('{guild}', {guild.id}, {len(guild.members)})")
        else:
            pass

    connection.commit()
    print('Gone')
	#await bot.change_presence(activity=discord.Activity(name='mc.greenshine.space', type=discord.ActivityType.watching))

#Принять
@bot.command( aliases = [ "Принять", "принять", "Принят", "принят", ] )
@commands.has_permissions ( administrator = True )
async def accept( ctx, member : discord.Member ):
    awaiting = discord.utils.get( ctx.message.guild.roles, id = 615644946791268446 ) # Айди роли ожидающего
    role1 = discord.utils.get( ctx.message.guild.roles, id = 615644682302521407 )
    for roles in member.roles:
        if roles in role1:			
            await member.add_roles(accepted, reason=None, atomic=True) # Добавление роли принятого
            await member.remove_roles( awaiting ) # Снимание роли ожидающего
            await ctx.send(embed = discord.Embed(description = f'{member.mention} ({member})**, Был принят модератором **{ctx.author.mention} ({ctx.author})**!** '))
        else:
        	await ctx.send(embed = discord.Embed(description = f'{ctx.author}, у данного пользователя нет роли {awaiting.mention}'))
#Пинг
@bot.command(aliases=["задержка"])
async def ping(ctx):
    embed = discord.Embed(description=f"{Bot.ws.latency * 1000:.0f} мс", color=0x1E90FF)
    await ctx.send(embed=embed)

bot.run(fucking_token)
