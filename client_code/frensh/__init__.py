from ._anvil_designer import frenshTemplate
from anvil import *
from ..kef import kef
from ..geopark import geopark
from ..mineralRessource_copy import mineralRessource_copy
from ..museum import museum
from ..cv import cv



class frensh(frenshTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def vist_kef_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(kef())

  def link_1_click(self, **event_args):
    open_form('home')

  def geoparck_click(self, **event_args):
    
    self.content_panel.clear()
    self.content_panel.add_component(geopark())

  def geology_click(self, **event_args):
    open_form('geology')

  def link_4_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(mineralRessource_copy())

  def link_5_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(museum())

  def link_2_click(self, **event_args):
    self.content_panel.clear()
    self.content_panel.add_component(cv())

  def frensh_mouse_move(self, x, y, **event_args):
    open_form('frensh')

  def english_mouse_down(self, x, y, button, keys, **event_args):
    open_form('english')

  
  

  




