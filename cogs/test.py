import discord
from discord.ext import commands,bridge
from discord.ext.bridge import Bot

embed = discord.Embed
class Info(commands.Cog):
    def __int__(self, bot:Bot):
        self.bot = bot
    @bridge.bridge_command()
    async def info(self, ctx: bridge.BridgeContext):
        embed = discord.Embed(
            title="DobbieBot",
            description="The Dobbie bot ",
            timestamp=discord.utils.utcnow(),
            color=discord.Color.dark_gray())
        embed.add_field(name="ping", value=(f'ping = {round(bot.latency * 1000, 2)}'))
        embed.add_field(name="info about the bot",
                        value="this bot is made by Soapy7261#8558 and Dobbie#4778. To learn Dobbie how Discord bots work and how py-cord works!")

        embed.add_field(name="main commands", value="the /call1 comamnd and the /info command")
        await Utils.respond(ctx=ctx, embed=embed)

def setup(bot: bridge.Bot):
    bot.add_cog(Info(bot))