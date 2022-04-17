import os

import discord
from discord.ext import commands
from discord.app_commands import CommandTree

import dotenv


class Ninejuan(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='n_',
            intents=discord.Intents.all(),
            application_id=961949296620634152
        )

    async def on_ready(self):
        print('{} | {}'.format(bot.user.name, bot.user.id))

    async def setup_hook(self):
        print('-' * 40)
        print('명령어 로딩')
        for fn in os.listdir('./cogs'):
            if fn.endswith('.py'):
                await self.load_extension(f'cogs.{fn[:-3]}')
                await bot.tree.sync(guild=discord.Object(id=947022293664673842))
                print(f'로딩됨 | {fn[:-3]}')

        print('-' * 40)


dotenv.load_dotenv(dotenv_path='./src/ven/.env')
bot = Ninejuan()


bot.run(os.environ.get("TOKEN"))
