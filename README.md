# Discord Bot "Dice Roller"

"Dice Roller" is a small **Discord** bot, which allows to roll dices, that are used in various TTRPG games (short for: Tabletop Role Playing Games), e.g - Dungeons & Dragons, Pathfinder, Starfinder, Call of Cthulu, Cyberpunk, Warhammer and many other. The dices in question are:

* D4
* D6
* D8
* D10
* D12
* D20
* D100

As well as what I call a "Custom" dice, where the user specifies the maximum number that can be rolled.

Additionally, there's a **OPTIONAL** component called **GM's Dices** which is a Single Page App made using **Vue.js**, that imports a JS based library for dice rolling called **RPG Dice Roller**, made by **GreenImp** and available on [Github](https://github.com/dice-roller/rpg-dice-roller) along with its [documentation.](https://dice-roller.github.io/documentation/)

**This bot is shared for free in form of set of files as-is, that are needed to self-host this bot on your own PC/Server/Whatever you use.**

***

### Used packages, Python version and short descriptions of them

**Python 3.11**

* `interactions.py`, version **5.11.0** - This is the main package, used to write the bot itself and handling its operation;
* `python-dotenv`, version **1.0.1** - I used this to have the code read the bot's token from a .env file using built-in `os` module; *Note: the .env file is not included in this repo due to security reasons, as it's supposed to contain the unique token of the bot that's needed to run the bot.*
* `markdown-strings`, version **3.3.0** - This gives the ability to parse strings formatted in **Markdown** language to the outputs of commands;
* `logging`, built-in module - This module gives the host a log of each command used by users in a form of .txt file, for additional logging;
* `random`, built-in module - This module handles all the dice rolls, by running `random.randint(1, x)`, where **x** is the maximum number of the dice that's being used.

**GM's Dices**, as mentioned before is based on **Vue.js**, which was added to this project using **Node.js** and its `npm` package manager by running `npm create vue@latest`, which runs a setup tool for creating a Vue project.
This Vue project uses a ready-to-use Vue component made by **GreenImp**, author of **RPG Dice Roller**, which is installed into the project using `npm install @dice-roller/vue` and added to the project files using its [documentiation.](https://github.com/dice-roller/vue)

***

### Installation

Instructions on setting up this bot for self-hosting on your own PC can be found [here.](https://github.com/TamaKoya/DiscordBot-DiceRoller/wiki/Setting-up-the-bot)

If you plan on running this bot through a hosting, then details about what you need to know can be found [here.](https://github.com/TamaKoya/DiscordBot-DiceRoller/wiki/Notes-for-running-the-bot-through-a-hosting)

If you plan on running this bot on a VPS or anything simillar to that, then I'm afraid you'll have to figure it out on your own, as I do not have any sort of experience with that. Sorry.

***

### How to use the bot

This bot gives a total of 4 Slash Commands to use. Here are their syntax and description.

* /single <dice> <modifier> - Rolls a single dice of choice and adds the modifier to the score. 
* /multi <count> <dice> <modifier> - Rolls <count> times dice of choice and adds the modifier to the total score, e.g - /multi 4 d6 0 is equivalent to rolling 4 d6 dices, without adding or substracting anything from total score, a.k.a 4d6.
* /custom_single <size> <title> <modifier> - Rolls a single dice with <size> being maximum number allowed to be rolled and adding modifier to the score. <title> asks the user to give a name for this roll to make it easier for other to understand what the roll was for.
* /custom_multi <size> <count> <title> <modifier> - Rolls <count> times dices with <size> being maximum number allowed to be rolled for each dice and adding modifier to the total score. <title> asks the user to give a name for this roll to make it easier for other to understand what the roll was for.

Since the bot uses Slash Commands instead of prefixed commands, as user starts typing the chosen command, the bot will ask the user for each required variable of the command as per syntax, thus lowering the risk for user to make a mistake. For <count> the user needs to type a positive number, for <dice> the user will be presented with a list of available dices, where the user just needs to click on one of them, and for <title> the user just needs to type a text that'll become the name of the roll.

After filling each required variable, the user will also have a choice to select the modifier option. If user clicks on the option, they'll be asked to type a number that'll become the modifier. It can be either positive or negative number.

**Modifier in each command is optional, it defaults to 0 if the option is not selected.**

***

### Licence

Copyright (c) 2024 TamaKoya

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so.

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
