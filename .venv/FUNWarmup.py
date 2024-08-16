from kivy.uix.screenmanager import Screen

class FUNWarmup(Screen):

    def go_to_funregister(self):
        # Back to FunRegister screen
        self.manager.transition.direction = 'right'
        self.manager.current = 'FUNRegister'

    def go_to_funcountdown(self):
        # Next to FunCountdown screen
        self.manager.transition.direction = 'left'
        self.manager.current = 'FUNCountdownToStart'
