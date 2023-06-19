import discord
from discord.ext import commands

bot = discord.Bot()
embed = discord.Embed


class Info(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @bot.slash_command(name='info')
    async def info(self, ctx):
        embed = discord.Embed(
            title="DragoBot",
            description="The DragoBot ",
            timestamp=discord.utils.utcnow(),
            color=discord.Color.dark_gray())
        embed.add_field(name="info about the bot",
                        value="This is a bot called DragoBot")
        await ctx.respond( embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
