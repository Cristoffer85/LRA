from kivy.uix.screenmanager import Screen
from kivy.clock import Clock

class FUNWarmup(Screen):
    countdown_event = None  # Track the scheduled countdown event

    def on_enter(self):
        # When the screen is entered, start the countdown
        warmup_time_str = self.manager.get_screen('FUNRegister').warmup_selection.split()[0]
        warmup_time = int(warmup_time_str) * 60  # Convert minutes to seconds
        self.start_countdown(warmup_time)

    def start_countdown(self, warmup_time):
        # Access the countdown label
        countdown_label = self.ids.countdown_label

        # Initialize the countdown time
        self.countdown_time = warmup_time

        # Start the countdown event
        self.countdown_event = Clock.schedule_interval(lambda dt: self.update_countdown(countdown_label), 1)

    def update_countdown(self, countdown_label):
        minutes, seconds = divmod(self.countdown_time, 60)
        countdown_label.text = f"Time Remaining: {minutes:02d}:{seconds:02d}"
        if self.countdown_time <= 0:
            if self.countdown_event:
                self.countdown_event.cancel()
                self.countdown_event = None
            self.go_to_funcountdown()
        self.countdown_time -= 1

    def go_to_funregister(self):
        # Stop the countdown if running
        if self.countdown_event:
            self.countdown_event.cancel()
            self.countdown_event = None
        
        # Make sure the countdown timer is hidden and the Start Registration button is visible
        fun_register_screen = self.manager.get_screen('FUNRegister')
        countdown_label = fun_register_screen.ids.countdown_label
        start_button = fun_register_screen.ids.start_button
        
        countdown_label.text = "Time Remaining: "  # Reset the countdown label
        start_button.disabled = False
        start_button.opacity = 1

        # Transition to the FunRegister screen
        self.manager.transition.direction = 'right'
        self.manager.current = 'FUNRegister'

    def go_to_funcountdown(self):
        # Next to FunCountdown screen
        if self.countdown_event:
            self.countdown_event.cancel()
            self.countdown_event = None
        self.manager.transition.direction = 'left'
        self.manager.current = 'FUNCountdownToStart'
