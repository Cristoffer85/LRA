from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty

class FUNStart(Screen):
    # Properties to store selected dropdown values
    class_selection = StringProperty("2WD")
    registrationtime_selection = StringProperty("1 min")
    heatlength_selection = StringProperty("5 min")
    warmup_selection = StringProperty("1 min")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    # Navigate back logic
    def go_to_index(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'Index'

    # Navigate forward logic
    def go_to_funregister(self):
        # Set the selected values in FUNRegister screen
        funregister_screen = self.manager.get_screen('FUNRegister')
        funregister_screen.class_selection = self.class_selection
        funregister_screen.registrationtime_selection = self.registrationtime_selection
        funregister_screen.heatlength_selection = self.heatlength_selection
        funregister_screen.warmup_selection = self.warmup_selection

        # Navigate to FUNRegister screen
        self.manager.transition.direction = 'left'
        self.manager.current = 'FUNRegister'
