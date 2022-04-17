import discord
from discord.ext import commands
from discord.ui import Modal
from discord import app_commands, ui


class kick(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name='킥',
        description='유저를 추방 합니다. (봇 제외)'
    )
    @commands.has_permissions(administrator=True)
    async def kick(self, interaction: discord.Interaction, mention: discord.Member, reason: str=None) -> None:
        if interaction.guild.fetch_member(mention.id) is not None:
            success = discord.Embed(
                title='[유저 관리] - 킥({})'.format(mention.name),
                colour=discord.Colour.green()
            )
            success.add_field(name='유저 이름', value=mention.name, inline=False)
            success.add_field(name='유저 아이디', value=mention.id, inline=False)
            success.add_field(name='사유', value=reason if reason is not None else '사유 없음', inline=False)
            await interaction.guild.kick(mention, reason=reason)
            await interaction.response.send_message(embed=success)
        else:
            err = discord.Embed(
                title='[에러] 킥',
                description='시스템 오류가 발생 했거나 존재 하지 않는 유저 혹은 이미 밴된 유저 입니다.',
                colour=discord.Colour.red()
            )
            await interaction.response.send_message(embed=err)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(kick(bot), guilds=[discord.Object(id=947022293664673842)])
