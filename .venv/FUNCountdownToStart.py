from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivy.uix.button import Button  # Import Button class

class FUNCountdownToStart(Screen):
    countdown_event = None  # Track the scheduled countdown event

    def start_countdown(self, countdown_label, next_button):
        if self.countdown_event:  # If a countdown is already running, do nothing
            return

        # Hide all other buttons
        next_button.opacity = 0
        for widget in self.children:
            if isinstance(widget, Button) and widget != next_button:
                widget.opacity = 0

        # Show countdown timer
        countdown_label.opacity = 1
        countdown_label.text = "10"  # Start countdown from 10 seconds
        self.countdown_time = 10
        self.countdown_event = Clock.schedule_interval(lambda dt: self.update_countdown(countdown_label), 1)

    def update_countdown(self, countdown_label):
        if self.countdown_time <= 0:
            self.countdown_event.cancel()
            self.countdown_event = None
            self.go_to_funliveboard()
            return

        # Update countdown label
        countdown_label.text = f"{self.countdown_time:02d}"
        self.countdown_time -= 1

    def go_to_funwarmup(self):
        # Back to Funwarmup screen
        self.manager.transition.direction = 'right'
        self.manager.current = 'FUNWarmup'

    def go_to_funliveboard(self):
        # Next to FunLiveboard screen
        self.manager.transition.direction = 'left'
        self.manager.current = 'FUNLiveboard'
