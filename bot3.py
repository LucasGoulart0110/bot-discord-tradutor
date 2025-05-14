import discord
from discord.ext import commands
from googletrans import Translator

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

translator = Translator()

# IDs dos canais
origem_channel_id = 1364692365909950485
destino_channel_id = 1370180575452729424

@client.event
async def on_ready():
    print(f"✅ Bot conectado como {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id == origem_channel_id:
        # Detectar idioma da mensagem
        detectado = translator.detect(message.content)
        idioma = detectado.lang

        destino_channel = client.get_channel(destino_channel_id)

        if destino_channel:
            # Verifica o idioma da mensagem
            if idioma == 'pt':
                traduzido = translator.translate(message.content, dest='en')
                embed = discord.Embed(
                    title=f"Mensagem de {message.author.display_name}",
                    description=f"**🇧🇷 Original:**\n{message.content}\n\n**🇺🇸 Tradução:**\n{traduzido.text}",
                    color=discord.Color.blue()
                )
                embed.set_thumbnail(url=message.author.avatar.url)  # Correção aqui
            elif idioma == 'en':
                traduzido = translator.translate(message.content, dest='pt')
                embed = discord.Embed(
                    title=f"Mensagem de {message.author.display_name}",
                    description=f"**🇺🇸 Original:**\n{message.content}\n\n**🇧🇷 Tradução:**\n{traduzido.text}",
                    color=discord.Color.green()
                )
                embed.set_thumbnail(url=message.author.avatar.url)  # Correção aqui
            else:
                traduzido = translator.translate(message.content, dest='en')
                embed = discord.Embed(
                    title=f"Mensagem de {message.author.display_name}",
                    description=f"**🌎 Original:**\n{message.content}\n\n**🇺🇸 Tradução:**\n{traduzido.text}",
                    color=discord.Color.purple()
                )
                embed.set_thumbnail(url=message.author.avatar.url)  # Correção aqui

            await destino_channel.send(embed=embed)

import os
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
bot.run(TOKEN)