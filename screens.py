import pygame
import abc
import time

from menu import *
from questions import *
from TextWidget import *
from eztext import Input

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
				self.game.current_screen = None
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
			self.game.init_new_game(num_questions)
			# Remove reference
			self.game.current_screen = None
			self.game.current_screen = QuestionScreenState(self.game)
	
		return
		
class QuestionScreenState(GameState):
	def __init__(self, game):
		# Store reference to Game object
		self.game = game
		# Question
		self.question = game.next_question()
		# Menu items
		if self.question != None:
			self.menu_items = []
			# Setup question text
			self.question_text = TextWidget(self.question.question_str, (0,0,0), static=True)
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
			self.score_text = TextWidget(str(self.question.score), (255,0,4), static=True)
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
			
	def onTitleScreen(self):
		return
		
	def onHighScoreScreen(self):
		return
		
	def onPreGameScreen(self):
		return
		
	def onQuestionScreen(self):
		if self.question != None:
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
		else:
			self.game.current_screen = None
			self.game.current_screen = ResultsScreenState(self.game)
	
	def onAnswerScreen(self):
		return
		
	def onResultsScreen(self):
		return
		
	def handle_event(self, event):
		if self.question != None:
			self.menu_container.handle_event(event)
		
			if event.type == TEXT_WIDGET_CLICK:
				user_response = event.text_widget.text
				# fix here
				self.game.current_screen = None
				if (user_response == self.question.correct_response):
					self.game.answers_correct = self.game.answers_correct + 1
					self.game.total_score = self.game.total_score + self.current_score
					self.game.current_screen = AnswerScreenState(self.game, True)
				else:
					self.game.current_screen = AnswerScreenState(self.game, False)
				
				self.game.total_time = self.game.total_time + self.current_time
		
		return

class AnswerScreenState(GameState):
	def __init__(self, game, user_correct, description=None):
		# Store reference to Game object
		self.game = game
		# Was user's answer correct?
		self.correct = user_correct
		# Detailed answer
		self.description = description
		# Menu items
		self.menu_items = []
		# Images
		if self.correct:
			self.image_sf = pygame.image.load(self.game.options["correct_img_file"]).convert()
			self.result_text = TextWidget("Correct!", (255,0,4), static=True)
		else:
			self.image_sf = pygame.image.load(self.game.options["incorrect_img_file"]).convert()
			self.result_text = TextWidget("Incorrect!", (255,0,4), static=True)
			
		self.image_rect = self.image_sf.get_rect(center=self.game.screen.get_rect().center)
		self.image_rect.top = 40
		
		self.result_text.size = 32
		self.result_text.font_filename = game.options["font"]
		self.result_text.rect.center = self.image_rect.center
		self.result_text.rect.top = self.image_rect.bottom + 55
		
		# Create continue menu
		self.continue_text = TextWidget("Continue", (255,0,4))
		self.continue_text.size = 40
		self.continue_text.font_filename = self.game.options["font"]
		self.menu_items.append(self.continue_text)
		
		self.menu_container = TextContainer(game.screen, self.menu_items, game.options["menu_container_colour"], top=self.result_text.rect.bottom + 60)
		
	
	def draw_result_img(self):
		self.game.screen.blit(self.image_sf, self.image_rect)
	
	def onTitleScreen(self):
		return
		
	def onHighScoreScreen(self):
		return
		
	def onPreGameScreen(self):
		return
		
	def onQuestionScreen(self):
		return
		
	def onAnswerScreen(self):
		self.draw_result_img()
		self.result_text.draw(self.game.screen)
		self.menu_container.draw()
		
		return
		
	def onResultsScreen(self):
		return
		
	def handle_event(self, event):
		# Handle events	
		self.menu_container.handle_event(event)
		
		# Fix this!!
		if event.type == TEXT_WIDGET_CLICK:
			self.game.current_screen = None
			self.game.current_screen = QuestionScreenState(self.game)
		
		return

class ResultsScreenState(GameState):
	def __init__(self, game):
		# Store reference to Game object
		self.game = game
		self.input = Input(maxlength=3, x=30, y= 40, color=(255,0,4), prompt="Name:")
		# Stats
		self.container_sf = pygame.Surface((215, 125), pygame.SRCALPHA, 32)
		self.container_sf.fill(game.options["menu_container_colour"])
		self.container_rect = self.container_sf.get_rect(center=game.screen.get_rect().center)
		self.container_rect.top = 100
		
		self.time_label = TextWidget("Time:", (255,0,4), static=True)
		self.time_label.size = 32
		self.time_label.font_filename = game.options["font"]
		self.time_label.rect.top = self.container_rect.top + 5
		self.time_label.rect.left = self.container_rect.left + 5
		
		self.time_text = TextWidget(str(game.total_time), (255,0,4), static=True)
		self.time_text.size = 32
		self.time_text.font_filename = game.options["font"]
		self.time_text.rect.top = self.time_label.rect.top
		self.time_text.rect.left = self.time_label.rect.left + self.time_label.rect.width + 5
		
		self.score_label = TextWidget("Score:", (255,0,4), static=True)
		self.score_label.size = 32
		self.score_label.font_filename = game.options["font"]
		self.score_label.rect.top = self.time_text.rect.bottom + 10
		self.score_label.rect.left = self.container_rect.left + 5
		
		self.score_text = TextWidget(str(game.total_score), (255,0,4), static=True)
		self.score_text.size = 32
		self.score_text.font_filename = game.options["font"]
		self.score_text.rect.top = self.score_label.rect.top
		self.score_text.rect.left = self.score_label.rect.left + self.score_label.rect.width + 5
	
		self.correct_label = TextWidget("Correct:", (255,0,4), static=True)
		self.correct_label.size = 32
		self.correct_label.font_filename = game.options["font"]
		self.correct_label.rect.top = self.score_text.rect.bottom + 10
		self.correct_label.rect.left = self.container_rect.left + 5
		
		total_correct = str(int(game.answers_correct/float(len(game.question_set.questions))*100)) + "%"
		self.correct_text = TextWidget(total_correct, (255,0,4), static=True)
		self.correct_text.size = 32
		self.correct_text.font_filename = game.options["font"]
		self.correct_text.rect.top = self.correct_label.rect.top
		self.correct_text.rect.left = self.correct_label.rect.left + self.correct_label.rect.width + 5
	
		# Menu items
		self.menu_items = []
		
		self.title_screen_text = TextWidget("Title Screen", (255,0,4))
		self.title_screen_text.size = 40
		self.title_screen_text.font_filename = game.options["font"]
		self.menu_items.append(self.title_screen_text)
		
		self.menu_container = TextContainer(game.screen, self.menu_items, game.options["menu_container_colour"], top=self.container_rect.bottom+200)
	
	def draw_container(self):
		self.game.screen.blit(self.container_sf, self.container_rect)
	
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
		self.draw_container()
	
		#self.input.draw(self.game.screen)
		self.time_label.draw(self.game.screen)
		self.time_text.draw(self.game.screen)
		self.score_label.draw(self.game.screen)
		self.score_text.draw(self.game.screen)
		self.correct_label.draw(self.game.screen)
		self.correct_text.draw(self.game.screen)
		
		self.menu_container.draw()
		
		
		return
		
	def handle_event(self, event):
		self.input.update(event)
		self.menu_container.handle_event(event)
		
		if event.type == TEXT_WIDGET_CLICK:
			if event.text_widget == self.title_screen_text:
				self.game.current_screen = TitleScreenState(self.game)
		
		return
