import discord, random, os, asyncio, requests, datetime
from BPass import gen_pass
from discord.ext import commands, tasks
 

intents = discord.Intents.default()

intents.message_content = True

 

bot = commands.Bot(command_prefix='$', intents=intents, description='python👑')

 


@bot.event
async def on_ready():
    print('katto esta activo!')
    channel = bot.get_channel(1241193662826680451)
    await channel.send('Hola, soy katto! Usa el comando "$functions" para ver que puedo hacer.')


@bot.command()

async def functions(ctx):
    await ctx.send('''Estos son mis comandos actuales y sus funciones:
"$hola": Comenzemos a hablar!
"$meme": Echa un vistaso a estos memes random sobre programacion!
"$seguridad": Crearé una contraseña aleatoria para ti!
"$reciclaje: Te enseñare donde desechar cada tipo de basura!
                   ''')


@bot.command()

async def hola(ctx):

    await ctx.send(f'Hola! Como estas?')


@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f'{ctx.guild.name}', description="Test Server", timestamp=datetime.datetime.now(datetime.UTC))
    embed.add_field(name='Server ID', value=f"{ctx.guild.id} ")
    embed.add_field(name='Server Date', value=f'{ctx.guild.created_at}')
    embed.add_field(name='Server Region', value=f'{ctx.guild.region}')
    embed.add_field(name='Server Owner', value=f'{ctx.guild.owner}')
    embed.set_thumbnail(url=f'{ctx.guild.icon}')
    await ctx.send(embed=embed)


@bot.command()
async def meme(ctx):
    image = random.choice(os.listdir("Memes"))


    with open(f'Memes/{image}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)


@bot.command()

async def seguridad(ctx):

    await ctx.send(gen_pass(10))

# Idea: El bot genera diferentes opciones de basura, donde eliges cual tienes y el bot te responde donde iria

@bot.command()

async def reciclaje(ctx):

    await ctx.send('''Opciones:
$Op1. Papeles.
$Op2. Vidrios/Cristales.
$Op3. Plasticos.
$Op4. Pilas/Baterias.
$Op5. Otros.
                   ''')
    

@bot.command()

async def Op1(ctx):

    await ctx.send(f'Puedes desechar papeles o similares en locales destinados a eso, o también puedes en zonas urbanas, donde encontraras contenedores azules con este símbolo "♻️".')

@bot.command()

async def Op2(ctx):

    await ctx.send(f'Puedes desechar vidrios o similares en locales destinados a eso, o también puedes en zonas urbanas, donde encontraras contenedores verdes con este símbolo "♻️".')


@bot.command()

async def Op3(ctx):

    await ctx.send(f'Puedes desechar plasticos o similares en locales destinados a eso, o también puedes en zonas urbanas, donde encontraras contenedores amarillos con este simbolo "♻️".')

@bot.command()

async def Op4(ctx):

    await ctx.send(f'Hay locales que reciben pilas/baterias usadas, lo recomendable es juntar la maxima cantidad posible y luego llevarlas.')

@bot.command()

async def Op5(ctx):

    await ctx.send(f'Lo mejor es reciclar, pero si ninguna de mis respuestas te sirve, investiga..¡Para un mundo mejor!')

bot.run("MTIwOTYwMDI4MzQ5MTk2NzA1Nw.GiqMdp.rwLzeDedXQMot-M02TrFINu5_Sbcoof_YIGJes")