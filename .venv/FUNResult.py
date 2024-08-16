from kivy.uix.screenmanager import Screen

class FUNResult(Screen):

    def go_to_funliveboard(self):
        # Back to FunLiveboard screen
        self.manager.transition.direction = 'right'
        self.manager.current = 'FUNLiveboard'

    def go_to_index(self):
        # Next to Index screen
        self.manager.transition.direction = 'left'
        self.manager.current = 'Index'