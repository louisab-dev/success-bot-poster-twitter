

<p align="center"> 🤖 Twitter Success Bot Poster (discord.py)
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Installing](#installing)
- [Deploying your own bot](#deployment)

## 🧐 About <a name = "about"></a>

Discord bot to automatically post pictures sent in a specific discord channel on a Twitter account of your choice. All you need is a Twitter developper account and a few steps to set up the bot !



## Installing <a name = "installing"></a>

- Install the libraries needed by running
```
pip install -r requirements.txt
```

- Get your keys and token from https://developer.twitter.com/ and add them at the right spot in the code
Also make sure that the created application can Write (by default it is on Read Only)

- Create a Discord Bot (plenty of tutorials online) and add it to your Discord Server, then get your Bot token and add it at the end of the script

- Run the script, if every thing is working correctly, "online" should be printed and pictures will be posted on your Twitter account


## 🚀 Deploying your own bot <a name = "deployment"></a>

To host your Discord Bot 24/24, you can use Heroku and the process is detailed on a lot of videos that you can find online. I added the Procfile and requirements.txt file in the repository so it will be very easy.


## Sources
- readme.md file template generated with thomascsd's extension (available on VSCode)
