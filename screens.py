import pygame
import abc

from menu import *
from questions import *
from TextWidget import *

class GameState(object):
	__metaclass__ = abc.ABCMeta

	@abc.abstractmethod
	def onTitleScreen(self):
		return

	@abc.abstractmethod
	def onHighScoreScreen(self):
		return
		
	@abc.abstractmethod
	def onPreGameScreen(self):
		return
		
	@abc.abstractmethod
	def onQuestionScreen(self):
		return
		
	@abc.abstractmethod
	def onAnswerScreen(self):
		return
		
	@abc.abstractmethod
	def onResultsScreen(self):
		return
		
	@abc.abstractmethod
	def handle_event(self, event):
		return

class TitleScreenState(GameState):
	def __init__(self, game):
		# Store reference to Game object
		self.game = game
		# Menu items
		self.menu_items = []
		# New game text
		self.newgame_text = TextWidget("New Game", (255,0,4))
		self.newgame_text.size = 40
		self.newgame_text.font_filename = game.options["font"]
		self.menu_items.append(self.newgame_text)
		# High score text
		self.highscore_text = TextWidget("High Scores", (255,0,4))
		self.highscore_text.size = 40
		self.highscore_text.font_filename = game.options["font"]
		self.menu_items.append(self.highscore_text)
		# Menu container
		self.menu_container = TextContainer(game.screen, self.menu_items, game.options["menu_container_colour"])
		# Attach observer
		self.newgame_text.attach(self.menu_container)
		self.highscore_text.attach(self.menu_container)
			
	def onTitleScreen(self):
		# Render menu
		self.menu_container.draw()
		
		return
		
	def onHighScoreScreen(self):
		return
		
	def onPreGameScreen(self):
		return
		
	def onQuestionScreen(self):
		return
		
	def onAnswerScreen(self):
		return
		
	def onResultsScreen(self):
		return
		
	def handle_event(self, event):
		# Handle events
		self.menu_container.handle_event(event)
		
		if event.type == TEXT_WIDGET_CLICK:
			if event.text_widget == self.newgame_text:
				print "Click new game"
				self.game.current_screen = PreGameScreenState(self.game)
					
		return
					
class HighScoreScreenState(GameState):
	def __init__(self, game):
		# Store reference to Game object
		self.game = game	
	
	def onTitleScreen(self):
		return
		
	def onHighScoreScreen(self):
		# Do something
		return
		
	def onPreGameScreen(self):
		return
		
	def onQuestionScreen(self):
		return
		
	def onAnswerScreen(self):
		return
		
	def onResultsScreen(self):
		return
		
	def handle_event(self, event):
		# Handle events	
		return

class PreGameScreenState(GameState):
	def __init__(self, game):
		# Store reference to Game object
		self.game = game
		# Text Items
		self.menu_items = []
		# Question Text
		self.question_text = TextWidget("How many questions do you want?", (0,0,0), static=True)
		self.question_text.size = 24
		self.question_text.font_filename = game.options["font"]
		self.menu_items.append(self.question_text)
		# Responses Text
		self.ten_questions_text = TextWidget("10", (255,0,4))
		self.ten_questions_text.size = 32
		self.ten_questions_text.font_filename = game.options["font"]
		self.menu_items.append(self.ten_questions_text)
		
		self.twenty_questions_text = TextWidget("20", (255,0,4))
		self.twenty_questions_text.size = 32
		self.twenty_questions_text.font_filename = game.options["font"]
		self.menu_items.append(self.twenty_questions_text)
		
		self.thirty_questions_text = TextWidget("30", (255,0,4))
		self.thirty_questions_text.size = 32
		self.thirty_questions_text.font_filename = game.options["font"]
		self.menu_items.append(self.thirty_questions_text)
		# Container
		self.menu_container = TextContainer(self.game.screen, self.menu_items, self.game.options["menu_container_colour"])
		# Attach observer
		self.ten_questions_text.attach(self.menu_container)
		self.twenty_questions_text.attach(self.menu_container)
		self.thirty_questions_text.attach(self.menu_container)
		
	def onTitleScreen(self):
		return
		
	def onHighScoreScreen(self):
		return
		
	def onPreGameScreen(self):
		# Do something
		self.menu_container.draw()
		
	def onQuestionScreen(self):
		return
		
	def onAnswerScreen(self):
		return
		
	def onResultsScreen(self):
		return
		
	def handle_event(self, event):
		self.menu_container.handle_event(event)
	
		if event.type == TEXT_WIDGET_CLICK and event.text_widget != self.question_text:
			num_questions = int(event.text_widget.text)
			self.game.create_question_set(num_questions)
			self.game.current_screen = QuestionScreenState(self.game, self.game.next_question())
	
		return
		
class QuestionScreenState(GameState):
	def __init__(self, game, question):
		# Store reference to Game object
		self.game = game
		# Question
		self.question = question
		# Setup container
	
	def onTitleScreen(self):
		return
		
	def onHighScoreScreen(self):
		return
		
	def onPreGameScreen(self):
		return
		
	def onQuestionScreen(self):
		# Do something
		return
		
	def onAnswerScreen(self):
		return
		
	def onResultsScreen(self):
		return
		
	def handle_event(self, event):
		# Handle events	
		return

class AnswerScreenState(GameState):
	def __init__(self, game):
		# Store reference to Game object
		self.game = game	
	
	def onTitleScreen(self):
		return
		
	def onHighScoreScreen(self):
		return
		
	def onPreGameScreen(self):
		return
		
	def onQuestionScreen(self):
		return
		
	def onAnswerScreen(self):
		# Do something
		return
		
	def onResultsScreen(self):
		return
		
	def handle_event(self, event):
		# Handle events	
		return

class ResultsScreenState(GameState):
	def __init__(self, game):
		# Store reference to Game object
		self.game = game	
	
	def onTitleScreen(self):
		return
		
	def onHighScoreScreen(self):
		return
		
	def onPreGameScreen(self):
		return
		
	def onQuestionScreen(self):
		return
		
	def onAnswerScreen(self):
		return
		
	def onResultsScreen(self):
		# Do something
		return
		
	def handle_event(self, event):
		# Handle events	
		return
