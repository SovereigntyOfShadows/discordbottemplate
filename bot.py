from discord.ext.commands import Bot,Context
from discord import Intents, Message

bot = Bot('>',intents=Intents.all())


# from here you can edit to make more commands


@bot.command()
async def hi(ctx:Context):
    await ctx.send("fats")

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send('FUCK OFF')

@bot.event
async def on_message(msg:Message):
    if msg.author.id !=bot.user.id:
        if msg.content.lower().startswith("im"):
            await message.channel.send(f"hi {msg.content[{}:]}, i'm dad")
        if msg.content.lower().startswith("i'm"):
            await message.channel.send(f"hi {msg.content[{}:]}, i'm dad")
        if msg.content.lower().startswith("i am"):
            await message.channel.send(f"hi {msg.content[{}:]}, i'm dad")


@bot.command()
async def bye(ctx:Context):
    await ctx.send("you're ugly")



# do not touch after this
try:
    with open("./token") as f:
        bot.run(f.readline().removesuffix("\n"))
except FileNotFoundError:
    print("No Token has been set")