from kivy.uix.screenmanager import Screen

class FUNLiveboard(Screen):
        
    def go_to_funcountdown(self):
        # Back to FunCountdown screen
        self.manager.transition.direction = 'right'
        self.manager.current = 'FUNCountdownToStart'

    def go_to_funresult(self):
        # Next to FunResult screen
        self.manager.transition.direction = 'left'
        self.manager.current = 'FUNResult'