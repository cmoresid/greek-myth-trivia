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
		self.newgame_text.rect.center = self.game.screen.get_rect().center
		self.newgame_text.rect.top = 200;
		self.menu_items.append(self.newgame_text)
		# High score text
		self.highscore_text = TextWidget("High Scores", (255,0,4))
		self.highscore_text.size = 40
		self.highscore_text.font_filename = game.options["font"]
		self.highscore_text.rect.center = self.game.screen.get_rect().center
		self.highscore_text.rect.top = self.newgame_text.rect.bottom + 10;
		self.menu_items.append(self.highscore_text)
		# Menu container
		menu_container_rect = pygame.Surface((250,90), pygame.SRCALPHA, 32)
		menu_container_rect.fill(game.options["menu_container_color"])
		self.menu_container = TextContainer(self.game.screen, self.menu_items, menu_container_rect, (220,200))
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
				print "Click new game."
					
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
		# Menu font
		
	
	def onTitleScreen(self):
		return
		
	def onHighScoreScreen(self):
		return
		
	def onPreGameScreen(self):
		# Do something
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
		
class QuestionScreenState(GameState):
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
