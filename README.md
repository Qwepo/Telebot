# Telebot
This is a telegram bot that will display information about the cryptocurrency rate from coinmarketcap.com

To launch the bot, you need to add your token to the Confi.py file. The token can be obtained from BotFather.

At the moment this is version 0.1
It contains the following bugs and shortcomings:
1)When adding a link with an " or ' sign at the beginning of a line, for example like this "https://coinmarketcap.com/currencies/bitcoin - returns an error.
2)Verification of correctness when entering a link to a non-existent token from the coinmarketcap site is not complete. 
To fix this, I had to write exceptions for the AttributeError.
3)There is no limit on the number of links for one user.
