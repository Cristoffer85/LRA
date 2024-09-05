from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.core.audio import SoundLoader

class FUNLiveboard(Screen):
    end_sound = None
# ------------------------------ Take value from FUNRegister saved heatlength and class selection property on_enter, use on this screen ------------------------------
    def on_enter(self):
        fun_register_screen = self.manager.get_screen('FUNRegister')
        
        # Retrieve and display the heat length selection
        heat_length_minutes = int(fun_register_screen.heatlength_selection.split()[0])
        self.heat_length_seconds = heat_length_minutes * 60 
        self.start_countdown(self.ids.countdown_label)

        # Retrieve and display the class selection
        self.class_selection = fun_register_screen.class_selection
        self.ids.class_label.text = f"Class: {self.class_selection}"

        self.end_sound = SoundLoader.load('sounds/race end.mp3')
# ------------------------------ Countdown ------------------------------
    def start_countdown(self, countdown_label):
        self.countdown_time = self.heat_length_seconds
        self.countdown_event = Clock.schedule_interval(lambda dt: self.update_countdown(countdown_label), 1)

    def update_countdown(self, countdown_label):
        minutes, seconds = divmod(self.countdown_time, 60)
        countdown_label.text = f"{minutes:02d}:{seconds:02d}"
        if self.countdown_time <= 0:
            self.countdown_event.cancel()
            self.play_end_sound()
            self.transition_to_funresult()
        self.countdown_time -= 1
# ------------------------------ End sound ------------------------------
    def play_end_sound(self):
        if self.end_sound:
            self.end_sound.play()
# ------------------------------ Navigation ------------------------------
    # Back, to index
    def go_to_home(self):
        self.manager.transition.direction = 'down'
        self.manager.current = 'index'
    # Next, to FUNResult (automatically)
    def transition_to_funresult(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'FUNResult'
