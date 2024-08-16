from kivy.uix.screenmanager import Screen

class FUNCountdownToStart(Screen):
       
    def go_to_funwarmup(self):
        # Back to Funwarmup screen
        self.manager.transition.direction = 'right'
        self.manager.current = 'FUNWarmup'

    def go_to_funliveboard(self):
        # Next to FunLiveboard screen
        self.manager.transition.direction = 'left'
        self.manager.current = 'FUNLiveboard'
