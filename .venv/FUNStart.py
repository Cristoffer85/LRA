from kivy.uix.screenmanager import Screen
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button

class FUNStart(Screen):

    # Dropdowns
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Initialize dropdowns in the Python file if needed
        self.dropdown1 = DropDown()
        self.dropdown2 = DropDown()
        self.dropdown3 = DropDown()
        self.dropdown4 = DropDown()

    # Navigate back logic
    def go_to_index(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Index'

    # Navigate forward logic
    def go_to_funregister(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'FUNRegister'
