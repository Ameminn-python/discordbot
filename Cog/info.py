import discord
from discord.ext import commands

class search_id:
    def __init__(self,bot,id):
        self.bot = bot
        self.id = id
        
    def judge(self):
        if self.id in self.bot.guilds:
            return 'guild_id'
        for
