# --==@==-- #
from logging import Manager, error
from time import sleep
from typing import Text
from discord.ext.commands.core import has_permissions
from discord.ext.commands.errors import MissingPermissions
from dotenv import load_dotenv
from discord import colour, guild, team
from discord.ext import tasks, commands
import discord
import json
import asyncio
import requests
import random
import libs
import os
# --==@==-- #

#Atributos e variaveis Gerais do Bot
load_dotenv()
Token = os.getenv('TOKEN1')
#TOKEN1 = SUNAA TESTE
#TOKEN2 = SUNNA OFICIAL
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '--', case_insensitive = True, intents=intents)
client.remove_command('help')
# --==@==-- #


#Logs Console - Geral do Bot
@client.event
async def on_ready():
    print('------------')
    print('Logado!!!')
   # print the total number of channels the bot is in
   
    print('Nome:', client.user.name)
    print('ID:', client.user.id)
    print('Servidores:', len(client.guilds))
    print('Usuarios:', len(client.guilds))
    print('------------')
    presence.start()
    
    
#Mudança de presença (Random)
@tasks.loop(seconds = 25)
async def presence():
  status = [
            'a memes...',
            'a Hentai...',
            'a {} usúarios | --help'.format(len (client.users)),
            'a {} servers | --help'.format(len (client.guilds)),
            'ao Reddit...',
            'a XVideos...',
            'a Batatinha 1 2 3...'
            ]
  numero = random.choice(status) 
  await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=numero))


#Comando de Limpar Chat
@client.command(name='clear')
async def clear(ctx, amount = 0):
 try:
   if amount == 0:
      embed = discord.Embed(
        colour= 12255232,
        description = f"Por favor, insira um valor para excluir! `Ex: --clear 1` ❌"
      )
      v= await ctx.send (embed=embed)
      await asyncio.sleep (5) 
      await v.delete() 
   else:
      await ctx.channel.purge(limit=amount)
      embed = discord.Embed(
          colour= 32768,
          description = f"Mensagens apagadas com Sucesso! ✅"
      )
      sucess = await ctx.send(embed=embed)
      await asyncio.sleep (5) 
      await sucess.delete()
 except:
    print('Erro no comando Clear!!!')




@client.command(name='stoploop')
async def stoploop(self, ctx, channel: discord.TextChannel): 
  self.c = False
  try:
    if ctx.message.author.guild_permissions.administrator:
      channel_position = channel.position   
      clonechannel = await channel.clone(name=channel.name, reason='Clonando') 
      await channel.delete()
      await clonechannel.edit(position=channel_position, sync_permissions=True)
      embed = discord.Embed(
        colour= 32768,
        description = f'O Loop do Canal: **{channel.name}** foi retirado com sucesso! ✅'
      )
      sucess = await ctx.channel.send(embed=embed)
      await sucess.add_reaction("✅")  
      await asyncio.sleep (6) 
      await sucess.delete()
    else:
      embed = discord.Embed(
         colour= 12255232,
         description = f'Você precisar ter permissão de administrador para usar este comando ❌'
      )
      sucess = await ctx.channel.send(embed=embed)
      await sucess.add_reaction("❌")  
      await asyncio.sleep (5) 
      await sucess.delete()         
  except:
    print('Erro no comando StopLoop!!!') 



