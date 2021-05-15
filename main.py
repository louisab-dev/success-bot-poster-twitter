import discord
import asyncio
import requests
import tweepy
import re
from discord.ext import commands


client = discord.Client()
bot = commands.Bot(command_prefix='.')

## TOKENS THAT CAN BE FOUND IN YOUR TWITTER APPLICATION DETAILS
CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_KEY = ""
ACCESS_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

global api
api = tweepy.API(auth)


@bot.event
async def on_ready():
    print("online")


@bot.event
async def on_message(message):
    global api
    if str(message.channel.name) == "success":  # Set channel name it is viewing
        try:
            author = str(message.author)
            author = re.split(r'\b#\b', author, maxsplit=1)[0].strip()  # Gets user's name without their tag
            image_url = message.attachments[0].url
            tweet_text = ('New success posted by' + author)  # Adjust how tweet looks
            tweet_image = image_url

            filename = 'temp.jpg'  # Note: a file with this name will be saved in the file location alongside bot.
            request = requests.get(tweet_image, stream=True)
            if request.status_code == 200:
                with open(filename, 'wb') as image:
                    for chunk in request:
                        image.write(chunk)

                upload_tweet = api.update_with_media(filename, status=tweet_text)  # Posts Tweet
                tweet_id = str(upload_tweet.id)
                embed = discord.Embed(title="Success posted !", color=0xe00b0b)
                embed.add_field(name="Success", value=f"https://twitter.com/{upload_tweet.user.screen_name}/status/{upload_tweet.id}\n")
                embed.add_field(name="Delete", value="React below to delete the tweet.")
                embed.set_footer(text="Success Bot")
                success_message = await message.channel.send(embed=embed)
                delete_reaction = await success_message.add_reaction(emoji="\U0001F5D1")
                await asyncio.sleep(0.1)  # Stops wait_for_reaction being triggered by the bot giving itself a reaction


                def check(reaction, user):
                    return user == message.author and str(reaction.emoji) == "\U0001F5D1"

                try:
                    reaction, user = await bot.wait_for('reaction_add', timeout=60.0, check=check)
                except asyncio.TimeoutError:
                    edit_embed = discord.Embed(
                        title="Tweet can't be deleted anymore", color=0xe00b0b)
                    edit_embed.set_footer(text="Success Bot")
                    await success_message.edit(embed=edit_embed)

                else:
                    api.destroy_status(tweet_id)  # Deletes Tweet
                    edit_embed = discord.Embed(
                    title="Tweet was deleted ! Make sure to check images before posting.", color=0x80ff00)
                    edit_embed.set_footer(text="Success Bot")
                    await success_message.edit(embed=edit_embed)

        except IndexError:
            pass

bot.run('YOUR_BOT_TOKEN_HERE')

