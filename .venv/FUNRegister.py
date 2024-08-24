from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.properties import StringProperty

class FUNRegister(Screen):
    # String properties to hold the selections
    class_selection = StringProperty()
    registrationtime_selection = StringProperty()
    heatlength_selection = StringProperty()
    warmup_selection = StringProperty()

    # Countdown timer
    def start_countdown(self, countdown_label):
        registration_time_str = self.registrationtime_selection.split()[0]  # Get the numeric part
        registration_time = int(registration_time_str) * 60  # Convert minutes to seconds
        self.countdown_time = registration_time
        self.countdown_event = Clock.schedule_interval(lambda dt: self.update_countdown(countdown_label), 1)

    def update_countdown(self, countdown_label):
        minutes, seconds = divmod(self.countdown_time, 60)
        countdown_label.text = f"Drive your car past Start line.\n\nTime Remaining: {minutes:02d}:{seconds:02d}"
        if self.countdown_time <= 0:
            self.countdown_event.cancel()
            self.go_to_funwarmup()
        self.countdown_time -= 1

    def go_to_funstart(self):
        # Back to FunStart screen
        self.manager.transition.direction = 'right'
        self.manager.current = 'FUNStart'

    def go_to_funwarmup(self):
        # Next to FunWarmup screen
        self.manager.transition.direction = 'left'
        self.manager.current = 'FUNWarmup'
