from ._anvil_designer import kef_engTemplate
from anvil import *

class kef_eng(kef_engTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
