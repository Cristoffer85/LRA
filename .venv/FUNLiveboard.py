from kivy.uix.screenmanager import Screen

class FUNLiveboard(Screen):
        
    def go_to_index(self):
        # Transition to the Index screen
        self.manager.transition.direction = 'left'
        self.manager.current = 'Index'

    def go_to_funcountdown(self):
        # Transition to the FunCountdown screen
        self.manager.transition.direction = 'right'
        self.manager.current = 'FUNCountdownToStart'