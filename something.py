from http import client
import json
from multiprocessing.connection import Client
import random
from types import MemberDescriptorType
from urllib import response
import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('On to something!!!'))
    print('Bot is online')
    print({client.user})
    print('Started')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
            await ctx.send(f'`Invalid Command`')

@client.command(name = "clear", aliases=["purge","cl"])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'`cleared {amount} messages`')

@client.command()
@commands.has_permissions(manage_messages=True)
async def nuke(ctx, amount=9999):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'`nuked this channel`')

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *,reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'kicked {member.name}#{member.discriminator}')

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *,reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'banned {member.name}#{member.discriminator}')

@client.command()
async def mention(ctx, member : discord.Member):
    await ctx.send(f'{member.mention}')

@client.command()
async def fk(ctx, member : discord.Member):
    await ctx.send(f'fked {member.mention}')

@client.command(name = "kill", aliases=["die"])
async def kill(ctx, member : discord.Member):
    await ctx.send(f'*killed {member.mention} successfully*')

@client.command(name = "spam", aliases=["sp"])
@commands.has_permissions(administrator=True)
async def spam(ctx, *, saymsg=None):
    await ctx.channel.purge(limit=1)
    await ctx.channel.send(f'{saymsg}\n{saymsg}\n{saymsg}\n{saymsg}\n{saymsg}\n{saymsg}\n{saymsg}\n{saymsg}\n{saymsg}\n{saymsg}\n{saymsg}\n{saymsg}\n{saymsg}\n{saymsg}\n{saymsg}')

@client.command(name = "say", aliases=["s"])
async def say(ctx, *, saymsg=None):
    await ctx.channel.purge(limit=1)

    embed=discord.Embed(title=f"{ctx.author.name} Said", description=f"{saymsg}", color=0xe3fc03)
    await ctx.send(embed=embed)

@client.command(name = "announcement", aliases=["announce","an"])
@commands.has_permissions(administrator=True)
async def announcement(ctx, *, saymsg=None):
    await ctx.channel.purge(limit=1)

    embed=discord.Embed(title="NEW ANNOUNCEMENT", description=f"{saymsg}", color=0xff0000)
    embed.add_field(name="Server Announcement", value=f"Something2022", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def ping(ctx,):
    await ctx.channel.purge(limit=1)
    await ctx.send(f'Pong! `{round(client.latency * 1000)} ms`')

@client.command()
@commands.has_permissions(administrator=True)
async def ding(ctx):
    await ctx.send(f'Dong! `{round(client.latency * 10000)} ms`')

@client.command()
@commands.has_permissions(administrator=True)
async def whoisnoob(ctx):
    await ctx.send(f'@𝓝𝓲𝓴𝓲#8887 is a NOOB')

@client.command()
async def info(ctx):
    embed=discord.Embed(title="INFO", description="This is a bot Made by MrGoose for\nsome usees idk what are they and i am not ours", color=0x03fc30)
    embed.add_field(name="Something BOT", value=".help for list of commands", inline=False)
    await ctx.send(embed=embed)

@client.command(name = "serversite", aliases=["ss"])
async def serversite(ctx):
    await ctx.send(f'`Our Templory Website https://sites.google.com/view/goosesmp`')

@client.command()
async def ip(ctx):
    await ctx.send(f'```ip = simoniacgoose88.ddns.net \nport = 19132```')

@client.command()
async def invite(ctx):
    await ctx.send(f'Invite Me to your server using this link \nhttps://discord.com/api/oauth2/authorize?client_id=962228219417882654&permissions=8&scope=bot')

@client.command(name = "partnership", aliases=["ps"])
async def partnership(ctx):
    embed=discord.Embed(title="H-Pixels", description="+-----------+------------+\njoin the server it is free hahahaha\nA good place for Minecraft both java and bedrock player's.\nserver owner - Hack_Gaming5008\njoin if u want.\n+-----------+------------+", color=0x03d3fc)
    embed.add_field(name="https://discord.gg/x3hH5m5QQK", value="Current Partnership\nfrom H-Pixel's", inline=False)
    await ctx.send(embed=embed)

@client.command()
async def roast(ctx):
    responses = ['Your Beautiful!',
                'idc',
                'If I throw a stick, will you leave?',
                'You are a gray sprinkle on a rainbow cupcake.',
                'OH MY GOD! IT SPEAKS!',
                'Child, I have forgotten more than you ever knew.',
                'Bye, hope to see you never.',
                'When you look in the mirror, say hi to the clown you see in there for me, would ya?',]
    await ctx.send(f'{random.choice(responses)}')

@client.command()
async def dog(ctx):
    responses = ['https://media.giphy.com/media/2C2qwckZzyiz8UzvzK/giphy.gif',
                'https://media.giphy.com/media/VeHBSH9F4GZpuuic00/giphy-downsized-large.gif',
                'https://media.giphy.com/media/tSjoI5BPjXsHzqQuCS/giphy-downsized-large.gif',
                'https://media.giphy.com/media/eYilisUwipOEM/giphy.gif',
                'https://media.giphy.com/media/MtsBHd0UsiH7t6twq0/giphy.gif',
                'https://media.giphy.com/media/mokQK7oyiR8Sk/giphy.gif',
                'https://media.giphy.com/media/0v0KlsuyXUvTrLPXZu/giphy.gif',
                'https://media.giphy.com/media/B2vBunhgt9Pc4/giphy.gif',]
    await ctx.send(f'{random.choice(responses)}')

@client.command()
async def sus(ctx):
    responses = ['uuhhhhh? ummmmmm?',
                'IMPOSTER?',
                'AMONG US?',
                'sus',
                'Never gonna give you up \nNever gonna lets you down \nNever gonna run around and desert you',
                'https://media.giphy.com/media/Ju7l5y9osyymQ/giphy.gif',
                'BEAT HIM UP BEAT HIM UP... BEAT HIM UP , BEAT HIM UP  ,BEAT HIM UP  ,BEAT HIM UP',]
    await ctx.send(f'{random.choice(responses)}') 

@client.command()
async def cat(ctx):
    responses = ['https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif',
                'https://media.giphy.com/media/jpbnoe3UIa8TU8LM13/giphy.gif',
                'https://media.giphy.com/media/v6aOjy0Qo1fIA/giphy.gif',
                'https://media.giphy.com/media/sr8jYZVVsCmxddga8w/giphy.gif',
                'https://media.giphy.com/media/VbnUQpnihPSIgIXuZv/giphy.gif',
                'https://media.giphy.com/media/C9x8gX02SnMIoAClXa/giphy-downsized-large.gif'
                'https://media.giphy.com/media/CqVNwrLt9KEDK/giphy.gif',
                'https://media.giphy.com/media/QObPo575HQHlGMhbae/giphy.gif',]
    await ctx.send(f'{random.choice(responses)}')

@client.command(name = "help", aliases=["?"])
async def help(ctx):
    embed=discord.Embed(title="Command Help", description="clear (Needs Manage Messages Perms)\nnuke (Need Manage Messages Perm)\nkick (Need Admin Perms)\nban (Need Admin Perms)\nannouncement (Need Admin Perms)\nmention\nsay\nping\ninfo\nserversite\nip\ninvite\npartnership\nroast\ncat\ndog\nsus\nkill\nhelp", color=0x5a03fc)
    embed.add_field(name="Something2022", value="Prefix Is (.)", inline=False)
    await ctx.send(embed=embed) 

client.run('OTYyMjI4MjE5NDE3ODgyNjU0.YlEe3A.m3-Y4UgzI0p-57SYHNSl8N6TefY')