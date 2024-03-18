from ._anvil_designer import englishTemplate
from anvil import *
from ..kef import kef

class english(englishTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(kef())

  def link_4_click(self, **event_args):
    open_form('english')

  def english_click(self, **event_args):
    open_form('home')

  def french_click(self, **event_args):
    open_form('french')

  def image_1_mouse_up(self, x, y, button, **event_args):
    open_form('french')

  def image_2_mouse_up(self, x, y, button, **event_args):
    open_form('french')

  def image_1_mouse_down(self, x, y, button, keys, **event_args):
    open_form('home')

  def image_2_mouse_down(self, x, y, button, keys, **event_args):
    open_form('french')

  def french_mouse_down(self, x, y, button, keys, **event_args):
    open_form('frensh')

  def englis_mouse_down(self, x, y, button, keys, **event_args):
    open_form('english')

  def tunis_mouse_down(self, x, y, button, keys, **event_args):
    """This method is called when a mouse button is pressed on this component"""
    pass
