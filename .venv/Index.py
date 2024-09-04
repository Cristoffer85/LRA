from kivy.uix.screenmanager import Screen

class index(Screen):














# ------------------------------ Navigation ------------------------------
    # Forward, to FUNStart
    def go_to_funstart(self): 
        self.manager.transition.direction = 'left'
        self.manager.current = 'FUNStart'
