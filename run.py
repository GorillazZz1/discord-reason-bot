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

TOKEN = 'Njc1MDM0MzgxODgyMDk3Njkz.XjyPvw.P6fo_GsGCNAomEAXz9YIUYbTUyE'
PERSONAL_CHANNEL_ID = 675036319822381076  # Персональный канал, который обнуляется при запуске бота!
REASON_GUILD_ID = 665628103480967202
# В текущий момент Причина-->reason

VOICE_CHANNELS = []

client = discord.Client()


@client.event
async def on_ready():
    print('Connected')
    async for m in client.get_channel(PERSONAL_CHANNEL_ID).history():
        await m.delete()
    await client.get_channel(PERSONAL_CHANNEL_ID).send(
        'Всё было подчищено _вилкой_!',
        delete_after=5.0
    )

    # global VOICE_CHANNELS
    # VOICE_CHANNELS = client.get_guild(REASON_GUILD_ID).voice_channels
    #
    # print(client.get_guild(REASON_GUILD_ID).members)
    # for channel in VOICE_CHANNELS:
    #     print([(m.nick + '#' + m.discriminator, m.id) for m in channel.members], (channel.id, channel.name))


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
        content = msg.content.split()
        await msg.channel.send(
            COMANDS[content[0] if content[0] in list(COMANDS.keys()) else '.help'](*tuple(content[1:])),
            delete_after=5.0
        )
        await msg.delete(delay=4.5)


client.run(TOKEN)
