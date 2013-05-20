import pygame
import abc
import time

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
		# Menu items
		self.menu_items = []
		# Setup question text
		self.question_text = TextWidget(question.question_str, (0,0,0), static=True)
		self.question_text.size = 24
		self.question_text.font_filename = game.options["font"]
		self.menu_items.append(self.question_text)
		# Setup time text
		self.current_time_text = TextWidget("0", (255,0,4), static=True)
		self.current_time_text.size = 24
		self.current_time_text.font_filename = game.options["font"]
		self.current_time_text.rect.top = 10
		self.current_time_text.rect.left = self.game.options["size"][0] - self.current_time_text.rect.width - 40
		
		self.current_time_label = TextWidget("Time:", (255,0,4), static=True)
		self.current_time_label.size = 24
		self.current_time_label.font_filename = game.options["font"]
		self.current_time_label.rect.top = 10
		self.current_time_label.rect.left = self.current_time_text.rect.left - self.current_time_label.rect.width - 10
		
		# Setup score text
		self.score_text = TextWidget(str(question.score), (255,0,4), static=True)
		self.score_text.size = 24
		self.score_text.font_filename = game.options["font"]
		self.score_text.rect.top = self.current_time_text.rect.bottom + 10
		self.score_text.rect.left = self.game.options["size"][0] - self.score_text.rect.width - 20
		
		self.score_label = TextWidget("Score:", (255,0,4), static=True)
		self.score_label.size = 24
		self.score_label.font_filename = game.options["font"]
		self.score_label.rect.top = self.score_text.rect.top
		self.score_label.rect.left = self.score_text.rect.left - self.score_label.rect.width - 10
		
		# Setup responses
		for response in self.question.responses:
			response_text = TextWidget(response, (255,0,4))
			response_text.size = 28
			response_text.font_filename = game.options["font"]
			self.menu_items.append(response_text)
		# Menu container
		self.menu_container = TextContainer(self.game.screen, self.menu_items, self.game.options["menu_container_colour"])
		# Register observer
		for item in self.menu_items:
			item.attach(self.menu_container)
		# For scoring scheme
		self.next_score_time = 0
		self.next_second_time = 0
		# Current score
		self.current_score = self.question.score
		# Current time
		self.current_time = 0
	
	def update_timer(self):
		current_time = time.time()
		
		if self.next_score_time == 0:
			self.next_score_time = current_time + 1
		
		if current_time >= self.next_score_time:
			# Question loses 10% of score value every second
			if self.current_score > 0:
				self.current_score = int(self.current_score - (self.question.score*0.1))
				self.score_text.text = str(self.current_score)
			self.current_time = self.current_time + 1
			self.current_time_text.text = str(self.current_time)
			self.next_score_time = time.time() + 1
			print self.current_score
			
	def onTitleScreen(self):
		return
		
	def onHighScoreScreen(self):
		return
		
	def onPreGameScreen(self):
		return
		
	def onQuestionScreen(self):
		# Draw question box
		self.menu_container.draw()
		# Draw current time
		self.current_time_label.draw(self.game.screen)
		self.current_time_text.draw(self.game.screen)
		# Draw score
		self.score_label.draw(self.game.screen)
		self.score_text.draw(self.game.screen)
		# Update score
		self.update_timer()
	
	def onAnswerScreen(self):
		return
		
	def onResultsScreen(self):
		return
		
	def handle_event(self, event):
		self.menu_container.handle_event(event)
		
		if event.type == TEXT_WIDGET_CLICK:
			user_response = event.text_widget.text
			
			if (user_response == self.question.correct_response):
				print "Correct response."
				self.game.answers_correct = self.game.answers_correct + 1
				self.game.current_screen = AnswerScreenState(self.game, True)
			else:
				print "Incorrect!"
				self.game.current_screen = AnswerScreenState(self.game, False)
				
			self.game.total_time = self.game.total_time + self.current_time
		
		return

class AnswerScreenState(GameState):
	def __init__(self, game, user_correct):
		# Store reference to Game object
		self.game = game
		# Was user's answer correct?
		self.correct = user_correct
	
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
