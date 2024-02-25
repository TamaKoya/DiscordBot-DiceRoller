import datetime
import os
import dotenv
from SingleDice import SingleRoll
from interactions import listen, slash_command, SlashContext, Client, Intents, SlashCommandChoice, OptionType, Embed, BrandColors, SlashCommandOption
import markdown_strings

bot = Client()
intents = Intents.DEFAULT
dotenv.load_dotenv()


@listen()
async def on_ready():
    print("Bot ONLINE!")


@slash_command(name="rollsingle",
               description="Roll a single dice!",
               dm_permission=False,
               options=[
                   SlashCommandOption(name="dice",
                                      description="Select a dice",
                                      required=True,
                                      type=OptionType.INTEGER,
                                      choices=[SlashCommandChoice(name="D4", value=1),
                                               SlashCommandChoice(name="D6", value=2),
                                               SlashCommandChoice(name="D8", value=3),
                                               SlashCommandChoice(name="D10", value=4),
                                               SlashCommandChoice(name="D12", value=5),
                                               SlashCommandChoice(name="D20", value=6),
                                               SlashCommandChoice(name="D100", value=7)
                                               ])
               ],
               scopes=[1211283623840325632])
async def rollsingle_function(ctx: SlashContext, dice: int):
    match dice:
        case 1:
            embed = Embed(title="Single D4 Roll",
                          description=markdown_strings.header(f"D4: [{SingleRoll.single_d4()}]", 2),
                          color=BrandColors.WHITE,
                          timestamp=datetime.datetime.now())
            await ctx.send(embeds=embed)
        case 2:
            embed = Embed(title="Single D6 Roll",
                          description=markdown_strings.header(f"D6: [{SingleRoll.single_d6()}]", 2),
                          color=BrandColors.WHITE,
                          timestamp=datetime.datetime.now())
            await ctx.send(embeds=embed)
        case 3:
            embed = Embed(title="Single D8 Roll",
                          description=markdown_strings.header(f"D8: [{SingleRoll.single_d8()}]",2),
                          color=BrandColors.WHITE,
                          timestamp=datetime.datetime.now())
            await ctx.send(embeds=embed)
        case 4:
            embed = Embed(title="Single D10 Roll",
                          description=markdown_strings.header(f"D10: [{SingleRoll.single_d10()}]",2),
                          color=BrandColors.WHITE,
                          timestamp=datetime.datetime.now())
            await ctx.send(embeds=embed)
        case 5:
            embed = Embed(title="Single D12 Roll",
                          description=markdown_strings.header(f"D12: [{SingleRoll.single_d12()}]",2),
                          color=BrandColors.WHITE,
                          timestamp=datetime.datetime.now())
            await ctx.send(embeds=embed)
        case 6:
            embed = Embed(title="Single D20 Roll",
                          description=markdown_strings.header(f"D20: [{SingleRoll.single_d20()}]",2),
                          color=BrandColors.WHITE,
                          timestamp=datetime.datetime.now())
            await ctx.send(embeds=embed)
        case 7:
            embed = Embed(title="Single D100 Roll",
                          description=markdown_strings.header(f"D100: [{SingleRoll.single_d100()}]",2),
                          color=BrandColors.WHITE,
                          timestamp=datetime.datetime.now())
            await ctx.send(embeds=embed)
        case _:
            await ctx.send("You didn't select a dice. Aborting...")

bot.start(os.getenv("token"))
