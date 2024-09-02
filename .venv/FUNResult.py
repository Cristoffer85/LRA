from kivy.uix.screenmanager import Screen

class FUNResult(Screen):

    def go_to_home(self):
        # Navigate to the home screen
        self.manager.transition.direction = 'left'
        self.manager.current = 'Index'