import discord
from discord.ext import commands
import time
import calendar as cal
import re #regex

bot = discord.Bot()
embed = discord.Embed
print(type(time))


class timec(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @bot.slash_command(name='time')
    async def info(self, ctx, style, date):
        # Corrected regex pattern with 'r' before the opening quote
        regex = r'(?P<value>\d*\.?\d+)\s*(?P<unit>years?|yrs?|y|months?|M|weeks?|w|days?|d|hours?|hrs?|h|minutes?|mins?|m|seconds?|secs?|s)'
        matches = re.finditer(regex, date, re.IGNORECASE)

        total = 0

        for match in matches:
            factor = 1
            unit = match.group('unit').lower()

            if unit in ['years', 'year', 'yrs', 'yr', 'y']:
                factor = 365 * 24 * 60 * 60
            elif unit in ['months', 'month'] or unit == 'm':
                factor = 30 * 24 * 60 * 60
            elif unit in ['weeks', 'week', 'w']:
                factor = 7 * 24 * 60 * 60
            elif unit in ['days', 'day', 'd']:
                factor = 24 * 60 * 60
            elif unit in ['hours', 'hour', 'hrs', 'hr', 'h']:
                factor = 60 * 60
            elif unit in ['minutes', 'minute', 'mins', 'min', 'm']:
                factor = 60
            elif unit in ['seconds', 'second', 'secs', 'sec', 's']:
                factor = 1

            total += int(match.group('value')) * factor
        print(type(time))
        epoch = total + time.time()
        epoch = int(round(epoch))
        message = f'<t:{epoch}:{style}> or `<t:{epoch}:{style}>`'

        print(total)  # Optional: Print the total duration in seconds
        print(epoch)  # Optional: Print the resulting epoch time

        embed = discord.Embed(
            title="timestap",
            description=message,
            timestamp=discord.utils.utcnow(),
            color=discord.Color.dark_gray())
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(timec(bot))
