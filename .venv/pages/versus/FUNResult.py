from kivy.uix.screenmanager import Screen

class FUNResult(Screen):










# ------------------------------ Navigation ------------------------------
    # Back, to index
    def go_to_home(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'index'