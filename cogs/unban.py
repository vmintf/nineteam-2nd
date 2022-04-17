import discord
from discord.ext import commands
from discord import app_commands


class unban(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name='언밴',
        description='유저를 차단 해제 합니다. (봇 제외)'
    )
    @commands.has_permissions(administrator=True)
    async def unban(self, interaction: discord.Interaction, member: discord.Member, reason: str = None) -> None:
        if interaction.guild.fetch_member(member.id) is not None:
            try:
                success = discord.Embed(
                    title='[유저 관리] - 언밴 ({})'.format(member.name),
                    description='해당 유저가 언밴 되었 습니다.',
                    colour=discord.Colour.green()
                )
                success.add_field(name='유저 이름', value=member.name, inline=False)
                success.add_field(name='유저 아이디', value=member.id, inline=False)
                success.add_field(name='사유', value=reason if reason is not None else '사유 없음', inline=False)
                await interaction.guild.unban(member, reason=reason)
                await interaction.response.send_message(embed=success)
            except:
                err = discord.Embed(
                    title='[오류] 감지',
                    description='무언가의 오류를 감지 했어요.\n'
                                '봇 개발자 한테 문의 해주 세요.',
                    colour=discord.Colour.red()
                )
                await interaction.response.send(embed=err)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(unban(bot), guilds=[discord.Object(id=947022293664673842)])
