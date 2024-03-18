from ._anvil_designer import slump_engTemplate
from anvil import *
import anvil.server

class slump_eng(slump_engTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
