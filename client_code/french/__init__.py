from ._anvil_designer import frenchTemplate
from anvil import *
from ..kef import kef

class french(frenchTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(kef())

  def link_4_click(self, **event_args):
    open_form('home')

  def english_click(self, **event_args):
    open_form('home')

  def french_click(self, **event_args):
    open_form('french')
