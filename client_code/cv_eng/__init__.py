from ._anvil_designer import cv_engTemplate
from anvil import *

class cv_eng(cv_engTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
