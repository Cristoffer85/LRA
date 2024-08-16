from kivy.uix.screenmanager import Screen

class FUNRegister(Screen):

    def go_to_funstart(self):
        # Back to FunStart screen
        self.manager.transition.direction = 'right'
        self.manager.current = 'FUNStart'

    def go_to_funwarmup(self):
        # Next to FunWarmup screen
        self.manager.transition.direction = 'left'
        self.manager.current = 'FUNWarmup'
