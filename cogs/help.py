import discord
from discord.ext import commands
from discord import app_commands, ui
from discord.ui import View


class helper(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(
        name='helper',
        description='명령어 를 보여 줍니다.'
    )
    async def helper(
            self,
            interaction: discord.Interaction,
    ) -> None:
        select = ui.Select(placeholder='도움말 을 선택 해주 세요.', min_values=1, max_values=1,
                           options=[
                               discord.SelectOption(label='일반 명령어', emoji='💬', description='일반 명령어 를 보여 줍니다.'),
                               discord.SelectOption(label='관리자 명령어', emoji='<:discord_staff:965104114721755196>',
                                                    description='관리자 명령어 를 '
                                                                '보여 줍니다.')
                           ])

        default_cmd = discord.Embed(
            title='[도움말] - 일반 명령어',
            colour=discord.Colour.random()
        )
        default_cmd.set_author(name=interaction.user.name, icon_url=interaction.user.avatar.url)
        default_cmd.add_field(name='도움말', value='명령 어를 표시 해줍 니다.', inline=False)
        default_cmd.add_field(name='핑', value='유저와 봇 간의 응답 속도를 표시 해줍 니다.', inline=False)
        default_cmd.set_footer(text='본 커맨드 들은 슬래시 커맨드 입니다. 칭호: /')

        moder_cmd = discord.Embed(
            title='[도움말] - 관리자 명렁어',
            colour=discord.Colour.random()
        )
        moder_cmd.add_field(name='밴', value='유저를 차단 합니다.(상위 역할 필요)', inline=False)
        moder_cmd.add_field(name='킥', value='유저를 추방 합니다.(상위 역할 필요)', inline=False)
        moder_cmd.add_field(name='언밴', value='유저를 차단 해재 합니다.', inline=False)
        moder_cmd.add_field(name='채팅청소', value='채팅 청소를 합니다.', inline=False)
        moder_cmd.add_field(name='인증', value='인증 시스템을 불러 옵니다. (캡차)', inline=False)
        moder_cmd.set_footer(text='본 커맨드 들은 슬래시 커맨드 입니다. 칭호: /')

        async def callback(sel_interact: discord.Interaction):
            if select.values[0] == '일반 명령어':
                await sel_interact.response.edit_message(embed=default_cmd)
            elif select.values[0] == '관리자 명령어':
                await sel_interact.response.edit_message(embed=moder_cmd)

        select.callback = callback
        view = View()
        view.add_item(select)

        await interaction.response.send_message(embed=default_cmd, view=view)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        helper(bot),
        guilds=[discord.Object(id=947022293664673842)]
    )
