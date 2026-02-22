import nextcord
from nextcord.ext import commands
import asyncio

intents = nextcord.Intents.default()
bot = commands.Bot(command_prefix="?", intents=intents)

@bot.command()
async def start(ctx):

    embed = nextcord.Embed(
        title="🔄 Restoration Process Started",
        description="Restoring members...\n\nPlease wait while the system rebuilds the server.",
        color=0x2f3136
    )

    embed.add_field(name="Status", value="🟡 Initializing", inline=True)
    embed.add_field(name="Progress", value="0%", inline=True)
    embed.add_field(name="System", value="Online", inline=True)
    embed.set_footer(text="Zornatalus Restore Engine")

    msg = await ctx.send(embed=embed)

    progress = 0

    while progress < 100:
        await asyncio.sleep(1.5)
        progress += 20

        update = nextcord.Embed(
            title="🔄 Restoration Process Started",
            description="Restoring members...\n\nPlease wait while the system rebuilds the server.",
            color=0x2f3136
        )

        status = "🟢 Complete" if progress >= 100 else "🟡 Restoring"

        update.add_field(name="Status", value=status, inline=True)
        update.add_field(name="Progress", value=f"{progress}%", inline=True)
        update.add_field(name="System", value="Online", inline=True)
        update.set_footer(text="Zornatalus Restore Engine")

        await msg.edit(embed=update)

bot.run("MTQ3NDg3NDQwNDQ1MzQ4MjU0Nw.G86nKT.c7IjjCGL250QgpHRJ2EXhr-gAy6klSdvukIi_U")