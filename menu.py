import pygame
		
class TextContainer(object):	
	def __init__(self, screen, menu_items, container, pos):
		self.screen = screen
		self.menu_items = menu_items
		self.container = container
		self.pos = pos
		self.clicked = None
	
	def draw(self):
		self.draw_container()
		self.draw_menu_items()
		
	def handle_event(self, event):
		if (event.type == pygame.MOUSEMOTION):
			for item in self.menu_items:
				item.highlight = item.rect.collidepoint(event.pos)
		elif (event.type == pygame.MOUSEBUTTONDOWN):
			for item in self.menu_items:
				item.on_mouse_button_down(event)
		elif (event.type == pygame.MOUSEBUTTONUP):
			for item in self.menu_items:
				item.on_mouse_button_up(event)
		
	def draw_container(self):
		self.screen.blit(self.container, self.pos)
		
	def draw_menu_items(self):
		for text in self.menu_items:
			text.draw(self.screen)
			
	def update(self, menu_item):
		for item in self.menu_items:
			if not(item.static):
				if item == menu_item:
					item.colour = (255,0,4)
					self.clicked = item
				else:
					item.colour = (255,0,4)