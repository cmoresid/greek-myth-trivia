import pygame
		
class TextContainer(object):	
	def __init__(self, screen, menu_items, colour, top=None):
		self.screen = screen
		self.menu_items = menu_items
		self.clicked = None
		self.colour = colour
		self.top = top
		# Create menu container
		self.container_sf, self.container_rect = self.create_container()
		# Realign menu items
		self.realign_menu_items()
		
	def create_container(self):
		# Get item with largest width
		widest_item = max(self.menu_items, key=lambda item: item.rect.width)
		container_height = 0
		container_width = widest_item.rect.width
		
		# Leave 5 pixels on for border
		container_width = container_width + 20
		for item in self.menu_items:
			container_height = container_height + item.rect.height + 10
			
		menu_container_sf = pygame.Surface((container_width, container_height), pygame.SRCALPHA, 32)
		menu_container_sf.fill(self.colour)
		menu_container_rect = menu_container_sf.get_rect(center=self.screen.get_rect().center)
		
		if self.top != None:
			menu_container_rect.top = self.top
		
		return (menu_container_sf, menu_container_rect)
	
	def realign_menu_items(self):
		previous_rect = self.container_rect.top + 5
		
		for item in self.menu_items:
			item.rect.center = self.container_rect.center
			item.rect.top = previous_rect
			
			previous_rect = item.rect.bottom + 10
	
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
		self.screen.blit(self.container_sf, self.container_rect)
		
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