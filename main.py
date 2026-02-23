import nextcord
from nextcord.ext import commands
import asyncio
import random
import os

# -----------------------------
# CONFIG
# -----------------------------
TOKEN = os.getenv("TOKEN")  # Railway reads this automatically
GUILD_ID = 1439272009715548170  # <-- replace with your Discord server ID

intents = nextcord.Intents.all()
bot = commands.Bot(intents=intents)

warn_data = {}

# GOJO THEME COLORS
GOJO_BLUE = 0x7DF9FF
GOJO_PURPLE = 0xB266FF
GOJO_RED = 0xED4245
GOJO_YELLOW = 0xFEE75C

def gojo_embed(title, color=GOJO_BLUE):
    return nextcord.Embed(title=f"⚡ {title}", color=color)

# -----------------------------
# BOT READY
# -----------------------------
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    # sync commands globally (or per guild for instant)
    await bot.sync_application_commands(guild_ids=[GUILD_ID])
    await bot.change_presence(activity=nextcord.Game(name="Infinity GOJO Mode 😎"))

# -----------------------------
# /start RESTORE COMMAND
# -----------------------------
@bot.slash_command(description="Start GOJO restoration process", guild_ids=[GUILD_ID])
async def start(interaction: nextcord.Interaction):
    await interaction.response.send_message("⚡ Starting GOJO restoration...", ephemeral=True)
    msg = await interaction.channel.send("⚡ Initializing...")

    restored = 0
    total = random.randint(40, 120)
    stages = [
        "Reconnecting Shibuya nodes...",
        "Decrypting Infinity...",
        "Restoring Domain Expansion...",
        "Synchronizing Cursed Energy...",
        "Finalizing GOJO Recovery..."
    ]

    for stage in stages:
        await asyncio.sleep(1.5)
        restored += random.randint(5, 20)

        embed = gojo_embed("GOJO RESTORATION", color=GOJO_BLUE)
        embed.description = f"```{stage}```"
        embed.add_field(name="Recovered", value=f"{restored}/{total}")
        embed.add_field(name="System", value="🟢 Stable")
        embed.set_footer(text="Gojo Bot | Infinite Coolness")

        await msg.edit(embed=embed, content=None)

    final = gojo_embed("Restoration Complete", color=GOJO_PURPLE)
    final.description = f"Recovered **{total}** members."
    final.set_footer(text="Gojo Bot | Infinity Achieved ✨")
    await msg.edit(embed=final)

# -----------------------------
# MODERATION COMMANDS
# -----------------------------
@bot.slash_command(description="Ban a member", guild_ids=[GUILD_ID])
async def ban(interaction: nextcord.Interaction, member: nextcord.Member, reason: str = "No reason"):
    await member.ban(reason=reason)
    embed = gojo_embed("User Banned", GOJO_RED)
    embed.add_field(name="Member", value=str(member))
    embed.add_field(name="Reason", value=reason)
    await interaction.response.send_message(embed=embed)

@bot.slash_command(description="Kick a member", guild_ids=[GUILD_ID])
async def kick(interaction: nextcord.Interaction, member: nextcord.Member, reason: str = "No reason"):
    await member.kick(reason=reason)
    embed = gojo_embed("User Kicked", GOJO_PURPLE)
    embed.add_field(name="Member", value=str(member))
    embed.add_field(name="Reason", value=reason)
    await interaction.response.send_message(embed=embed)

@bot.slash_command(description="Mute (timeout) a member", guild_ids=[GUILD_ID])
async def mute(interaction: nextcord.Interaction, member: nextcord.Member, minutes: int):
    await member.timeout(minutes * 60)
    embed = gojo_embed("User Muted", GOJO_BLUE)
    embed.add_field(name="Member", value=str(member))
    embed.add_field(name="Duration", value=f"{minutes} minutes")
    await interaction.response.send_message(embed=embed)

@bot.slash_command(description="Warn a member", guild_ids=[GUILD_ID])
async def warn(interaction: nextcord.Interaction, member: nextcord.Member, reason: str):
    warn_data.setdefault(member.id, []).append(reason)
    embed = gojo_embed("User Warned", GOJO_YELLOW)
    embed.add_field(name="Member", value=str(member))
    embed.add_field(name="Reason", value=reason)
    embed.add_field(name="Total Warns", value=str(len(warn_data[member.id])))
    await interaction.response.send_message(embed=embed)

@bot.slash_command(description="Remove a warning", guild_ids=[GUILD_ID])
async def unwarn(interaction: nextcord.Interaction, member: nextcord.Member):
    if member.id in warn_data and warn_data[member.id]:
        warn_data[member.id].pop()
        embed = gojo_embed("Warn Removed", GOJO_BLUE)
        embed.add_field(name="Member", value=str(member))
        await interaction.response.send_message(embed=embed)
    else:
        await interaction.response.send_message("No warns found")

@bot.slash_command(description="View warnings", guild_ids=[GUILD_ID])
async def warns(interaction: nextcord.Interaction, member: nextcord.Member):
    warns = warn_data.get(member.id, [])
    if not warns:
        await interaction.response.send_message("No warns")
        return
    embed = gojo_embed(f"Warnings for {member}", GOJO_YELLOW)
    embed.description = "\n".join(warns)
    await interaction.response.send_message(embed=embed)

# -----------------------------
# RUN BOT
# -----------------------------
bot.run(TOKEN)
