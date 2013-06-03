import pygame
import pygame._view

from screens import *
from questions import *

class Game(object):
	def __init__(self, options):
		# Initialize mixer
		pygame.mixer.pre_init(44100, -16, 2, 2048)
		# Initialize pygame
		pygame.init()
		# Set options
		self.options = options
		# Set screen size
		self.screen = pygame.display.set_mode(self.options["size"], pygame.SWSURFACE, 32)
		# Set background image
		self.bg_image = pygame.image.load(self.options["bg_img_file"]).convert()
		# Start playing music
		pygame.mixer.music.load(self.options["bg_music_file"])
		# Set game running invariant
		self.done = False
		# Set initial screen
		self.current_screen = TitleScreenState(self)
		# Create clock
		self.clock = pygame.time.Clock()
		# Set title
		pygame.display.set_caption(options["title"])
		# Questions set for game
		self.question_set = None
		# Total time to answer question
		self.total_time = 0
		# Total answers correct
		self.answers_correct = 0
		# Total score
		self.total_score = 0
		# Correct sound
		self.correct_sound = pygame.mixer.Sound(self.options["correct_sound_file"])
		# Incorrect sound
		self.incorrect_sound = pygame.mixer.Sound(self.options["incorrect_sound_file"])
		
	def init_new_game(self, numquestions):
		self.question_set = QuestionSet(numquestions, self.options["q_json_file"])
		self.total_time = 0
		self.answers_correct = 0
		
	def next_question(self):
		return self.question_set.next_question()
		
	def draw_background(self):
		self.screen.blit(self.bg_image, [0,0])
	
	def run(self):
		# Start playing music
		pygame.mixer.music.play(-1)
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
		self.current_screen.onAnswerDescriptionScreen()
		self.current_screen.onResultsScreen()
			
		