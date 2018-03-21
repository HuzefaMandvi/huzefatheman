import configparser
import praw

config = configparser.ConfigParser()
config.read('config.ini')

bot = praw.Reddit(user_agent='Huzefa_TheMan_Bot',
		client_id='-XompsHslZP7Gw',
		client_secret='rLWt8RLg5QUyHeK42bbi3MIyguk',
		username='Huzefa_TheMan_Bot',
		password=config['ManBot']['password'])

subreddit = bot.subreddit('huzefa_theman')

comments = subreddit.stream.comments()

for comment in comments:
    text = comment.body
    author = comment.author
    if author == 'saworetu':
	message = "Hello, creator."
	comment.reply(message)

