# main.py
import nextcord
from nextcord.ext import commands
import asyncio

# =======================
# === CONFIG SECTION ====
# =======================
BOT_TOKEN = "MTQ3NDg3NDQwNDQ1MzQ4MjU0Nw.G86nKT.c7IjjCGL250QgpHRJ2EXhr-gAy6klSdvukIi_U"  # <-- put your token here
GUILD_ID = 1439272009715548170      # <-- replace with your server ID for slash commands to register fast

# =======================
# === BOT SETUP =========
# =======================
intents = nextcord.Intents.default()
bot = commands.Bot(
    command_prefix="!", 
    intents=intents, 
    debug_guilds=[GUILD_ID]  # registers slash commands immediately in your server
)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

# =======================
# === SLASH COMMAND =====
# =======================
@bot.slash_command(description="Start the fake restoring process")
async def start(interaction: nextcord.Interaction):
    # Initial embed
    embed = nextcord.Embed(
        title="🛠️ Restoring Files...",
        description="Initializing restore process...",
        color=0x00ff00
    )
    await interaction.response.send_message(embed=embed)
    message = await interaction.original_message()

    # Fake progress steps
    steps = [
        "Connecting to server...",
        "Scanning files...",
        "Decrypting data...",
        "Restoring files...",
        "Finalizing..."
    ]

    for i, step in enumerate(steps):
        await asyncio.sleep(2)  # wait 2 seconds per step
        percent = int((i+1)/len(steps)*100)
        # Optional fake progress bar
        bars = int((i+1)/len(steps)*10)
        progress_bar = "█" * bars + "-" * (10 - bars)
        embed.description = f"{step}\n`[{progress_bar}] {percent}%`"
        await message.edit(embed=embed)

    # Finished
    embed.title = "✅ Restore Complete!"
    embed.description = "All files have been restored successfully!"
    embed.color = 0x00ffff
    await message.edit(embed=embed)

# =======================
# === RUN BOT ===========
# =======================
bot.run(BOT_TOKEN)
