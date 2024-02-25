import os
import dotenv
from interactions import listen, slash_command, SlashContext, Client, Intents
from discordhelp import createEmbed


bot = Client()
intents = Intents.DEFAULT
dotenv.load_dotenv()


@listen()
async def on_ready():
    print("Bot ONLINE!")


@slash_command(name="test", description="Test command")
async def test_command_function(ctx: SlashContext):
    await ctx.send("Test passed!")


bot.start(os.getenv("token"))
