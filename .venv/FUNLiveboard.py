from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.properties import StringProperty
from kivy.core.audio import SoundLoader

class FUNLiveboard(Screen):
    heatlength_selection = StringProperty()
    end_sound = None  # Placeholder for the sound object

    def on_enter(self):
        heat_length_minutes = int(self.manager.get_screen('FUNRegister').heatlength_selection.split()[0])
        self.heat_length_seconds = heat_length_minutes * 60  # Convert to seconds
        self.start_countdown(self.ids.countdown_label)

        # Load the sound file when the screen is entered
        self.end_sound = SoundLoader.load('sounds/race end.mp3')

    def start_countdown(self, countdown_label):
        self.countdown_time = self.heat_length_seconds
        self.countdown_event = Clock.schedule_interval(lambda dt: self.update_countdown(countdown_label), 1)

    def update_countdown(self, countdown_label):
        minutes, seconds = divmod(self.countdown_time, 60)
        countdown_label.text = f"{minutes:02d}:{seconds:02d}"
        if self.countdown_time <= 0:
            self.countdown_event.cancel()
            self.play_end_sound()  # Play the sound when the countdown ends
            self.transition_to_funresult()
        self.countdown_time -= 1

    def play_end_sound(self):
        if self.end_sound:
            self.end_sound.play()

    def transition_to_funresult(self):
        # Automatically transition to FUNResult
        self.manager.transition.direction = 'left'
        self.manager.current = 'FUNResult'

    def go_to_home(self):
        # Navigate to the home screen
        self.manager.transition.direction = 'down'
        self.manager.current = 'Index'