#Comando de Enviar Memes
@client.command(name="meme")   
async def meme(ctx):
  try:
        dados = requests.get(f'https://meme-api.herokuapp.com/gimme/{random.choice(libs.gerais)}')
        meme = json.loads(dados.text)
        embed = discord.Embed(
          title = meme['title'],
          url = meme['url'],
          ups = meme['ups'],
          description = meme['subreddit'],
          colour = discord.Colour.red()
        )
        embed.set_author(name='Sunaa', icon_url='https://cdn.discordapp.com/attachments/637851829396570134/875176423386669086/image5.jpg')
        embed.set_image(url=meme['url']) 
        embed.set_footer(text = '👍 para like  || 👎 para deslike')
        msg = await ctx.channel.send(embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")
  except:
    print('Erro no comando Meme!!!')  

#Comando de Enviar Memes de Animes
@client.command(name="addloopmeme") 
async def addloopmeme(self, ctx):
  self.c == True
  try: 
    if ctx.message.author.guild_permissions.administrator:
        embed = discord.Embed(
        color=0xffae00,
        description = "Aguarde estou Iniciando o Loop! 🟡"
        )
        sucess = await ctx.send(embed=embed)
        sleep (3)
        idcanal = ctx.channel.id
        asyncio.create_task(loopmeme(self.c, idcanal))
        embed = discord.Embed(
        colour= 32768,
        description = "Memes automáticos adicionado com Sucesso! ✅"
        )
        await ctx.send(embed=embed)
        await sucess.delete()
    else:
      embed = discord.Embed(
         colour= 12255232,
         description = f'Você precisar ter permissão de administrador para usar este comando ❌'
      )
      sucess = await ctx.channel.send(embed=embed)
      await sucess.add_reaction("❌")  
      await asyncio.sleep (5) 
      await sucess.delete()   
  except:
      print('Erro no comando addloopmeme!!!')

    
async def loopmeme(self, idcanal):
   while True and self.c == True:
     try:
        dados = requests.get(f'https://meme-api.herokuapp.com/gimme/{random.choice(libs.gerais)}')
        meme = json.loads(dados.text)
        embed = discord.Embed(
          title = meme['title'],
          url = meme['url'],
          ups = meme['ups'],
          description = meme['subreddit'],
          colour = discord.Colour.red()
        )
        embed.set_author(name='Sunaa', icon_url='https://cdn.discordapp.com/attachments/637851829396570134/875176423386669086/image5.jpg')
        embed.set_image(url=meme['url']) 
        embed.set_footer(text = '👍 para like  || 👎 para deslike')
        channel = client.get_channel(idcanal)
        msg = await channel.send(embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")
        sleep(8)
     except:   
       print('Erro de "titulo" ignorado (Loopmeme)!!!')



#Comandos de Enviar Memes de Animes
@client.command() 
async def animes(ctx):
  try:
        dados = requests.get(f'https://meme-api.herokuapp.com/gimme/{random.choice(libs.anime)}')
        meme = json.loads(dados.text)
        embed = discord.Embed(
          title = meme['title'],
          url = meme['url'],
          ups = meme['ups'],
          description = meme['subreddit'],
          colour = discord.Colour.red()
        )
        embed.set_author(name='Sunaa', icon_url='https://cdn.discordapp.com/attachments/637851829396570134/875176423386669086/image5.jpg')
        embed.set_image(url=meme['url']) 
        embed.set_footer(text = '👍 para like  || 👎 para deslike')
        msg = await ctx.channel.send(embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")
  except:
      print('Erro no comando Animes!!!')    


#Comando de Enviar Memes de Animes
@client.command(name="addloopanimes") 
async def addloopanimes(ctx):
  try:
    if ctx.message.author.guild_permissions.administrator:
        embed = discord.Embed(
        color=0xffae00,
        description = "Aguarde estou Iniciando o Loop! 🟡"
        )
        sucess = await ctx.send(embed=embed)
        sleep (3) 
        idcanal = ctx.channel.id
        asyncio.create_task(loopanimes(idcanal))
        embed = discord.Embed(
        colour= 32768,
        description = f"Animes automáticos adicionado com Sucesso! ✅"
        )
        await ctx.send(embed=embed)
        await sucess.delete()
    else:
      embed = discord.Embed(
         colour= 12255232,
         description = f'Você precisar ter permissão de administrador para usar este comando ❌'
      )
      sucess = await ctx.channel.send(embed=embed)
      await sucess.add_reaction("❌")  
      await asyncio.sleep (5) 
      await sucess.delete()      
  except:
      print('Erro no comando addloopanimes!!!')

async def loopanimes(idcanal):
   while True:
     try:
        dados = requests.get(f'https://meme-api.herokuapp.com/gimme/{random.choice(libs.anime)}')
        meme = json.loads(dados.text)
        embed = discord.Embed(
          title = meme['title'],
          url = meme['url'],
          ups = meme['ups'],
          description = meme['subreddit'],
          colour = discord.Colour.red()
        )
        embed.set_author(name='Sunaa', icon_url='https://cdn.discordapp.com/attachments/637851829396570134/875176423386669086/image5.jpg')
        embed.set_image(url=meme['url']) 
        embed.set_footer(text = '👍 para like  || 👎 para deslike')
        channel = client.get_channel(idcanal)
        msg = await channel.send(embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")
        sleep(8)
     except:   
       print('Erro de "titulo" ignorado (Loopanimes)!!!')




#Comando de Enviar Animes +18
@client.command() 
async def ansfw(ctx):
  try:
        if ctx.channel.is_nsfw():
            dados = requests.get(f'https://meme-api.herokuapp.com/gimme/{random.choice(libs.anime2)}')
            meme = json.loads(dados.text)
            embed = discord.Embed(
              title = meme['title'],
              url = meme['url'],
              ups = meme['ups'],
              description = meme['subreddit'],
              colour = discord.Colour.red()
            )
            embed.set_author(name='Sunaa', icon_url='https://cdn.discordapp.com/attachments/637851829396570134/875176423386669086/image5.jpg')
            embed.set_image(url=meme['url']) 
            embed.set_footer(text = '👍 para like  || 👎 para deslike')
            msg = await ctx.channel.send(embed=embed)
            await msg.add_reaction("👍")
            await msg.add_reaction("👎")
        else:
            embed = discord.Embed(
              colour= 12255232,
              description = f"Você precisa estar em um canal de NSFW 💢"
            )
            error = await ctx.channel.send(embed=embed)
            await error.add_reaction("💢")
  except:
      print('Erro no comando ansfw!!!')

#Comando de Enviar Memes de Animes
@client.command(name="addloopanimes18") 
async def addloopanimes18(ctx):
  try:
    if ctx.message.author.guild_permissions.administrator:
      if ctx.channel.is_nsfw():
        embed = discord.Embed(
        color=0xffae00,
        description = "Aguarde estou Iniciando o Loop! 🟡"
        )
        sucess = await ctx.send(embed=embed)
        sleep (3)
        idcanal = ctx.channel.id
        asyncio.create_task(loopanimes18(idcanal))
        embed = discord.Embed(
        colour= 32768,
        description = "Animes +18 automáticos adicionado com Sucesso! 😈✅"
        )
        await ctx.send(embed=embed)
        await sucess.delete()
      else:    
        embed = discord.Embed(
          colour= 12255232,
          description = f"Você precisa estar em um canal de NSFW 💢"
        )
        error = await ctx.channel.send(embed=embed)
        await error.add_reaction("💢")
    else:
      embed = discord.Embed(
         colour= 12255232,
         description = f'Você precisar ter permissão de administrador para usar este comando ❌'
      )
      sucess = await ctx.channel.send(embed=embed)
      await sucess.add_reaction("❌")  
      await asyncio.sleep (5) 
      await sucess.delete()      
  except:
      print('Erro no comando addloopanimes!!!')

async def loopanimes18(idcanal):
   while True:
     try:
            dados = requests.get(f'https://meme-api.herokuapp.com/gimme/{random.choice(libs.anime2)}')
            meme = json.loads(dados.text)
            embed = discord.Embed(
              title = meme['title'],
              url = meme['url'],
              ups = meme['ups'],
              description = meme['subreddit'],
              colour = discord.Colour.red()
            )
            embed.set_author(name='Sunaa', icon_url='https://cdn.discordapp.com/attachments/637851829396570134/875176423386669086/image5.jpg')
            embed.set_image(url=meme['url']) 
            embed.set_footer(text = '👍 para like  || 👎 para deslike')
            channel = client.get_channel(idcanal)
            msg = await channel.send(embed=embed)
            await msg.add_reaction("👍")
            await msg.add_reaction("👎")
            sleep(8)
     except:   
        print('Erro de "titulo" ignorado (Loopanimes18)!!!')

 

#Comando de Enviar IRL +18
@client.command() 
async def rnsfw(ctx):
  try:
        if ctx.channel.is_nsfw():
            dados = requests.get(f'https://meme-api.herokuapp.com/gimme/{random.choice(libs.realporn)}')
            meme = json.loads(dados.text)
            embed = discord.Embed(
              title = meme['title'],
              url = meme['url'],
              ups = meme['ups'],
              description = meme['subreddit'],
              colour = discord.Colour.red()
            )
            embed.set_author(name='Sunaa', icon_url='https://cdn.discordapp.com/attachments/637851829396570134/875176423386669086/image5.jpg')
            embed.set_image(url=meme['url']) 
            embed.set_footer(text = '👍 para like  || 👎 para deslike')
            msg = await ctx.channel.send(embed=embed)
            await msg.add_reaction("👍")
            await msg.add_reaction("👎")
        else:
          embed = discord.Embed(
            colour= 12255232,
            description = f"Você precisa estar em um canal de NSFW 💢"
          )
          error = await ctx.channel.send(embed=embed)
          await error.add_reaction("💢")
  except:
      print('Erro no comandoo rnsfw!!!')

#Comando de Enviar Memes de Animes
@client.command(name="addloopreal18") 
async def addloopreal18(ctx):
  try:
    if ctx.message.author.guild_permissions.administrator:
      if ctx.channel.is_nsfw():
        embed = discord.Embed(
        color=0xffae00,
        description = "Aguarde estou Iniciando o Loop! 🟡"
        )
        sucess = await ctx.send(embed=embed)
        sleep (3)
        idcanal = ctx.channel.id
        asyncio.create_task(loopreal18(idcanal))
        embed = discord.Embed(
        colour= 32768,
        description = "Porn +18 automáticos adicionado com Sucesso! 😈✅"
        )
        await ctx.send(embed=embed)
        await sucess.delete()
      else:    
        embed = discord.Embed(
          colour= 12255232,
          description = f"Você precisa estar em um canal de NSFW 💢"
        )
        error = await ctx.channel.send(embed=embed)
        await error.add_reaction("💢")
    else:
      embed = discord.Embed(
         colour= 12255232,
         description = f'Você precisar ter permissão de administrador para usar este comando ❌'
      )
      sucess = await ctx.channel.send(embed=embed)
      await sucess.add_reaction("❌")  
      await asyncio.sleep (5) 
      await sucess.delete()      
  except:
      print('Erro no comando addloopreal18!!!')

async def loopreal18(idcanal):
   while True:
     try:
            dados = requests.get(f'https://meme-api.herokuapp.com/gimme/{random.choice(libs.realporn)}')
            meme = json.loads(dados.text)
            embed = discord.Embed(
              title = meme['title'],
              url = meme['url'],
              ups = meme['ups'],
              description = meme['subreddit'],
              colour = discord.Colour.red()
            )
            embed.set_author(name='Sunaa', icon_url='https://cdn.discordapp.com/attachments/637851829396570134/875176423386669086/image5.jpg')
            embed.set_image(url=meme['url']) 
            embed.set_footer(text = '👍 para like  || 👎 para deslike')
            channel = client.get_channel(idcanal)
            msg = await channel.send(embed=embed)
            await msg.add_reaction("👍")
            await msg.add_reaction("👎")
            sleep(8)
     except:   
        print('Erro de "titulo" ignorado (Loopreal18)!!!')


#Comando de Enviar Meme de Futebol
@client.command() 
async def futebol(ctx):
  try:
        dados = requests.get(f'https://meme-api.herokuapp.com/gimme/{random.choice(libs.fut)}')
        meme = json.loads(dados.text)
        embed = discord.Embed(
          title = meme['title'],
          url = meme['url'],
          ups = meme['ups'],
          description = meme['subreddit'],
          colour = discord.Colour.red()
        )
        embed.set_author(name='Sunaa', icon_url='https://cdn.discordapp.com/attachments/637851829396570134/875176423386669086/image5.jpg')
        embed.set_image(url=meme['url']) 
        embed.set_footer(text = '👍 para like  || 👎 para deslike')
        msg = await ctx.channel.send(embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")
  except:
      print('Erro no comando futebol!!!')


#Comando de Enviar Gifs
@client.command() 
async def gifs(ctx):
  try:
        dados = requests.get(f'https://meme-api.herokuapp.com/gimme/{random.choice(libs.gif)}')
        meme = json.loads(dados.text)
        embed = discord.Embed(
          title = meme['title'],
          url = meme['url'],
          ups = meme['ups'],
          description = meme['subreddit'],
          colour = discord.Colour.red()
        )
        embed.set_author(name='Sunaa', icon_url='https://cdn.discordapp.com/attachments/637851829396570134/875176423386669086/image5.jpg')
        embed.set_image(url=meme['url']) 
        embed.set_footer(text = '👍 para like  || 👎 para deslike')
        msg = await ctx.channel.send(embed=embed)
        await msg.add_reaction("👍")
        await msg.add_reaction("👎")
  except:
    print('Erro no comando gifs!!!')

 
#Comando de Help Geral
@client.command() 
async def help(ctx):
  try:
       embed=discord.Embed(title="Sunna - Lista de comandos.", description="**Apoie o projeto e mande sugestões.** Possui alguma ideia, conhece um SubReddit com conteúdos  incríveis para o bot? **Mande um e-mail para:** *sunnabot@hotmail.com*", color=0xf24526)
       embed.set_author(name="Sunna Bot", icon_url="https://cdn.discordapp.com/attachments/637851829396570134/875176423386669086/image5.jpg")
       embed.add_field(name="Memes😂", value="`--meme`", inline=True)
       embed.add_field(name="Futebol⚽️", value="`--futebol`", inline=True)
       embed.add_field(name="Anime㊙️", value="`--animes`", inline=True)
       embed.add_field(name="** **", value="** **", inline=True)
       embed.add_field(name="** **", value="** **", inline=True)
       embed.add_field(name="** **", value="** **", inline=True)
       embed.add_field(name="Porn +18🔞", value="`--rnsfw`", inline=True)
       embed.add_field(name="Anime +18🔞", value="`--ansfw`", inline=True) 
       embed.add_field(name="Gifs♨️", value="`--gifs`", inline=True)       
       embed.add_field(name="** **", value="** **", inline=True)    
       embed.add_field(name="** **", value="** **", inline=True)           
       embed.add_field(name="** **", value="** **", inline=True)
       embed.add_field(name="Futebol⚽️", value="`--futebol`", inline=True)
       embed.add_field(name="Help❓", value="`--help`", inline=True)
       embed.add_field(name="Clear Chat⛔️", value="`--clear`", inline=True)
       embed.add_field(name="** **", value="** **", inline=True)  
       embed.add_field(name="** **", value="** **", inline=True)    
       embed.add_field(name="** **", value="** **", inline=True)  
       embed.add_field(name="Gerador de Memes📜", value="`--gerador`", inline=True)
       embed.set_footer(text="~ Sunaa Bot - Desenvolvedor Biell#0001")
       await ctx.channel.send(embed=embed) 
  except:
      print('Erro no comando help!!!')


@client.command()
async def gerador(ctx):
  try:
    embed=discord.Embed(title="Instruções 📜", color=0xf24526)
    embed.set_author(name="Sunna", icon_url="https://cdn.discordapp.com/attachments/637851829396570134/875176423386669086/image5.jpg")
    embed.add_field(name="**Aviso 💢**", value="**Você precisar de permissão de administrador no servidor para usar esses comandos! 💢**", inline=False)
    embed.add_field(name="⌛️ Memes automáticos", value="A função *memes automáticos* basicamente permite a **Sunaa** enviar memes e outras funções do bot de forma automática em um intervalo de 10 segundos, para adicionar é muito facil.", inline=True)
    embed.add_field(name="📃 Passo a Passo", value="Basta digitar os comandos de sua escolha em um canal de texto para o bot iniciar o gerador. Após enviar o comando aguarde o Loop ser iniciado, isso pode demorar alguns segundos", inline=False)
    embed.add_field(name="** ** ", value="**🔴 --addloopmeme** :O bot fará o envio de **memes** aleatórios *(Intervalo 10s)*", inline=False)
    embed.add_field(name="** ** ", value="**🔴 --addloopanimes** : O bot fará o envio de **meme anime** aleatórios *(Intervalo 10s)*", inline=False)
    embed.add_field(name="** ** ", value="**🔴 --addloopanimes18** : O bot fará o envio de **animes +18** aleatórios *(Intervalo 10s)* - **Requisitos** *: O Canal deve ser NSFW💢*", inline=False)
    embed.add_field(name="** ** ", value="**🔴 --addloopreal18** : O bot fará o envio de **porn +18** aleatórios *(Intervalo 10s)* - **Requisitos** *: O Canal deve ser NSFW💢*", inline=False)
    embed.add_field(name="** ** ", value="** **", inline=False)
    embed.add_field(name="**⛔️ Remover o Loop**", value="**--stoploop (nomedocanal)** : Para parar o envio de memes automáticos basta reenviar o comando --stoploop seguido do nome do canal onde se encontra o loop, por exemplo: `--stoploop memes`", inline=False)
    embed.add_field(name="** **", value="**Aviso 💢 - Caso o gerador automáticos pare de funcionar basta reenviar o comando novamente!**", inline=False)
    embed.set_footer(text="~ Sunaa Bot - Desenvolvedor Biell#0001")
    await ctx.send(embed=embed)
  except:
      print('Erro no comando gerador!!!')


#Comando em Teste - Adicionar Subreddit ao Bot!!
@client.command() 
async def addreddit(ctx):
  try:
      comu = ctx.content
      comu = comu.split(' ')
      libs.gerais.append(comu[1])
      print(libs.gerais)
  except:
      print('Erro no comando!!!')


client.run(Token)
