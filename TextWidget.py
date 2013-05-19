#! /usr/bin/env python

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# If you find any bugs or have any suggestions email: selsine@gmail.com
# URL: http://www.learningpython.com
#
# Feel free to use this in whatever manner you want, but if you do end up using
# it, I would appreciate it if you sent me an email and let me know.

"""
History:

0.1.1: 2008/09/24
- Fixed a bug where pygame.local.USEREVENT was not defined for some
versions of pygame. Switched to pygame.USEREVENT. May have to make this
switch based on pygame versions at some point.

0.1: 2008/09/21

- Fixed a bug where the font filename was always being treated as
a full path.
- Fixed a bug where an exception thrown when trying to create the
the PyGame font was not being handled well. Now if the font creation
fails TextWidget will try to use the default font.

Initial release: 2006/12/18
"""

__author__ = "Mark Mruss <selsine@gmail.com>"
__version__ = "0.1"
__date__ = "Date: 2008/09/21"
__copyright__ = "Copyright (c) 2008 Mark Mruss"
__license__ = "LGPL"

import os
import pygame
import observer

TEXT_WIDGET_CLICK = pygame.USEREVENT + 1

class TextWidget(observer.Subject):
    """This is a helper class for handling text in PyGame.  It performs
    some basic highlighting and tells you when the text has been clicked.
    This is just one of the many ways to handle your text.
    This is a new-style class and I am somewhat new to them so hopefully it
    all works.
    """
    #Hand Cursor
    __hand_cursor_string = (
    "     XX         ",
    "    X..X        ",
    "    X..X        ",
    "    X..X        ",
    "    X..XXXXX    ",
    "    X..X..X.XX  ",
    " XX X..X..X.X.X ",
    "X..XX.........X ",
    "X...X.........X ",
    " X.....X.X.X..X ",
    "  X....X.X.X..X ",
    "  X....X.X.X.X  ",
    "   X...X.X.X.X  ",
    "    X.......X   ",
    "     X....X.X   ",
    "     XXXXX XX   ")
    __hcurs, __hmask = pygame.cursors.compile(__hand_cursor_string, ".", "X")
    __hand = ((16, 16), (5, 1), __hcurs, __hmask)
    #Text
    def __get_text(self):
        return self.__m_text
    def __set_text(self, text):
        if (self.__m_text != text):
            self.__m_text = text
            self.update_surface()
    def __del_text(self):
        del self.__m_text
    def __doc_text(self):
        return "The text to be displayed by the text widget"
    text = property(__get_text, __set_text, __del_text, __doc_text)
    #Colour
    def __get_colour(self):
        return self.__m_colour
    def __set_colour(self, colour):
        if (self.__m_colour != colour):
            self.__m_colour = colour
            self.update_surface()
    colour = property(__get_colour, __set_colour)
    #Size
    def __get_size(self):
        return self.__m_size
    def __set_size(self, size):
        if (self.__m_size != size):
            self.__m_size = size
            self.create_font()
    size = property(__get_size, __set_size)
    #Font Filename
    def __get_font_filename(self):
        return self.__m_font_filename
    def __set_font_filename(self, font_filename):
        if (self.__m_font_filename != font_filename):
            self.__m_font_filename = font_filename
            #Is this a full path?
            if (not os.access(self.__m_font_filename, os.F_OK)):
                #Join with the local path to try to get the full path
                self.__m_font_filename = os.path.join(self.__local_path
                    , self.__m_font_filename)
            self.create_font()
    font_filename = property(__get_font_filename, __set_font_filename)
    #Highlight
    def __get_highlight(self):
        return self.__m_highlight
    def __set_highlight(self, highlight):
        if (not(self.__m_highlight == highlight)):
            #Save the bold_rect
            if (self.__m_highlight):
                self.bold_rect = self.rect
            self.__m_highlight = highlight
            #update the cursor
            self.update_cursor()
            if (highlight):
                self.size += self.highlight_increase
            else:
                self.size -= self.highlight_increase
            if (self.highlight_increase == 0):
                self.create_font()
    highlight = property(__get_highlight, __set_highlight)
    #Show Highlight Cursor
    def __get_highlight_cursor(self):
        return self.__m_highlight_cursor
    def __set_highlight_cursor(self, highlight_cursor):
        if (self.__m_highlight_cursor != highlight_cursor):
            self.__m_highlight_cursor = highlight_cursor
            self.update_cursor()
    highlight_cursor = property(__get_highlight_cursor, __set_highlight_cursor)

    def __init__(self, text="", colour=(0,0,0), size=32
                , highlight_increase = 0, font_filename=None
                , show_highlight_cursor = True):
        """Initialize the TextWidget
        @param text = "" - string - The text for the text widget
        @param colour = (0,0,0) - The colour of the text
        @param size = 32 - number - The size of the text
        @param highlight_increase - number - How large do we want the
        text to grow when it is highlighted?
        @param font_filename = None - string the patht to the font file
        to use, None to use the default pygame font.
        @param show_highlight_cursor = True - boolean - Whether or not to change
        the cursor when the text is highlighted.  The cursor will turn into
        a hand if this is true.
        """

		# Initialize parent class
        observer.Subject.__init__(self)
		
        #inits
        self.dirty = False
        self.bold_rect = None
        self.highlight_increase = highlight_increase
        self.tracking = False
        self.rect = None

        #Get the local path
        self.__local_path = os.path.realpath(os.path.dirname(__file__))

        #property inits
        self.__m_text = None
        self.__m_colour = None
        self.__m_size = None
        self.__m_font_filename = None
        self.__m_highlight = False
        self.__m_font = None
        self.__m_highlight_cursor = False
        self.__m_rect = None

        self.text = text
        self.colour = colour
        self.size = size
        self.font_filename = font_filename
        self.highlight = False
        self.highlight_cursor = show_highlight_cursor

        self.create_font()

    def __str__(self):
        return "TextWidget: %s at %s" % (self.text, self.rect)

    def update_cursor(self):
        if (self.highlight_cursor):
            if (self.highlight):
                pygame.mouse.set_cursor(*self.__hand)
            else:
                pygame.mouse.set_cursor(*pygame.cursors.arrow)

    def create_font(self):
        """Create the internal font, using the current settings
        """
        if (self.size):
            try:
                self.__m_font = pygame.font.Font(self.font_filename
                    , self.size)
            except Exception, e:
                print("Error creating font: '%s' using file: '%s'" % (
                    str(e), self.font_filename))
                print("Trying with default font")
                self.__m_font = pygame.font.Font(None, self.size)

            self.update_surface()

    def update_surface(self):
        """Update the current surface, basically render the
        text using the current settings.
        """
        if (self.__m_font):
            self.__m_font.set_bold(self.highlight)
            self.image = self.__m_font.render(self.text
                , True
                , self.colour)
            self.dirty = True
            if (self.rect):
                # Used the current rects center point
                self.rect = self.image.get_rect(center=self.rect.center)
            else:
                self.rect = self.image.get_rect()

    def draw(self, screen):
        """Draw yourself text widget
        @param screen - pygame.Surface - The surface that we will draw to
        @returns - pygame.rect - If drawing has occurred this is the
        rect that we drew to.  None if no drawing has occurerd."""

        rect_return = None
        if ((self.image)  and  (self.rect) and (self.dirty)):
            if (self.bold_rect):
                """We may need to overwrite the bold text size
                This gets rid of leftover text when moving from
                bold text to non-bold text.
                """
                rect_return = pygame.Rect(self.bold_rect)
                """Set to None, since we only need to do this
                once."""
                self.bold_rect = None
            else:
                rect_return = self.rect
            #Draw the text
            screen.blit(self.image, self.rect)
            #Dirty no more
            self.dirty = True

            return rect_return

    def on_mouse_button_down(self, event):
        """Called by the main application when the
        MOUSEBUTTONDOWN event fires.
        @param event - Pygame Event object
        MOUSEBUTTONDOWN  pos, button
        """
        #Check for collision
        self.tracking = False
        if (self.rect.collidepoint(event.pos)):
            self.tracking = True

    def on_mouse_button_up(self, event):
        """Called by the main application when the
        MOUSEBUTTONDOWN event fires.
        @param event - Pygame Event object
        MOUSEBUTTONDOWN  pos, button
        """
        #Check for collision
        if ((self.tracking) and (self.rect.collidepoint(event.pos))):
            #Not Tracking anymore
            self.tracking = False
            self.on_mouse_click(event)

    def on_mouse_click(self, event):
        """Called by the main application when the
        MOUSEBUTTONDOWN event fires, and the text widget
        has been clicked on.  You can either let
        this post the event (default) or you can override this
        function call in your app.
        ie. myTextWidget.on_mouse_click = my_click_handler
        @param event - Pygame Event object
        MOUSEBUTTONDOWN  pos, button
        """
        #Create the TEXT_WIDGET_CLICK event
        event_attrib = {}
        event_attrib["button"] = event.button
        event_attrib["pos"] = event.pos
        event_attrib["text_widget"] = self
        e = pygame.event.Event(TEXT_WIDGET_CLICK, event_attrib)
        pygame.event.post(e)
		
		# Notify observers of update
        self.notify()

