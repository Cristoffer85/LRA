from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.properties import StringProperty, BooleanProperty

class FUNRegister(Screen):
    class_selection = StringProperty()
    registrationtime_selection = StringProperty()
    heatlength_selection = StringProperty()
    warmup_selection = StringProperty()
    shortest_laptime_selection = StringProperty()
    auto_start_after_warmup = BooleanProperty(False)

    countdown_event = None  # Track the scheduled countdown event

    def start_countdown(self, countdown_label, start_button):
        if self.countdown_event:  # If a countdown is already running, do nothing
            return

        # Hide and disable the Start Registration button after pressing it
        start_button.disabled = True
        start_button.opacity = 0

        registration_time_str = self.registrationtime_selection.split()[0]  # Get the numeric part
        registration_time = int(registration_time_str) * 60  # Convert minutes to seconds
        self.countdown_time = registration_time

        # Show the countdown label
        countdown_label.opacity = 1  # Make the countdown label visible
        self.countdown_event = Clock.schedule_interval(lambda dt: self.update_countdown(countdown_label), 1)

    def update_countdown(self, countdown_label):
        minutes, seconds = divmod(self.countdown_time, 60)
        countdown_label.text = f"Time Remaining: {minutes:02d}:{seconds:02d}"
        if self.countdown_time <= 0:
            self.countdown_event.cancel()
            self.countdown_event = None
            self.reset_countdown(countdown_label, self.ids.start_button)  # Reset before transitioning
            self.go_to_funwarmup()
        self.countdown_time -= 1

    def reset_countdown(self, countdown_label, start_button):
        if self.countdown_event:
            self.countdown_event.cancel()
            self.countdown_event = None  # Reset the countdown event
            self.countdown_time = 0

        # Hide countdown label again when pressing the back button
        countdown_label.opacity = 0  # Hide the countdown label

        # Re-enable and show the Start Registration button
        start_button.disabled = False
        start_button.opacity = 1

    def go_to_funstart(self):
        countdown_label = self.ids.countdown_label
        start_button = self.ids.start_button
        self.reset_countdown(countdown_label, start_button)
        self.manager.transition.direction = 'right'
        self.manager.current = 'FUNStart'

    def go_to_funwarmup(self):
        countdown_label = self.ids.countdown_label
        start_button = self.ids.start_button
        self.reset_countdown(countdown_label, start_button)  # Ensure reset happens before transition
        # Navigate to FunWarmup
        self.manager.transition.direction = 'left'
        self.manager.current = 'FUNWarmup'