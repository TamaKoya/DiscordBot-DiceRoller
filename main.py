import os
import dotenv
import logging
from SingleDice import SingleRoll
from MultiDice import MultiRoll
from CustomDice import CustomRoll
from interactions import listen, slash_command, SlashContext, Client, Intents, SlashCommandChoice, OptionType, Embed, BrandColors, SlashCommandOption, slash_option, Timestamp

bot = Client()
intents = Intents.DEFAULT
dotenv.load_dotenv()
server_id = [1211283623840325632]
logging.basicConfig(filename='logs.txt', filemode='w', format='%(asctime)s - %(message)s', level=logging.WARNING, encoding='utf-8')


@listen()
async def on_ready():
    print("Bot ONLINE!")
    logging.warning("Bot ONLINE!")


def dices_option():
    def wrapper(func):
        return slash_option(
            name="dice",
            description="Select a dice",
            required=True,
            opt_type=OptionType.INTEGER,
            choices=[SlashCommandChoice(name="D4", value=1),
                     SlashCommandChoice(name="D6", value=2),
                     SlashCommandChoice(name="D8", value=3),
                     SlashCommandChoice(name="D10", value=4),
                     SlashCommandChoice(name="D12", value=5),
                     SlashCommandChoice(name="D20", value=6),
                     SlashCommandChoice(name="D100", value=7)
                     ]
        )(func)
    return wrapper


def roll_modifier():
    def wrapper(func):
        return slash_option(
            name="modifier",
            description="OPTIONAL - Add a modifier to your roll",
            required=False,
            opt_type=OptionType.INTEGER
        )(func)
    return wrapper


@slash_command(name="single", description="Roll a single dice!", dm_permission=False, scopes=server_id)
@dices_option()
@roll_modifier()
async def single_function(ctx: SlashContext, dice: int, modifier: int = 0):
    match dice:
        case 1:
            result = SingleRoll.single_dice(dice, modifier)
            embed = Embed(title="Single D4 Roll",
                          description=result,
                          color=BrandColors.WHITE,
                          timestamp=Timestamp.now())
            await ctx.send(embeds=embed)
            logging.warning(f"{ctx.member} has invoked a single roll of D4. The result was - {result}   || Format: total(rolled dice) ||")
        case 2:
            result = SingleRoll.single_dice(dice, modifier)
            embed = Embed(title="Single D6 Roll",
                          description=result,
                          color=BrandColors.WHITE,
                          timestamp=Timestamp.now())
            await ctx.send(embeds=embed)
            logging.warning(f"{ctx.member} has invoked a single roll of D6. The result was - {result}   || Format: total(rolled dice) ||")
        case 3:
            result = SingleRoll.single_dice(dice, modifier)
            embed = Embed(title="Single D8 Roll",
                          description=result,
                          color=BrandColors.WHITE,
                          timestamp=Timestamp.now())
            await ctx.send(embeds=embed)
            logging.warning(f"{ctx.member} has invoked a single roll of D8. The result was - {result}   || Format: total(rolled dice) ||")
        case 4:
            result = SingleRoll.single_dice(dice, modifier)
            embed = Embed(title="Single D10 Roll",
                          description=result,
                          color=BrandColors.WHITE,
                          timestamp=Timestamp.now())
            await ctx.send(embeds=embed)
            logging.warning(f"{ctx.member} has invoked a single roll of D10. The result was - {result}   || Format: total(rolled dice) ||")
        case 5:
            result = SingleRoll.single_dice(dice, modifier)
            embed = Embed(title="Single D12 Roll",
                          description=result,
                          color=BrandColors.WHITE,
                          timestamp=Timestamp.now())
            await ctx.send(embeds=embed)
            logging.warning(f"{ctx.member} has invoked a single roll of D12. The result was - {result}   || Format: total(rolled dice) ||")
        case 6:
            result = SingleRoll.single_dice(dice, modifier)
            embed = Embed(title="Single D20 Roll",
                          description=result,
                          color=BrandColors.WHITE,
                          timestamp=Timestamp.now())
            await ctx.send(embeds=embed)
            logging.warning(f"{ctx.member} has invoked a single roll of D20. The result was - {result}   || Format: total(rolled dice) ||")
        case 7:
            result = SingleRoll.single_dice(dice, modifier)
            embed = Embed(title="Single D100 Roll",
                          description=result,
                          color=BrandColors.WHITE,
                          timestamp=Timestamp.now())
            await ctx.send(embeds=embed)
            logging.warning(f"{ctx.member} has invoked a single roll of D100. The result was - {result}   || Format: total(rolled dice) ||")
        case _:
            await ctx.send("You didn't select a dice. Aborting...")


@slash_command(name="multi",
               description="Roll multiple dices!",
               dm_permission=False,
               options=[
                   SlashCommandOption(
                       name="count",
                       description="How many times do you wish to roll the dice?",
                       required=True,
                       type=OptionType.INTEGER
                   )
               ],
               scopes=server_id)
