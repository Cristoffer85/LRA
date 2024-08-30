from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.properties import StringProperty

class FUNLiveboard(Screen):
    heatlength_selection = StringProperty()

    def on_enter(self):
        heat_length_minutes = int(self.manager.get_screen('FUNRegister').heatlength_selection.split()[0])
        self.heat_length_seconds = heat_length_minutes * 60  # Convert to seconds
        self.start_countdown(self.ids.countdown_label)

    def start_countdown(self, countdown_label):
        self.countdown_time = self.heat_length_seconds
        self.countdown_event = Clock.schedule_interval(lambda dt: self.update_countdown(countdown_label), 1)

    def update_countdown(self, countdown_label):
        minutes, seconds = divmod(self.countdown_time, 60)
        countdown_label.text = f"{minutes:02d}:{seconds:02d}"
        if self.countdown_time <= 0:
            self.countdown_event.cancel()
            self.transition_to_funresult()
        self.countdown_time -= 1

    def transition_to_funresult(self):
        # Automatically transition to FUNResult
        self.manager.transition.direction = 'left'
        self.manager.current = 'FUNResult'
