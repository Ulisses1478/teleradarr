import telebot
from .config import CONFIG
from telebot import types
from .api import radarr
import json

bot = telebot.TeleBot(CONFIG['telegram']['botToken'])

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, f'Oi {message.from_user.first_name}, como vai você?')

@bot.chosen_inline_handler(func=lambda chosen_inline_result: True)
def test_chosen(chosen_inline_result):
	api = radarr()

	# Search Movie
	moviesQuery = api.searchMovies(chosen_inline_result.query, limit=5)
	movie = moviesQuery[int(chosen_inline_result.result_id)]

	# Add movie and log
	print(chosen_inline_result.from_user.first_name+' Added the movie: ' + movie.get('title'))	

	# # Alert
	# title = movie.get('title') # Movie name
	# bot.reply_to(chosen_inline_result, f'Oi {chosen_inline_result.from_user.first_name}, já estou baixando o filme {title} pra você')

@bot.inline_handler(lambda query: query.query)
def query_text(inline_query):
	movies = []
	moviesQuery = radarr().searchMovies(inline_query.query, limit=5)

	for index, movie in enumerate(moviesQuery):
		title = movie.get('title')
		movies.append(
			types.InlineQueryResultArticle(
				index,
				movie.get('title'),
				types.InputTextMessageContent(f'Oi {inline_query.from_user.first_name}, já estou baixando o filme {title} pra você'),
				thumb_url=movie.get('remotePoster'),
				thumb_height=1050,
				thumb_width=700
			)
		)

	print(inline_query.from_user.first_name+' Searched Movies')
	try:
	    bot.answer_inline_query(inline_query.id, movies)
	except Exception as e:
	    print(e)

def startBot():
	return bot.polling()