@dices_option()
@roll_modifier()
async def multi_function(ctx: SlashContext, dice: int, count: int, modifier: int = 0):
    match dice:
        case 1:
            result = MultiRoll.multi_dice(dice, count, modifier)
            embed = Embed(title="Multi D4 Roll",
                          description=result,
                          color=BrandColors.WHITE,
                          timestamp=Timestamp.now())
            await ctx.send(embeds=embed)
            logging.warning(f"{ctx.member} has invoked a multi roll of D4. The result was: {result}, amount of dices: {count}.")
        case 2:
            result = MultiRoll.multi_dice(dice, count, modifier)
            embed = Embed(title="Multi D6 Roll",
                          description=result,
                          color=BrandColors.WHITE,
                          timestamp=Timestamp.now())
            await ctx.send(embeds=embed)
            logging.warning(f"{ctx.member} has invoked a multi roll of D4. The result was: {result}, amount of dices: {count}.")
        case 3:
            result = MultiRoll.multi_dice(dice, count, modifier)
            embed = Embed(title="Multi D8 Roll",
                          description=result,
                          color=BrandColors.WHITE,
                          timestamp=Timestamp.now())
            await ctx.send(embeds=embed)
            logging.warning(f"{ctx.member} has invoked a multi roll of D4. The result was: {result}, amount of dices: {count}.")
        case 4:
            result = MultiRoll.multi_dice(dice, count, modifier)
            embed = Embed(title="Multi D10 Roll",
                          description=result,
                          color=BrandColors.WHITE,
                          timestamp=Timestamp.now())
            await ctx.send(embeds=embed)
            logging.warning(f"{ctx.member} has invoked a multi roll of D4. The result was: {result}, amount of dices: {count}.")
        case 5:
            result = MultiRoll.multi_dice(dice, count, modifier)
            embed = Embed(title="Multi D12 Roll",
                          description=result,
                          color=BrandColors.WHITE,
                          timestamp=Timestamp.now())
            await ctx.send(embeds=embed)
            logging.warning(f"{ctx.member} has invoked a multi roll of D4. The result was: {result}, amount of dices: {count}.")
        case 6:
            result = MultiRoll.multi_dice(dice, count, modifier)
            embed = Embed(title="Multi D20 Roll",
                          description=result,
                          color=BrandColors.WHITE,
                          timestamp=Timestamp.now())
            await ctx.send(embeds=embed)
            logging.warning(f"{ctx.member} has invoked a multi roll of D4. The result was: {result}, amount of dices: {count}.")
        case 7:
            result = MultiRoll.multi_dice(dice, count, modifier)
            embed = Embed(title="Multi D100 Roll",
                          description=result,
                          color=BrandColors.WHITE,
                          timestamp=Timestamp.now())
            await ctx.send(embeds=embed)
            logging.warning(f"{ctx.member} has invoked a multi roll of D4. The result was: {result}, amount of dices: {count}.")
        case _:
            await ctx.send("You didn't select a dice. Aborting...")


@slash_command(name="custom_single",
               description="A single roll of custom dice!",
               dm_permission=False,
               options=[
                   SlashCommandOption(
                       name="size",
                       description="What's the size of the dice you wish to roll?",
                       required=True,
                       type=OptionType.INTEGER
                   ),
                   SlashCommandOption(
                       name="title",
                       description="What's this roll about?",
                       required=True,
                       type=OptionType.STRING
                   )
               ],
               scopes=server_id)
@roll_modifier()
async def custom_single_function(ctx: SlashContext, size: int, title: str, modifier: int = 0):
    result = CustomRoll.single_custom(size, modifier)
    embed = Embed(title=title,
                  description=result,
                  color=BrandColors.WHITE,
                  timestamp=Timestamp.now())
    await ctx.send(embeds=embed)
    logging.warning(f"{ctx.member} has invoked a single roll of custom dice. The result was: {result}.")


@slash_command(name="custom_multi",
               description="Multiple rolls of custom dices!",
               dm_permission=False,
               options=[
                   SlashCommandOption(
                       name="size",
                       description="What's the size of the dice you wish to roll?",
                       required=True,
                       type=OptionType.INTEGER
                   ),
                   SlashCommandOption(
                       name="count",
                       description="How many times do you wish to roll the dice?",
                       required=True,
                       type=OptionType.INTEGER
                   ),
                   SlashCommandOption(
                       name="title",
                       description="What's this roll about?",
                       required=True,
                       type=OptionType.STRING
                   )
               ],
               scopes=server_id)
@roll_modifier()
async def custom_multi_function(ctx: SlashContext, size: int, count: int, title: str, modifier: int = 0):
    result = CustomRoll.multi_custom(size, count, modifier)
    embed = Embed(title=title,
                  description=result,
                  color=BrandColors.WHITE,
                  timestamp=Timestamp.now())
    await ctx.send(embeds=embed)
    logging.warning(f"{ctx.member} has invoked a multi roll of custom dice. The result was: {result}, amount of dices: {count}.")

bot.start(os.getenv("TOKEN"))
