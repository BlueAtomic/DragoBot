import discord
from discord.ext import commands
import datetime
import calendar

bot = discord.Bot()
embed = discord.Embed


class time(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @bot.slash_command(name='time')
    async def info(self, ctx,year:int,month:int,day:int,hour:int,minute:int,second:int,style ):
        #check Time!
        if year <=1:
            message="your year is invalid"
        elif 0 < month >= 12:
            message = "your month is invalid"
        elif 0< day >= 31:
            message = "your day is invalid"
        elif 0 <= hour >= 24:
            message="your hour is invalid"
        elif 0 <= minute >= 59:
            message="you minute is invalid"
        elif 0 <= second >=59:
            message="your seconds are invalid"
        else:
            t = datetime.datetime(year, month, day, hour, minute, second)
            epoch= calendar.timegm(t.timetuple())
            message = f'<t:{epoch}:{style}> or `<t:{epoch}:{style}>`'




        embed = discord.Embed(
            title="timestap",
            description=message,
            timestamp=discord.utils.utcnow(),
            color=discord.Color.dark_gray())
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(time(bot))
