import pygame

from screens import *

class Game(object):
	def __init__(self, options):
		# Initialize pygame
		pygame.init()
		# Set options
		self.options = options
		# Set screen size
		self.screen = pygame.display.set_mode(self.options["size"], pygame.DOUBLEBUF, 32)
		# Set background image
		self.bg_image = pygame.image.load(self.options["bg_img_file"]).convert()
		# Start playing music
		pygame.mixer.music.load(self.options["bg_music_file"])
		# Set game running invariant
		self.done = False
		# Instantiate states
		self.init_screen_states()
		# Create clock
		self.clock = pygame.time.Clock()
		# Set title
		pygame.display.set_caption(options["title"])
		
	def init_screen_states(self):
		self.title_screen = TitleScreenState(self)
		self.highscores_screen = HighScoreScreenState(self)
		self.pregame_screen = PreGameScreenState(self)
		self.question_screen = QuestionScreenState(self)
		self.answer_screen = AnswerScreenState(self)
		self.results_screen = ResultsScreenState(self)
		
		self.current_screen = self.title_screen
	
	def draw_background(self):
		self.screen.blit(self.bg_image, [0,0])
	
	def run(self):
		# Start playing music
		pygame.mixer.music.play()
		# Game loop
		while self.done == False:
			# Pass event to the current state and see
			# if it wants to handle it
			for event in pygame.event.get():
				# First handle global events,
				# then pass other events to state
				if event.type == pygame.QUIT:
					self.done = True
				else:
					self.current_screen.handle_event(event)

			# Draw background
			self.draw_background()
			# Handle state specific stuff
			self.handle_state()
			# Update screen
			pygame.display.flip()
			# Update clock
			self.clock.tick(self.options["fps"])
	
		# Game is done, now quit!
		pygame.quit()
				
	def handle_state(self):
		self.current_screen.onTitleScreen()
		self.current_screen.onHighScoreScreen()
		self.current_screen.onPreGameScreen()
		self.current_screen.onQuestionScreen()
		self.current_screen.onAnswerScreen()
		self.current_screen.onResultsScreen()
			
		