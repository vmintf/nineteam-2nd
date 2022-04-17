import discord
from discord.ext import commands

from discord import app_commands


class clean(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(
        name='채팅청소',
        description='채팅창을 청소 합니다.'
    )
    @commands.has_permissions(administrator=True)
    async def clean(self, interaction: discord.Interaction, number: int):
        if number is not None:
            await interaction.channel.purge(limit=number)
            success = discord.Embed(
                title='[청소] 청소 완료({}개)'.format(number),
                description='청소를 완료 하였 습니다.'
            )
            await interaction.response.send_message(embed=success)


async def setup(bot: commands.Bot):
    await bot.add_cog(clean(bot), guilds=[discord.Object(id=947022293664673842)])
