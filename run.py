import discord
from event_handler import *

COMANDS = {
    '.help': help,
    '.search': lmgtfy_search,
    '.s': lmgtfy_search,
}
# Список команд, для добавления новой:
# 1) В файле event_handler.py созать функцию // Например: test_func(*args):
# 2) Добавить как будет выглядеть команда и добавить её в словарь // Например '.test': test_func

TOKEN = 'Njc1MDM0MzgxODgyMDk3Njkz.XjxRXw.EzrpaU4u2WSgKnNWuEFUGfoWxLI'
PERSONAL_CHANNEL = 675036319822381076  # Персональный канал, который обнуляется при запуске бота!
# В текущий момент Причина-->reason

client = discord.Client()


@client.event
async def on_ready():
    print('Connected')
    async for m in client.get_channel(PERSONAL_CHANNEL).history():
        await m.delete()


@client.event
async def on_message(msg):
    """
    <
        Message id=675039799312384033
        channel=<TextChannel id=675036319822381076 name='reason' position=1 nsfw=False news=False category_id=665628103992803368>
        type=<MessageType.default: 0>
        author=<Member id=188660675046932482 name='GorillazZz' discriminator='8901' bot=False nick='Ссанина'
        guild=<Guild id=665628103480967202 name='Причина' shard_id=None chunked=True member_count=14>>
        flags=<MessageFlags value=0>
    >
    """
    if msg.author == client.user:
        return

    if msg.content.startswith('.'):
        print(msg.channel.id)
        content = msg.content.split()

        await msg.delete(delay=4.5)
        await msg.channel.send(
            COMANDS[content[0] if content[0] in list(COMANDS.keys()) else '.help'](*tuple(content[1:])),
            delete_after=5.0
        )


client.run(TOKEN)
