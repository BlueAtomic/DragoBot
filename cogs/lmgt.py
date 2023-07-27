import discord
from discord.ext import commands

bot = discord.Bot()
embed = discord.Embed

URl_LMGT= "https://letmegooglethat.com/?q="
class lmgt(commands.Cog):
    def __int__(self, bot):
        self.bot = bot

    @bot.slash_command(name='lmgt')
    async def info(self, ctx, input):
        Url =(URl_LMGT + input.replace(" ", "+"))
        embed = discord.Embed(
            title="lmgt link",
            timestamp=discord.utils.utcnow(),
            color=discord.Color.dark_gray())
        embed.add_field(name=f"link to {input}",
                        value=Url)
        await ctx.respond( embed=embed)


def setup(bot):
    bot.add_cog(lmgt(bot))
