import discord
from event_handler import *
from secret_token import TOKEN

COMMANDS = {
    '.help': {'content': help},
    '.search': {'content': google_search},
    '.s': {'content': google_search},
    '.time': {'content': get_local_time},
    '.t': {'content': get_local_time},
    '.anek': {'content': get_random_anek,
              'tts': True, 'delete_after': 30.0},
    '.a': {'content': get_random_anek,
           'tts': True, 'delete_after': None},
}

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
        command = COMMANDS[content[0] if content[0] in COMMANDS.keys() else '.help']
        kwargs = {
            'content': command['content'](*tuple(content[1:])),
            'delete_after': (command['delete_after'] if 'delete_after' in command.keys() else 5.0),
            'tts': (command['tts'] if 'tts' in command.keys() else False),
        }
        '''
        kwargs = {
            'content': None,
            'delete_after': None,
            'tts': False,
            'embed': None,
            'file': None,
            'files': None,
            'nonce': None
        }
            content: :class:`str`
                The content of the message to send.
            tts: :class:`bool`
                Indicates if the message should be sent using text-to-speech.
            embed: :class:`~discord.Embed`
                The rich embed for the content.
            file: :class:`~discord.File`
                The file to upload.
            files: List[:class:`~discord.File`]
                A list of files to upload. Must be a maximum of 10.
            nonce: :class:`int`
                The nonce to use for sending this message. If the message was successfully sent,
                then the message will have a nonce with this value.
            delete_after: :class:`float`
                If provided, the number of seconds to wait in the background
                before deleting the message we just sent. If the deletion fails,
                then it is silently ignored.
                
        content=None, *, tts=False, embed=None, file=None, files=None, delete_after=None, nonce=None
        '''
        await msg.channel.send(**kwargs)
        await msg.delete(delay=4.5)


client.run(TOKEN)
