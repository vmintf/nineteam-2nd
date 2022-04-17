# 모듈 불러오기
import discord
from discord.ext import commands

from discord import app_commands, ui
from discord.ui import View

import random
import string


class verify(commands.Cog):  # 클래스 생성
    def __init__(self, bot: commands.Bot) -> None:  # cog 기능의 일부 코드
        self.bot = bot  # self를 commands.Bot 함수로 선언

    @app_commands.command(
        name='인증',
        description='인증 채널을 설정 합니다.'
    )  # 슬래시 커맨드 선언
    @commands.has_permissions(administrator=True)  # 관리자 펄미션 선언
    async def verify(self, interaction: discord.Interaction):  # 커맨드 코어 코딩
        btn = ui.Button(label='인증 하기', style=discord.ButtonStyle.green, emoji='✅')  # 버튼 형성

        async def button_callback(btn_callback: discord.Interaction):  # 버튼 콜백 기능
            role = discord.utils.get(btn_callback.guild.roles, name='유저')
            if discord.utils.get(btn_callback.user.roles, name='유저') is None:
                await btn_callback.user.send('인증 되었 습니다.')
                await btn_callback.user.add_roles(role)
            else:
                await btn_callback.user.send('인증 실패 | 사유: 이미 역할이 있음')

        # 버튼 생성
        btn.callback = button_callback
        view = View()
        view.add_item(btn)

        if discord.utils.get(interaction.guild.channels, name='인증-채널') is not None:
            channel = discord.utils.get(interaction.guild.channels, name='인증-채널')
            intro = discord.Embed(  # 임베드 생성
                title='인증 하기',
                description='아래의 버튼을 눌러 인증을 진행해 주세요.',
                colour=discord.Colour.random()
            )
            await interaction.response.send_message('200 | Ok. 메세지 생성 완료')
            await channel.send(embed=intro, view=view)  # 채널이 존재 하는 쪽으로 메세지 보내기
        else:
            await interaction.response.send_message('200 | Ok. 채널 생성 완료, 인증 명령어 를 다시 사용해 주세요.')
            await interaction.guild.create_text_channel(name='인증-채널', reason='인증을 위한 채널 생성')  # 인증 채널을 생성


# cog 최종 작업
async def setup(bot: commands.Bot):
    await bot.add_cog(verify(bot), guilds=[discord.Object(id=947022293664673842)])
