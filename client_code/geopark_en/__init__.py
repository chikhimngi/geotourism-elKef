from ._anvil_designer import geopark_enTemplate
from anvil import *

class geopark_en(geopark_enTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
