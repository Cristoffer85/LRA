from kivy.uix.screenmanager import Screen

class Index(Screen):
    def go_to_funstart(self): 
        # Function to navigate and set transition
        self.manager.transition.direction = 'left'
        self.manager.current = 'FUNStart'
